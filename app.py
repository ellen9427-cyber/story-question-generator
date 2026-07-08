import json
import streamlit as st
import openai
import google.generativeai as genai

SYSTEM_PROMPT = """You are an English learning content designer for children aged 9-11.
Your job is to generate educational question pools based on a given story.
Always respond with valid JSON only. No markdown, no explanation outside JSON."""

QUESTION_TYPES = [
    ("patternPractice", "Pattern Practice"),
    ("recall", "Comprehension — Recall"),
    ("inference", "Comprehension — Inference"),
    ("transfer", "Extension — Transfer"),
    ("reflection", "Extension — Reflection"),
]


def build_prompt(story_text, patterns, selected_types):
    return f"""
Story Text:
{story_text}

Core Patterns for Pattern Practice:
{patterns}

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
- patternPractice: generate 5 different sentences for the learner to repeat. Each sentence must be unique — do not repeat the same sentence. The sentences do not need to be exact quotes from the story; they should be natural applications or variations of the core patterns within the story's context and flow.
- recall: questions must be answerable directly from the story text only. The acceptableCriteria for each recall question must specify the exact keyword(s) or key content that must appear in the answer — not a generic statement. Format: "'[keyword]'를 포함하여 말하면 정답으로 인정한다." or "[핵심 내용]이 드러나게 말하면 정답으로 인정한다." Include any important constraints (e.g., verb synonyms allowed, specific word variants accepted).
- inference: questions require reading between the lines of the story.
- transfer: questions ask the learner about their own experience or opinion, linked to story themes.
- reflection: open-ended questions asking for evaluation or advice about story events.
- Questions should be from the character's first-person perspective ("What sport did I love?").
- Acceptable criteria must be written in Korean.
- All questions and answers must be in English.
- characterPersona fields (name, age, gender, personality, coreMessage, openingLine) must ALL be written in English, derived from the story text.
"""


def generate_with_openai(api_key, prompt):
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


def generate_with_gemini(api_key, prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            temperature=0.7,
        ),
    )
    result = model.generate_content(f"{SYSTEM_PROMPT}\n\n{prompt}")
    return result.text


def render_question(q, idx):
    with st.container(border=True):
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            st.markdown(f"**{idx + 1}**")
        with col2:
            st.markdown(f"**{q['question']}**")
            st.caption(q.get("relatedScene", ""))

            if q.get("targetAnswer"):
                st.markdown("**Target Answer**")
                st.success(q["targetAnswer"])
            if q.get("targetAnswers"):
                st.markdown("**Target Answers**")
                for a in q["targetAnswers"]:
                    st.success(f"• {a}")

            st.markdown("**채점 기준**")
            st.info(q.get("acceptableCriteria", ""))


# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Story Question Generator", layout="wide")
st.title("Story Question Generator")
st.caption("스토리 텍스트와 패턴을 입력하면 질문 풀을 자동 생성합니다.")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
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

    st.subheader("핵심 패턴 (Pattern Practice용)")
    patterns = st.text_area(
        "패턴",
        placeholder="You're not worried anymore.\nYou're not weak anymore.\n...",
        height=100,
        label_visibility="collapsed",
    )

    st.subheader("생성할 질문 유형")
    selected_types = []
    for key, label in QUESTION_TYPES:
        if st.checkbox(label, value=True, key=key):
            selected_types.append(key)

    generate = st.button("페르소나 및 질문 풀 생성", type="primary", use_container_width=True)

# ── Main ──────────────────────────────────────────────────────────────────────
if generate:
    if not story_text.strip():
        st.error("스토리 텍스트를 입력해주세요.")
    elif not api_key.strip():
        st.error("API 키를 입력해주세요.")
    elif not selected_types:
        st.error("질문 유형을 하나 이상 선택해주세요.")
    else:
        with st.spinner("AI가 질문 풀을 생성하고 있습니다..."):
            try:
                prompt = build_prompt(story_text, patterns, selected_types)
                raw = (
                    generate_with_openai(api_key, prompt)
                    if api_provider == "OpenAI"
                    else generate_with_gemini(api_key, prompt)
                )
                st.session_state["result"] = json.loads(raw)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

if "result" in st.session_state:
    result = st.session_state["result"]
    persona = result.get("characterPersona", {})
    questions = result.get("questions", {})

    # Character Persona
    with st.expander("Character Persona", expanded=True):
        c1, c2, c3 = st.columns(3)
        c1.metric("Name", persona.get("name", "-"))
        c2.metric("Age", persona.get("age", "-"))
        c3.metric("Gender", persona.get("gender", "-"))
        st.markdown(f"**Personality** {persona.get('personality', '')}")
        st.markdown(f"**Core Message** {persona.get('coreMessage', '')}")
        st.markdown(f"**Opening Line** *\"{persona.get('openingLine', '')}\"*")

        st.download_button(
            "전체 JSON 다운로드",
            data=json.dumps(result, ensure_ascii=False, indent=2),
            file_name="result.json",
            mime="application/json",
        )

    # Question Tabs
    active_types = [(k, l) for k, l in QUESTION_TYPES if k in questions and k in selected_types]
    if active_types:
        tabs = st.tabs([label for _, label in active_types])
        for tab, (key, _) in zip(tabs, active_types):
            with tab:
                for i, q in enumerate(questions.get(key, [])):
                    render_question(q, i)
