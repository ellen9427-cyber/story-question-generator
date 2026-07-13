import base64
import io
import json
import streamlit as st
import openai
from google import genai
from google.genai import types as genai_types
import pandas as pd

SYSTEM_PROMPT = """You are an English learning content designer for children aged 9-11.
Your job is to generate educational question pools based on a given story.
Always respond with valid JSON only. No markdown, no explanation outside JSON."""

QUESTION_TYPES = [
    ("patternPractice", "Pattern Practice"),
    ("recall", "Recall"),
    ("inference", "Inference"),
    ("transfer", "Transfer"),
    ("reflection", "Reflection"),
]

BOOK_LEVEL_MAP = {
    "Lv 1": "A2",
    "Lv 2": "B1",
    "Lv 3": "B2",
    "Lv 4": "C1",
}


def build_prompt(story_text, patterns, keywords, story_words, selected_types, cefr_level="B1"):
    return f"""
Book Level: {cefr_level} (maximum CEFR vocabulary level allowed)

Story Text:
{story_text}

Core Patterns for Pattern Practice:
{patterns}

Keywords (tutor may use these in questions):
{keywords}

Story Words (tutor must NOT use these words in questions — use simpler or different vocabulary instead):
{story_words}

Generate the following question types: {", ".join(selected_types)}

Return a JSON object with this exact structure:
{{
  "characterPersona": {{
    "name": "character name (derived from the story)",
    "age": "age range (derived from the story)",
    "gender": "gender (derived from the story)",
    "personality": "personality description in English (derived from the story)",
    "coreMessage": "core message in English (derived from the story)",
    "openingLine": "opening line in English (derived from the story)"
  }},
  "questions": {{
    "patternPractice": [
      {{
        "question": "Say it with me: '[pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "exact sentence to repeat",
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "recall": [
      {{
        "question": "factual question about the story (from character's POV using 'I')",
        "relatedScene": "SC##",
        "targetAnswers": ["answer variant 1", "answer variant 2"],
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "inference": [
      {{
        "question": "inference question (from character's POV using 'I')",
        "relatedScene": "SC##",
        "targetAnswers": ["answer variant 1", "answer variant 2"],
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "transfer": [
      {{
        "question": "question connecting story to learner's own life",
        "relatedScene": "SC##",
        "targetAnswers": ["example answer 1", "example answer 2"],
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "reflection": [
      {{
        "question": "open-ended reflection question about the story",
        "relatedScene": "SC##",
        "targetAnswers": ["example answer 1", "example answer 2"],
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ]
  }}
}}

Rules:
- Generate exactly 5 questions for each selected type (omit unselected types from the JSON).
- All questions within each type must be ordered by scene (SC01 before SC02, etc.), following the chronological flow of the story.
- patternPractice: generate 5 different sentences for the learner to repeat. Each sentence must be unique — do not repeat the same sentence. The sentences do not need to be exact quotes from the story; they should be natural applications or variations of the core patterns within the story's context and flow. The acceptableCriteria for each patternPractice question must follow this format: "발음을 명확하게 하지 않아도 '[해당 문장의 핵심 구조 또는 패턴]'를 포함해서 말하면 정답으로 인정한다." — replace the bracketed part with the specific grammatical structure or key phrase of that sentence (e.g., 'not + 형용사 구조', 'I used to + 동사 구조').
- recall: questions must be answerable directly from the story text only. The acceptableCriteria for each recall question must specify the exact keyword(s) or key content that must appear in the answer — not a generic statement. Format: "'[keyword]'를 포함하여 말하면 정답으로 인정한다." or "[핵심 내용]이 드러나게 말하면 정답으로 인정한다." Include any important constraints (e.g., verb synonyms allowed, specific word variants accepted).
- inference: questions require reading between the lines of the story. The acceptableCriteria for each inference question must specify the exact keyword(s) or key meaning that must appear in the answer — not a generic statement. Format: "'[keyword]' 또는 '[keyword]'를 포함하여 [핵심 의미]가 드러나면 정답으로 인정한다." Include semantic variants where appropriate (e.g., synonyms or paraphrases that convey the same meaning).
- transfer: questions ask the learner about their own experience or opinion, linked to story themes. The acceptableCriteria for each transfer question must be specific to that question — not a generic statement. Specify the type of response that counts as correct: relevant keywords, emotional vocabulary, categories of examples (e.g., sports/activities/situations), or meaningful content the learner's answer must include. Format: "[keyword 또는 카테고리 예시]를 포함하거나 [핵심 의미]가 드러나면 정답으로 인정한다."
- reflection: open-ended questions asking for evaluation or advice about story events. The acceptableCriteria for each reflection question must be specific to that question — not a generic statement. Follow these patterns based on question type:
  * For opinion/judgment questions (Do you think...? Would you...?): "Yes 또는 No라고 답한 뒤, [핵심 내용]을 타당한 근거와 함께 설명하면 정답으로 인정한다. [keyword1], [keyword2] 등의 의미를 포함하면 더 적절한 답변으로 본다."
  * For questions asking what the learner learned or felt from the story: "Judy 이야기의 메시지와 연결하여 [핵심 주제: 예 - 자신감, 연습, 자기 힘] 등의 의미가 드러나면 정답으로 인정한다."
  * For advice-giving questions (What would you say to...?): "경기 결과와 상관없이 [노력/자신감/연습/자기 힘] 등을 인정하거나 격려하는 내용이면 정답으로 인정한다."
  Always specify (1) expected response format, (2) acceptable keywords or meanings, and (3) what makes an answer especially strong, if applicable.
- Questions should be from the character's first-person perspective ("What sport did I love?").
- VOCABULARY LEVEL CONSTRAINT: The book level is CEFR {cefr_level}. All vocabulary used in questions and target answers must not exceed CEFR {cefr_level}. Do not use any word more complex than CEFR {cefr_level}. This applies to every word in every question, answer, and the acceptableCriteria (Korean text in acceptableCriteria is exempt from CEFR rules).
- Match the vocabulary and sentence complexity of the questions to the level of the story text. Do not use words or structures more advanced than those found in the story.
- The tutor's question wording may include provided Keywords, but must NOT use Story Words. Replace story words with simpler or alternative vocabulary that conveys the same meaning.
- Acceptable criteria must be written in Korean.
- All questions and answers must be in English.
- characterPersona fields (name, age, gender, personality, coreMessage, openingLine) must ALL be written in English, derived from the story text.
"""


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


