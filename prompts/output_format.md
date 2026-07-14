Return a JSON object with this exact structure:
{
  "characterPersona": {
    "name": "character name",
    "age": "exact age derived from the story (e.g., \"10 years old\")",
    "gender": "gender",
    "personality": "personality description",
    "coreMessage": "one-sentence core message",
    "openingLine": "single continuous tutor script as described above"
  },
  "patterns": [
    "Pattern label — Example: example sentence.",
    "Pattern label — Example: example sentence."
  ],
  "questions": {
    "patternPractice": [
      {
        "question": "Say it with me: 'I [pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "I [pattern sentence]",
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "recall": [
      {
        "question": "WH question about an explicitly stated fact",
        "relatedScene": "SC##",
        "targetAnswers": ["answer variant 1", "answer variant 2"],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "inference": [
      {
        "question": "single direct WH question requiring clues from multiple parts of the story",
        "relatedScene": "SC##",
        "targetAnswers": ["answer variant 1", "answer variant 2"],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "transfer": [
      {
        "question": "question applying the story theme to the learner's own life",
        "relatedScene": "SC##",
        "targetAnswers": ["example answer 1", "example answer 2"],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "reflection": [
      {
        "question": "question asking the learner to evaluate, judge, or reflect",
        "relatedScene": "SC##",
        "targetAnswers": ["example answer 1", "example answer 2"],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ]
  }
}

Rules:
- Generate exactly 5 questions per selected type (omit unselected types entirely).
- Order questions within each type chronologically by scene.
- patternPractice: base sentences on the user-provided Core Patterns above. Each question: "Say it with me: 'I [pattern sentence]'". targetAnswer must start with "I". acceptableCriteria format: "발음을 명확하게 하지 않아도 '[핵심 구조]'를 포함해서 말하면 정답으로 인정한다."
- recall: answers must be explicitly stated in the story. Avoid vague quantity answers. Stick to concrete facts: names, places, actions, objects. acceptableCriteria must name the exact required keyword(s).
- inference: single direct question only — no setup sentences before it. Answer must be derivable from story clues, not speculation. acceptableCriteria must name exact keyword(s) or meaning required.
- transfer: link to story themes; accept any relevant personal answer. acceptableCriteria must specify what type of content counts as correct.
- reflection: ask for evaluation or judgment. acceptableCriteria must specify expected format and key meanings that make a strong answer.
- VOCABULARY: Do not exceed CEFR <<CEFR_LEVEL>> in any question or answer. If a concept requires a word above this level, replace it with a simpler synonym at or below <<CEFR_LEVEL>>. Do not keep the harder word just because it is more precise — always prefer the simpler alternative. Example substitutions: "valuable" → "special" or "important"; "terrified" → "very scared"; "exhausted" → "very tired"; "enormous" → "very big". Apply the sentence structure guide above.
- All questions and answers must be in English. acceptableCriteria must be in Korean.
- age must be a single exact number (e.g., "10 years old"), not a range.
- openingLine must be a single string of natural connected speech, not an array.
