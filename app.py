import base64
import io
import json
import time
from pathlib import Path
import streamlit as st
import openai
from google import genai
from google.genai import types as genai_types
import pandas as pd
from streamlit_local_storage import LocalStorage

_PROMPTS_DIR = Path(__file__).parent / "prompts"


def _load_prompt(filename: str) -> str:
    return (_PROMPTS_DIR / filename).read_text(encoding="utf-8").strip()


SYSTEM_PROMPT = "\n\n".join([
    _load_prompt("system_prompt.md"),
    _load_prompt("analysis_rules.md"),
    _load_prompt("question_rules.md"),
    "Always respond with valid JSON only. No markdown, no explanation outside JSON.",
])

SCENE_ANALYSIS_SYSTEM_PROMPT = """You are a children's story analyst for English education.
Analyze story texts and extract structured story information.
Always respond with valid JSON only. No markdown, no explanation outside JSON."""

QUESTION_TYPES = [
    ("patternPractice", "Pattern Practice"),
    ("recall", "Recall"),
    ("inference", "Inference"),
    ("transfer", "Transfer"),
    ("reflection", "Reflection"),
]

BOOK_LEVEL_MAP = {
    "Lv 1": "Pre-A1",
    "Lv 2": "A1",
    "Lv 3": "A2",
    "Lv 4": "B1",
}

CEFR_SENTENCE_STRUCTURE = {
    "Pre-A1": (
        "Use only words, phrases, or 2–3 word expressions. "
        "Allowed structures: noun phrases, adjective+noun, basic verbs, some be-verb forms. "
        "No complex sentences. Keep everything as short and simple as possible."
    ),
    "A1": (
        "Use short, simple sentences (SVO structure). "
        "Allowed structures: present tense, be verbs, can, there is/are, imperatives, basic question forms (Do/Does/Is/Are). "
        "Avoid past tense, conjunctions, or any complex grammar."
    ),
    "A2": (
        "Use simple sentences and begin introducing basic compound sentences. "
        "Allowed structures: past tense (simple), be going to (future), because, and, but, when, basic if-clauses. "
        "Avoid relative clauses, present perfect, or advanced grammar."
    ),
    "B1": (
        "Use compound and complex sentences. "
        "Allowed structures: relative clauses (who/which/that), present perfect, basic passives, first conditionals, "
        "a variety of conjunctions (although, unless, while). "
        "Avoid second conditionals, past perfect, or C1+ structures."
    ),
}


def analyze_story(api_key, api_provider, story_text):
    prompt = f"""Analyze the following children's story.

Story Text:
{story_text}

Return a JSON object with this exact structure:
{{
  "summary": "Summarize the story in exactly 3 sentences.",
  "storyElements": {{
    "characters": "main characters and their roles",
    "setting": "when and where the story takes place",
    "conflict": "the main problem or challenge",
    "resolution": "how the conflict is resolved",
    "moral": "the lesson or theme"
  }}
}}

Return valid JSON only."""

    if api_provider == "OpenAI":
        client = openai.OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SCENE_ANALYSIS_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        return json.loads(completion.choices[0].message.content)
    else:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SCENE_ANALYSIS_SYSTEM_PROMPT}\n\n{prompt}",
            config=genai_types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.3,
            ),
        )
        return json.loads(response.text)


def build_prompt(story_text, story_analysis, user_patterns, keywords, story_words, selected_types, cefr_level="B1"):
    sentence_structure_guide = CEFR_SENTENCE_STRUCTURE.get(cefr_level, CEFR_SENTENCE_STRUCTURE["B1"])
    summary = story_analysis.get("summary", "")
    elements = story_analysis.get("storyElements", {})
    story_context = (
        f"Summary: {summary}\n"
        f"Characters: {elements.get('characters', '')}\n"
        f"Setting: {elements.get('setting', '')}\n"
        f"Conflict: {elements.get('conflict', '')}\n"
        f"Resolution: {elements.get('resolution', '')}\n"
        f"Moral: {elements.get('moral', '')}"
    )

    user_input = (
        _load_prompt("user_prompt_template.md")
        .replace("<<CEFR_LEVEL>>", cefr_level)
        .replace("<<SENTENCE_STRUCTURE_GUIDE>>", sentence_structure_guide)
        .replace("<<STORY_TEXT>>", story_text)
        .replace("<<STORY_CONTEXT>>", story_context)
        .replace("<<USER_PATTERNS>>", user_patterns)
        .replace("<<KEYWORDS>>", keywords)
        .replace("<<STORY_WORDS>>", story_words)
        .replace("<<SELECTED_TYPES>>", ", ".join(selected_types))
    )

    output_section = _load_prompt("output_format.md").replace("<<CEFR_LEVEL>>", cefr_level)

    return f"{user_input}\n\n{output_section}\n"


