import base64
import io
import json
import streamlit as st
import openai
from google import genai
from google.genai import types as genai_types
import pandas as pd

SYSTEM_PROMPT = """You are an English learning content designer for children.
Your job is to generate educational question pools based on a given story.
Always respond with valid JSON only. No markdown, no explanation outside JSON."""

SCENE_ANALYSIS_SYSTEM_PROMPT = """You are a children's story analyst for English education.
Analyze story texts and extract structured scene-by-scene information.
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


def analyze_scenes(api_key, api_provider, story_text):
    prompt = f"""Analyze the following children's story and extract structured information for each scene.

Story Text:
{story_text}

Return a JSON object with this exact structure:
{{
  "scenes": [
    {{
      "scene": "SC01",
      "event": "What physically happens in this scene (1–2 sentences)",
      "trigger": "What causes or leads up to this event (1–2 sentences)",
      "result": "The outcome or consequence of this scene (1–2 sentences)",
      "emotional_response": "How the main character feels or reacts (1–2 sentences)",
      "include": true
    }}
  ]
}}

Rules:
- Detect every scene marker (SC01, SC02, ...) present in the story text, in order.
- Write all field values in English.
- Set "include" to true for all scenes by default.
- Return valid JSON only."""

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
        return json.loads(completion.choices[0].message.content)["scenes"]
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
        data = json.loads(response.text)
        return data["scenes"] if isinstance(data, dict) and "scenes" in data else data


def build_prompt(scene_summaries, patterns, keywords, story_words, selected_types, cefr_level="B1"):
    sentence_structure_guide = CEFR_SENTENCE_STRUCTURE.get(cefr_level, CEFR_SENTENCE_STRUCTURE["B1"])
    return f"""
Book Level: {cefr_level} (maximum CEFR vocabulary level allowed)

CEFR {cefr_level} Sentence Structure Guide:
{sentence_structure_guide}
Apply this sentence structure to ALL questions and target answers.