ALT_TEXT_CEFR_CAP = {"A2": "A2", "B1": "B1", "B2": "B2", "C1": "B2"}


def generate_alt_text(api_key, api_provider, image_bytes, mime_type, scene_key, story_text, cefr_level="B1"):
    effective_level = ALT_TEXT_CEFR_CAP.get(cefr_level, "B1")
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
    prompt = f"""Story Text:
{story_text}

Book Level: CEFR {cefr_level} — all vocabulary in questions and answers must not exceed this level.
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


def build_excel(result, alt_texts):
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
    df = pd.DataFrame(rows, columns=["Type", "Question", "Target Answer", "Related Scene", "Alt Text", "Acceptable Criteria"])
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Questions")
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


# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Story Question Generator", layout="wide")
st.title("Story Question Generator")
st.caption("스토리 텍스트와 패턴을 입력하면 질문 풀을 자동 생성합니다.")

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
    patterns = st.text_area(
        "패턴",
        placeholder="You're not worried anymore.\nYou're not weak anymore.\n...",
        height=100,
        label_visibility="collapsed",
    )

    st.subheader("키워드 (질문에 사용 가능)")
    keywords = st.text_area(
        "키워드",
        placeholder="tennis, racket, practice, confidence, ...",
        height=70,
        label_visibility="collapsed",
    )

    st.subheader("Story Words (질문에 사용 금지)")
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

    generate = st.button("페르소나 및 질문 풀 생성", type="primary", use_container_width=True)

# ── 페르소나 및 질문 풀 생성 (+ alt 텍스트 통합) ─────────────────────────────
if generate:
    if not story_text.strip():
        st.error("스토리 텍스트를 입력해주세요.")
    elif not api_key.strip():
        st.error("API 키를 입력해주세요.")
    elif not selected_types:
        st.error("질문 유형을 하나 이상 선택해주세요.")
    else:
        if uploaded_images:
            alt_texts = {}
            progress = st.progress(0, text="장면 Alt 텍스트 생성 중...")
            try:
                for i, img_file in enumerate(uploaded_images):
                    scene_key = f"SC{i + 1:02d}"
                    img_file.seek(0)
                    image_bytes = img_file.read()
                    mime_type = img_file.type or "image/jpeg"
                    alt_texts[scene_key] = generate_alt_text(
                        api_key, api_provider, image_bytes, mime_type, scene_key, story_text, cefr_level
                    )
                    progress.progress((i + 1) / len(uploaded_images), text=f"{scene_key} 완료")
                st.session_state["alt_texts"] = alt_texts
            except Exception as e:
                st.error(f"Alt 생성 오류: {e}")
            finally:
                progress.empty()

        with st.spinner("AI가 페르소나 및 질문 풀을 생성하고 있습니다..."):
            try:
                prompt = build_prompt(story_text, patterns, keywords, story_words, selected_types, cefr_level)
                raw = call_api(api_key, api_provider, prompt)
                st.session_state["result"] = json.loads(raw)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

# Alt 텍스트 결과 표시
if "alt_texts" in st.session_state and st.session_state["alt_texts"]:
    with st.expander("생성된 Alt 텍스트", expanded=False):
        for scene_key, alt in sorted(st.session_state["alt_texts"].items()):
            st.markdown(f"**{scene_key}** {alt}")

if "result" in st.session_state:
    result = st.session_state["result"]
    persona = result.get("characterPersona", {})
    questions = result.get("questions", {})
    alt_texts = st.session_state.get("alt_texts", {})

    # Character Persona
    with st.expander("Character Persona", expanded=True):
        c1, c2, c3 = st.columns(3)
        c1.metric("Name", persona.get("name", "-"))
        c2.metric("Age", persona.get("age", "-"))
        c3.metric("Gender", persona.get("gender", "-"))
        st.markdown(f"**Personality** {persona.get('personality', '')}")
        st.markdown(f"**Core Message** {persona.get('coreMessage', '')}")
        st.markdown(f"**Opening Line** *\"{persona.get('openingLine', '')}\"*")

        dl_col1, dl_col2 = st.columns(2)
        with dl_col1:
            st.download_button(
                "Excel 다운로드",
                data=build_excel(result, alt_texts),
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

    # Question Tabs
    active_types = [(k, l) for k, l in QUESTION_TYPES if k in questions and k in selected_types]
    if active_types:
        tabs = st.tabs([label for _, label in active_types])
        for tab, (key, _) in zip(tabs, active_types):
            with tab:
                for i, q in enumerate(questions.get(key, [])):
                    render_question(
                        q, i, key, api_key, api_provider,
                        story_text, keywords, story_words, alt_texts, cefr_level,
                    )