def call_api(api_key, api_provider, prompt):
    if api_provider == "OpenAI":
        client = openai.OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
        )
        return completion.choices[0].message.content
    else:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\n\n{prompt}",
            config=genai_types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.7,
            ),
        )
        return response.text


ALT_TEXT_CEFR_CAP = {"Pre-A1": "A1", "A1": "A1", "A2": "A2", "B1": "A2"}


def generate_alt_text(api_key, api_provider, image_bytes, mime_type, scene_key, story_text, cefr_level="B1"):
    effective_level = ALT_TEXT_CEFR_CAP.get(cefr_level, "A2")
    prompt = (
        f"This is scene {scene_key} from a children's English storybook.\n"
        f"Story context: {story_text[:300]}\n\n"
        f"Describe what is happening in this scene in 1 short English sentence. "
        f"Include the character's name (if visible), action, emotion, and key objects. "
        f"Use only simple vocabulary at or below CEFR {effective_level} level — "
        f"prefer words already used in the story context above. "
        f"Never use C1-level words. "
        f"Example format: 'Judy standing on a tennis court, holding a racket and looking nervous.' "
        f"Output the description only. No extra text."
    )

    if api_provider == "OpenAI":
        client = openai.OpenAI(api_key=api_key)
        b64 = base64.b64encode(image_bytes).decode()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{b64}"}},
                    {"type": "text", "text": prompt},
                ],
            }],
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    else:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                genai_types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
                prompt,
            ],
        )
        return response.text.strip()


def regenerate_question(api_key, api_provider, story_text, keywords, story_words, question_type, original_q, instruction, cefr_level="B1"):
    type_label = dict(QUESTION_TYPES).get(question_type, question_type)
    sentence_structure_guide = CEFR_SENTENCE_STRUCTURE.get(cefr_level, CEFR_SENTENCE_STRUCTURE["B1"])
    prompt = f"""Story Text:
{story_text}

Book Level: CEFR {cefr_level} — vocabulary must not exceed this level.
Sentence Structure Guide: {sentence_structure_guide}
Keywords (may be used in questions): {keywords}
Story Words (must NOT be used in questions): {story_words}

The following question was generated for the "{type_label}" category:
{json.dumps(original_q, ensure_ascii=False, indent=2)}

Refinement instruction: {instruction}

Regenerate ONLY this single question following the instruction.
Return a JSON object with exactly the same structure as the original.
Valid JSON only. No markdown, no explanation outside JSON."""

    raw = call_api(api_key, api_provider, prompt)
    return json.loads(raw)