Scene-by-Scene Story Summary (basis for question generation):
{scene_summaries}

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
    "age": "exact age as a single number derived from the story (e.g., \\"10 years old\\" or \\"11 years old\\")",
    "gender": "gender (derived from the story)",
    "personality": "personality description in English (derived from the story)",
    "coreMessage": "core message in English (derived from the story)",
    "openingLine": "a single continuous tutor script that naturally flows through: (1) a warm greeting, (2) the character's self-introduction by name, (3) one sentence capturing the story's core theme or personal message (e.g., I am strong inside.), and (4) a simple preference question with no right or wrong answer (e.g., What sport do you like?). Write it as natural connected speech, not as separate labeled parts."
  }},
  "questions": {{
    "patternPractice": [
      {{
        "question": "Say it with me: 'I [pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "exact sentence starting with I for the student to repeat (e.g., I am not scared anymore.)",
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "recall": [
      {{
        "question": "factual question about the story (tutor asks from character's POV using 'I')",
        "relatedScene": "SC##",
        "targetAnswers": ["You + answer variant 1", "You + answer variant 2"],
        "acceptableCriteria": "grading criterion in Korean"
      }}
    ],
    "inference": [
      {{
        "question": "inference question (tutor asks from character's POV using 'I')",
        "relatedScene": "SC##",
        "targetAnswers": ["You + answer variant 1", "You + answer variant 2"],
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
- Only reference scenes that appear in the Scene-by-Scene Story Summary above. Do not invent scenes not listed there.
- patternPractice: generate 5 different sentences for the learner to repeat. Each sentence must be unique — do not repeat the same sentence. The sentences do not need to be exact quotes from the story; they should be natural applications or variations of the core patterns within the story's context and flow. Each question must follow the format: "Say it with me: 'I [pattern sentence]'" — the pattern sentence must use "I" as the subject (tutor speaking as the character). The targetAnswer must also start with "I" (the student repeats the sentence using "I"). The acceptableCriteria for each patternPractice question must follow this format: "발음을 명확하게 하지 않아도 '[해당 문장의 핵심 구조 또는 패턴]'를 포함해서 말하면 정답으로 인정한다." — replace the bracketed part with the specific grammatical structure or key phrase of that sentence (e.g., 'not + 형용사 구조', 'I used to + 동사 구조').
- recall: questions must be answerable directly from the story summary only, and must have a single, specific, unambiguous answer explicitly stated in the story. Do NOT generate questions where the answer would be vague or non-specific — for example, avoid questions about uncounted quantities (e.g., "How much gold?" → "much gold" is not an acceptable answer), or questions where the story only implies a general amount rather than a precise fact. Stick to questions whose answers are concrete: a specific name, place, action, object, or clearly stated fact. The acceptableCriteria for each recall question must specify the exact keyword(s) or key content that must appear in the answer — not a generic statement. Format: "'[keyword]'를 포함하여 말하면 정답으로 인정한다." or "[핵심 내용]이 드러나게 말하면 정답으로 인정한다." Include any important constraints (e.g., verb synonyms allowed, specific word variants accepted).
- inference: questions require reading between the lines of the story, but the answer must still be grounded in the story summary — do NOT generate questions that cannot be answered based on what is described in the scenes (e.g., no speculative "what do you think would happen if..." questions). Write each question as a single direct question only — do NOT add any setup or context sentences before it (e.g., do NOT write "I had heavy gold. I saw a man on a horse. Why did I want to ride a horse?" — just write "Why did I want to ride a horse?"). Adding context sentences before the question gives away the answer and defeats the purpose of inference. The acceptableCriteria for each inference question must specify the exact keyword(s) or key meaning that must appear in the answer — not a generic statement. Format: "'[keyword]' 또는 '[keyword]'를 포함하여 [핵심 의미]가 드러나면 정답으로 인정한다." Include semantic variants where appropriate (e.g., synonyms or paraphrases that convey the same meaning).
- transfer: questions ask the learner about their own experience or opinion, linked to story themes. The acceptableCriteria for each transfer question must be specific to that question — not a generic statement. Specify the type of response that counts as correct: relevant keywords, emotional vocabulary, categories of examples (e.g., sports/activities/situations), or meaningful content the learner's answer must include. Format: "[keyword 또는 카테고리 예시]를 포함하거나 [핵심 의미]가 드러나면 정답으로 인정한다."
- reflection: open-ended questions asking for evaluation or advice about story events. The acceptableCriteria for each reflection question must be specific to that question — not a generic statement. Follow these patterns based on question type:
  * For opinion/judgment questions (Do you think...? Would you...?): "Yes 또는 No라고 답한 뒤, [핵심 내용]을 타당한 근거와 함께 설명하면 정답으로 인정한다. [keyword1], [keyword2] 등의 의미를 포함하면 더 적절한 답변으로 본다."
  * For questions asking what the learner learned or felt from the story: "[캐릭터] 이야기의 메시지와 연결하여 [핵심 주제: 예 - 자신감, 연습, 자기 힘] 등의 의미가 드러나면 정답으로 인정한다."
  * For advice-giving questions (What would you say to...?): "결과와 상관없이 [노력/자신감/연습/자기 힘] 등을 인정하거나 격려하는 내용이면 정답으로 인정한다."
  Always specify (1) expected response format, (2) acceptable keywords or meanings, and (3) what makes an answer especially strong, if applicable.
- Questions must be asked from the tutor's (character's) first-person perspective using "I" (e.g., "What sport did I love?").
- patternPractice targetAnswer must use "I" as the subject (student repeats the pattern sentence as the character).
- For recall and inference, all targetAnswers must use "You" as the subject — the learner answers about the character (e.g., "You loved tennis." not "I loved tennis.").
- For transfer and reflection, where the learner talks about themselves, answers may use "I" naturally (e.g., "I feel happy when I play soccer.").
- VOCABULARY LEVEL CONSTRAINT: The book level is CEFR {cefr_level}. All vocabulary used in questions and target answers must not exceed CEFR {cefr_level}. Do not use any word more complex than CEFR {cefr_level}. This applies to every word in every question, answer, and the acceptableCriteria (Korean text in acceptableCriteria is exempt from CEFR rules).
- SENTENCE STRUCTURE CONSTRAINT: Apply the CEFR {cefr_level} sentence structure guide above to all questions and target answers. Do not use grammar or sentence patterns more complex than what is specified for this level.
- The tutor's question wording may include provided Keywords, but must NOT use Story Words. Replace story words with simpler or alternative vocabulary that conveys the same meaning.
- Acceptable criteria must be written in Korean.
- All questions and answers must be in English.
- characterPersona fields (name, age, gender, personality, coreMessage, openingLine) must ALL be written in English, derived from the story.
- The openingLine field must be a single string of continuous natural speech (not an array, not labeled sections).
- age must be a single exact age (e.g., "10 years old"), not a range.
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


def regenerate_question(api_key, api_provider, scene_summaries, keywords, story_words, question_type, original_q, instruction, cefr_level="B1"):
    type_label = dict(QUESTION_TYPES).get(question_type, question_type)
    sentence_structure_guide = CEFR_SENTENCE_STRUCTURE.get(cefr_level, CEFR_SENTENCE_STRUCTURE["B1"])
    prompt = f"""Scene-by-Scene Story Summary:
{scene_summaries}

Book Level: CEFR {cefr_level} — all vocabulary in questions and answers must not exceed this level.
CEFR {cefr_level} Sentence Structure Guide: {sentence_structure_guide}
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


def render_question(q, idx, question_type, api_key, api_provider, scene_summaries, keywords, story_words, alt_texts, cefr_level="B1"):
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
                            api_key, api_provider, scene_summaries, keywords, story_words,
                            question_type, q, instruction, cefr_level,
                        )
                        st.session_state["result"]["questions"][question_type][idx] = new_q
                        st.rerun()
                    except Exception as e:
                        st.error(f"오류: {e}")


# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Story Question Generator", layout="wide")
st.title("Story Question Generator")
st.caption("스토리 텍스트를 입력하고, 씬을 검수한 뒤 질문을 생성하세요.")

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
    analyze_clicked = st.button("① 씬 분석하기", type="primary", use_container_width=True)

# ── ① 씬 분석 ─────────────────────────────────────────────────────────────────
if analyze_clicked:
    if not story_text.strip():
        st.error("스토리 텍스트를 입력해주세요.")
    elif not api_key.strip():
        st.error("API 키를 입력해주세요.")
    else:
        # Alt 텍스트 생성 (이미지 업로드된 경우)
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

        with st.spinner("씬을 분석하고 있습니다..."):
            try:
                scenes = analyze_scenes(api_key, api_provider, story_text)
                st.session_state["scene_analysis"] = scenes
                st.session_state.pop("result", None)
            except Exception as e:
                st.error(f"씬 분석 오류: {e}")

# ── 씬 분석 결과 표시 + ② 질문 생성 ──────────────────────────────────────────
if "scene_analysis" in st.session_state:
    st.subheader("① 씬 분석 결과")
    st.caption("셀을 클릭해 내용을 수정하거나, '포함' 체크박스로 질문 생성 대상 씬을 선택하세요.")

    df = pd.DataFrame(st.session_state["scene_analysis"])
    for col in ["event", "trigger", "result", "emotional_response"]:
        if col not in df.columns:
            df[col] = ""
    if "include" not in df.columns:
        df["include"] = True

    edited_df = st.data_editor(
        df[["scene", "event", "trigger", "result", "emotional_response", "include"]],
        column_config={
            "scene": st.column_config.TextColumn("씬", disabled=True, width="small"),
            "event": st.column_config.TextColumn("사건", width="large"),
            "trigger": st.column_config.TextColumn("계기", width="large"),
            "result": st.column_config.TextColumn("결과", width="large"),
            "emotional_response": st.column_config.TextColumn("심리반응", width="large"),
            "include": st.column_config.CheckboxColumn("포함", width="small", default=True),
        },
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
        key="scene_editor",
    )

    st.divider()

    generate_clicked = st.button("② 질문 생성하기", type="primary")

    if generate_clicked:
        if not selected_types:
            st.error("질문 유형을 하나 이상 선택해주세요.")
        else:
            included = edited_df[edited_df["include"] == True]
            if included.empty:
                st.error("포함할 씬을 하나 이상 선택해주세요.")
            else:
                scene_summaries = "\n".join([
                    f"{row['scene']}: 사건: {row['event']} | 계기: {row['trigger']} | 결과: {row['result']} | 심리반응: {row['emotional_response']}"
                    for _, row in included.iterrows()
                ])

                with st.spinner("AI가 페르소나 및 질문 풀을 생성하고 있습니다..."):
                    try:
                        prompt = build_prompt(scene_summaries, patterns, keywords, story_words, selected_types, cefr_level)
                        raw = call_api(api_key, api_provider, prompt)
                        st.session_state["result"] = json.loads(raw)
                        st.session_state["scene_summaries"] = scene_summaries
                    except Exception as e:
                        st.error(f"오류가 발생했습니다: {e}")

# ── Alt 텍스트 미리보기 ────────────────────────────────────────────────────────
if "alt_texts" in st.session_state and st.session_state["alt_texts"]:
    with st.expander("생성된 Alt 텍스트", expanded=False):
        for scene_key, alt in sorted(st.session_state["alt_texts"].items()):
            st.markdown(f"**{scene_key}** {alt}")

# ── 결과 출력 ─────────────────────────────────────────────────────────────────
if "result" in st.session_state:
    result = st.session_state["result"]
    persona = result.get("characterPersona", {})
    questions = result.get("questions", {})
    alt_texts = st.session_state.get("alt_texts", {})
    scene_summaries = st.session_state.get("scene_summaries", "")

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

    active_types = [(k, l) for k, l in QUESTION_TYPES if k in questions and k in selected_types]
    if active_types:
        tabs = st.tabs([label for _, label in active_types])
        for tab, (key, _) in zip(tabs, active_types):
            with tab:
                for i, q in enumerate(questions.get(key, [])):
                    render_question(
                        q, i, key, api_key, api_provider,
                        scene_summaries, keywords, story_words, alt_texts, cefr_level,
                    )
