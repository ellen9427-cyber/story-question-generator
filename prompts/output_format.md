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
        "question": "WH question from the character's POV using 'I' (e.g., 'What sport did I love?')",
        "relatedScene": "SC##",
        "targetAnswers": ["You [verb]...", "You [verb]..."],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "inference": [
      {
        "question": "single direct WH question from the character's POV using 'I' (e.g., 'Why did I feel scared?')",
        "relatedScene": "SC##",
        "targetAnswers": ["You [verb]...", "You [verb]..."],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "transfer": [
      {
        "question": "question using 'you' to address the learner (e.g., 'What do you do when...?')",
        "relatedScene": "SC##",
        "targetAnswers": ["I [verb]...", "I [verb]..."],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "reflection": [
      {
        "question": "question asking the learner to evaluate, judge, or reflect",
        "relatedScene": "SC##",
        "targetAnswers": ["I think...", "I think..."],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ]
  }
}

Rules:
- Generate exactly 5 questions per selected type (omit unselected types entirely).
- Order questions within each type chronologically by scene.
- patternPractice: base sentences on the user-provided Core Patterns above. Each question: "Say it with me: 'I [pattern sentence]'". targetAnswer must start with "I". acceptableCriteria format: "발음을 명확하게 하지 않아도 '[핵심 구조]'를 포함해서 말하면 정답으로 인정한다."
- recall: questions use character's "I" POV. targetAnswers MUST start with "You" (learner addresses the character). Never use "she", "he", or the character's name in targetAnswers. acceptableCriteria must name the exact required keyword(s).
- inference: same rule as recall — questions use "I", targetAnswers MUST start with "You". acceptableCriteria must name exact keyword(s) or meaning required.
- transfer: questions address the learner with "you". targetAnswers start with "I" (learner talks about themselves). acceptableCriteria must specify what type of content counts as correct.
- reflection: open-ended; targetAnswers start with "I think..." or "I believe...". acceptableCriteria must specify expected format and key meanings that make a strong answer.
- VOCABULARY: Do not exceed CEFR <<CEFR_LEVEL>> in any question or answer. If a concept requires a word above this level, replace it with a simpler synonym at or below <<CEFR_LEVEL>>. Do not keep the harder word just because it is more precise — always prefer the simpler alternative. Example substitutions: "valuable" → "special" or "important"; "terrified" → "very scared"; "exhausted" → "very tired"; "enormous" → "very big". Apply the sentence structure guide above.
- All questions and answers must be in English. acceptableCriteria must be in Korean.
- age must be a single exact number (e.g., "10 years old"), not a range.
- openingLine must be a single string of natural connected speech, not an array.