def build_excel(result, story_analysis, alt_texts):
    # Questions sheet
    rows = []
    for type_key, type_label in QUESTION_TYPES:
        for q in result.get("questions", {}).get(type_key, []):
            scene = q.get("relatedScene", "")
            target_answer = q.get("targetAnswer") or ", ".join(q.get("targetAnswers", []))
            rows.append({
                "Type": type_label,
                "Question": q.get("question", ""),
                "Target Answer": target_answer,
                "Related Scene": scene,
                "Alt Text": alt_texts.get(scene, ""),
                "Acceptable Criteria": q.get("acceptableCriteria", ""),
            })
    df_q = pd.DataFrame(rows, columns=["Type", "Question", "Target Answer", "Related Scene", "Alt Text", "Acceptable Criteria"])

    # Story Info sheet
    persona = result.get("characterPersona", {})
    elements = story_analysis.get("storyElements", {})
    opening = persona.get("openingLine", "")
    if isinstance(opening, list):
        opening = " ".join(opening)
    info_rows = [
        {"Field": "Summary", "Value": story_analysis.get("summary", "")},
        {"Field": "Characters", "Value": elements.get("characters", "")},
        {"Field": "Setting", "Value": elements.get("setting", "")},
        {"Field": "Conflict", "Value": elements.get("conflict", "")},
        {"Field": "Resolution", "Value": elements.get("resolution", "")},
        {"Field": "Moral", "Value": elements.get("moral", "")},
        {"Field": "Core Message", "Value": persona.get("coreMessage", "")},
        {"Field": "Opening Line", "Value": opening},
    ]
    df_info = pd.DataFrame(info_rows)

    # Patterns sheet
    df_patterns = pd.DataFrame({"Pattern": result.get("patterns", [])})

    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        df_q.to_excel(writer, index=False, sheet_name="Questions")
        df_info.to_excel(writer, index=False, sheet_name="Story Info")
        df_patterns.to_excel(writer, index=False, sheet_name="Patterns")
    return buf.getvalue()


def render_question(q, idx, question_type, api_key, api_provider, story_text, keywords, story_words, alt_texts, cefr_level="B1"):
    with st.container(border=True):
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            st.markdown(f"**{idx + 1}**")
        with col2:
            st.markdown(f"**{q['question']}**")

            scene = q.get("relatedScene", "")
            alt = alt_texts.get(scene, "")
            if alt:
                st.caption(f"{scene} · {alt}")
            else:
                st.caption(scene)

            if q.get("targetAnswer"):
                st.markdown("**Target Answer**")
                st.success(q["targetAnswer"])
            if q.get("targetAnswers"):
                st.markdown("**Target Answers**")
                for a in q["targetAnswers"]:
                    st.success(f"• {a}")

            st.markdown("**채점 기준**")
            st.info(q.get("acceptableCriteria", ""))

            col_input, col_btn = st.columns([0.82, 0.18])
            with col_input:
                instruction = st.text_input(
                    "수정 요청",
                    key=f"refine_{question_type}_{idx}",
                    placeholder="예: 난이도를 낮춰줘 / 더 구체적인 상황을 넣어줘",
                    label_visibility="collapsed",
                )
            with col_btn:
                regenerate_clicked = st.button(
                    "재생성", key=f"btn_{question_type}_{idx}", use_container_width=True
                )

        if regenerate_clicked:
            if not instruction.strip():
                st.warning("수정 요청을 입력해주세요.")
            else:
                with st.spinner("재생성 중..."):
                    try:
                        new_q = regenerate_question(
                            api_key, api_provider, story_text, keywords, story_words,
                            question_type, q, instruction, cefr_level,
                        )
                        st.session_state["result"]["questions"][question_type][idx] = new_q
                        st.rerun()
                    except Exception as e:
                        st.error(f"오류: {e}")


CACHE_KEY = "sgq_cache_v1"
CACHE_TTL = 5 * 24 * 3600  # 5일 (초 단위)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Story Question Generator", layout="wide")
st.title("Story Question Generator")
st.caption("스토리를 분석하고 페르소나와 질문을 생성합니다.")

# ── 로컬 스토리지 초기화 및 캐시 복원 ────────────────────────────────────────
_ls = LocalStorage()
_raw_cache = _ls.getItem(CACHE_KEY)
_cache_data = None
_cache_age_days = None

if _raw_cache:
    try:
        _parsed = json.loads(_raw_cache)
        _age = time.time() - _parsed.get("saved_at", 0)
        if _age < CACHE_TTL:
            _cache_data = _parsed
            _cache_age_days = _age / 86400
    except Exception:
        pass

if _cache_data and "story_analysis" not in st.session_state:
    for _k in ["story_analysis", "story_text_saved", "result", "alt_texts"]:
        if _cache_data.get(_k):
            st.session_state[_k] = _cache_data[_k]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.subheader("도서 레벨")
    book_level = st.selectbox(
        "도서 레벨",
        options=list(BOOK_LEVEL_MAP.keys()),
        format_func=lambda lv: f"{lv} (CEFR {BOOK_LEVEL_MAP[lv]})",
        label_visibility="collapsed",
    )
    cefr_level = BOOK_LEVEL_MAP[book_level]

    st.subheader("API 설정")
    api_provider = st.radio("Provider", ["OpenAI", "Gemini"], horizontal=True)
    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="sk-... (OpenAI)" if api_provider == "OpenAI" else "AI... (Gemini)",
    )

    st.subheader("스토리 전문")
    story_text = st.text_area(
        "스토리",
        placeholder="SC01 — Judy loved tennis...\nSC02 — One day, Judy found...",
        height=180,
        label_visibility="collapsed",
    )

    st.subheader("장면 이미지 (Alt 텍스트 생성용)")
    st.caption("업로드 순서가 SC01, SC02, ... 순으로 매핑됩니다.")
    uploaded_images = st.file_uploader(
        "이미지",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    st.subheader("핵심 패턴 (Pattern Practice용)")
    user_patterns = st.text_area(
        "패턴",
        placeholder="not {adj} anymore",
        height=100,
        label_visibility="collapsed",
    )

    st.subheader("키워드")
    keywords = st.text_area(
        "키워드",
        placeholder="tennis, racket, practice, confidence, ...",
        height=70,
        label_visibility="collapsed",
    )

    st.subheader("Story Words")
    story_words = st.text_area(
        "스토리 단어",
        placeholder="whispers, shimmering, silver, ...",
        height=70,
        label_visibility="collapsed",
    )

    st.subheader("생성할 질문 유형")
    selected_types = []
    for key, label in QUESTION_TYPES:
        if st.checkbox(label, value=True, key=key):
            selected_types.append(key)

    st.divider()
    analyze_clicked = st.button("① 스토리 분석하기", type="primary", use_container_width=True)

    if _cache_data:
        _remaining = 5 - _cache_age_days
        st.caption(f"💾 {_cache_age_days:.1f}일 전 저장 · 만료까지 {_remaining:.1f}일")
        if st.button("캐시 삭제", use_container_width=True):
            _ls.deleteItem(CACHE_KEY)
            for _k in ["story_analysis", "story_text_saved", "result", "alt_texts"]:
                st.session_state.pop(_k, None)
            st.rerun()

# ── ① 스토리 분석 ─────────────────────────────────────────────────────────────
if analyze_clicked:
    if not story_text.strip():
        st.error("스토리 텍스트를 입력해주세요.")
    elif not api_key.strip():
        st.error("API 키를 입력해주세요.")
    else:
        if uploaded_images:
            alt_texts_new = {}
            progress = st.progress(0, text="장면 Alt 텍스트 생성 중...")
            try:
                for i, img_file in enumerate(uploaded_images):
                    scene_key = f"SC{i + 1:02d}"
                    img_file.seek(0)
                    image_bytes = img_file.read()
                    mime_type = img_file.type or "image/jpeg"
                    alt_texts_new[scene_key] = generate_alt_text(
                        api_key, api_provider, image_bytes, mime_type, scene_key, story_text, cefr_level
                    )
                    progress.progress((i + 1) / len(uploaded_images), text=f"{scene_key} 완료")
                st.session_state["alt_texts"] = alt_texts_new
            except Exception as e:
                st.error(f"Alt 생성 오류: {e}")
            finally:
                progress.empty()

        with st.spinner("스토리를 분석하고 있습니다..."):
            try:
                analysis = analyze_story(api_key, api_provider, story_text)
                st.session_state["story_analysis"] = analysis
                st.session_state["story_text_saved"] = story_text
                st.session_state.pop("result", None)
                _ls.setItem(CACHE_KEY, json.dumps({
                    "saved_at": time.time(),
                    "story_analysis": analysis,
                    "story_text_saved": story_text,
                    "alt_texts": st.session_state.get("alt_texts"),
                    "result": None,
                }, ensure_ascii=False))
            except Exception as e:
                st.error(f"분석 오류: {e}")

# ── Story Analysis 표시 + ② 페르소나 및 질문 생성 ─────────────────────────────
if "story_analysis" in st.session_state:
    analysis = st.session_state["story_analysis"]
    elements = analysis.get("storyElements", {})

    with st.expander("① Story Analysis", expanded=True):
        st.markdown(f"**Summary**  \n{analysis.get('summary', '')}")
        st.divider()
        el_col1, el_col2 = st.columns(2)
        with el_col1:
            st.markdown(f"**Characters** {elements.get('characters', '')}")
            st.markdown(f"**Setting** {elements.get('setting', '')}")
            st.markdown(f"**Conflict** {elements.get('conflict', '')}")
        with el_col2:
            st.markdown(f"**Resolution** {elements.get('resolution', '')}")
            st.markdown(f"**Moral** {elements.get('moral', '')}")

    st.divider()
    generate_clicked = st.button("② 페르소나 및 질문 생성하기", type="primary")

    if generate_clicked:
        if not selected_types:
            st.error("질문 유형을 하나 이상 선택해주세요.")
        else:
            with st.spinner("AI가 페르소나 및 질문 풀을 생성하고 있습니다..."):
                try:
                    prompt = build_prompt(
                        st.session_state["story_text_saved"],
                        st.session_state["story_analysis"],
                        user_patterns, keywords, story_words, selected_types, cefr_level,
                    )
                    raw = call_api(api_key, api_provider, prompt)
                    result_data = json.loads(raw)
                    st.session_state["result"] = result_data
                    _ls.setItem(CACHE_KEY, json.dumps({
                        "saved_at": time.time(),
                        "story_analysis": st.session_state["story_analysis"],
                        "story_text_saved": st.session_state["story_text_saved"],
                        "alt_texts": st.session_state.get("alt_texts"),
                        "result": result_data,
                    }, ensure_ascii=False))
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")

# ── Alt 텍스트 미리보기 ────────────────────────────────────────────────────────
if "alt_texts" in st.session_state and st.session_state["alt_texts"]:
    with st.expander("생성된 Alt 텍스트", expanded=False):
        for scene_key, alt in sorted(st.session_state["alt_texts"].items()):
            st.markdown(f"**{scene_key}** {alt}")

# ── ② 결과 출력 ───────────────────────────────────────────────────────────────
if "result" in st.session_state:
    result = st.session_state["result"]
    persona = result.get("characterPersona", {})
    questions = result.get("questions", {})
    alt_texts = st.session_state.get("alt_texts", {})
    story_text_saved = st.session_state.get("story_text_saved", "")
    story_analysis = st.session_state.get("story_analysis", {})

    with st.expander("Character Persona", expanded=True):
        c1, c2, c3 = st.columns(3)
        c1.metric("Name", persona.get("name", "-"))
        c2.metric("Age", persona.get("age", "-"))
        c3.metric("Gender", persona.get("gender", "-"))
        st.markdown(f"**Personality** {persona.get('personality', '')}")
        st.markdown(f"**Core Message** {persona.get('coreMessage', '')}")
        opening = persona.get("openingLine", "")
        if isinstance(opening, list):
            opening = " ".join(opening)
        st.markdown(f"**Opening Line** *\"{opening}\"*")

    patterns_list = result.get("patterns", [])
    if patterns_list:
        with st.expander("Patterns", expanded=False):
            for p in patterns_list:
                st.markdown(f"- {p}")

    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        st.download_button(
            "Excel 다운로드",
            data=build_excel(result, story_analysis, alt_texts),
            file_name="questions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
    with dl_col2:
        st.download_button(
            "JSON 다운로드",
            data=json.dumps(result, ensure_ascii=False, indent=2),
            file_name="result.json",
            mime="application/json",
            use_container_width=True,
        )

    active_types = [(k, l) for k, l in QUESTION_TYPES if k in questions and k in selected_types]
    if active_types:
        tabs = st.tabs([label for _, label in active_types])
        for tab, (key, _) in zip(tabs, active_types):
            with tab:
                for i, q in enumerate(questions.get(key, [])):
                    render_question(
                        q, i, key, api_key, api_provider,
                        story_text_saved, keywords, story_words, alt_texts, cefr_level,
                    )
