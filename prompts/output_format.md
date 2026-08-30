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
        "question": "Say it with me: '[pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "[exact pattern sentence]",
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "recall": [
      {
        "question": "WH question from the character's POV using 'I' (e.g., 'What sport did I love?')",
        "relatedScene": "SC##",
        "targetAnswers": ["answer in correct grammatical person for the subject of the question", "another acceptable answer"],
        "acceptableCriteria": "채점 기준 (Korean)"
      }
    ],
    "inference": [
      {
        "question": "single direct WH question from the character's POV using 'I' (e.g., 'Why did I feel scared?')",
        "relatedScene": "SC##",
        "targetAnswers": ["answer in correct grammatical person for the subject of the question", "another acceptable answer"],
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
- Select the best 5 questions based on quality, story grounding, and type correctness. After selection, sort them in chronological scene order (SC01 → SC02 → SC03...) as the final step. Scene order controls output order only — do not select a weaker question to achieve a different scene position.
- patternPractice: Each question format: "Say it with me: '[pattern sentence]'". The targetAnswer is the exact same sentence. The sentence can start with any subject (I, He, She, There, Can, The character's name, etc.) — do NOT force "I" as the subject. Story verbatim rule: if the pattern appears as dialogue or a sentence in the story, use that exact text (strip quotation marks and speaker tags). No-duplicate rule: if the same verbatim sentence would repeat across scenes, use it only once (first scene); create a variation for other scenes. Within the scene order constraint, write each sentence to be slightly longer or more complex than the previous where possible so difficulty generally increases from sentence 1 to sentence 5. acceptableCriteria format: "발음을 명확하게 하지 않아도 '[핵심 구조]'를 포함해서 말하면 정답으로 인정한다."
- recall: questions use character's "I" POV (e.g., "What sport did I love?"). targetAnswers use the correct grammatical person based on who the question is about. When the question refers to the speaking main character, use "You [verb]...". When the question refers to another character, use their correct pronoun or name. Short noun-phrase alternatives are also acceptable (e.g., "A rabbit. / You brought a rabbit."). acceptableCriteria must name the exact required keyword(s).
- inference: questions use character's "I" POV. targetAnswers use "You [verb]..." when the answer refers to the speaking main character. When the answer is about another character's action or emotion, use that character's correct pronoun ("he", "she") or name. acceptableCriteria must name exact keyword(s) or meaning required.
- transfer: questions address the learner with "you". targetAnswers start with "I" (learner talks about themselves). acceptableCriteria must specify what type of content counts as correct.
- reflection: for yes/no questions use "Yes, because [reason]. / No, because [reason]." format; for open-ended questions use "I think..." or "I believe...". acceptableCriteria must specify what evidence or reasoning makes a strong answer for both Yes and No responses.
- VOCABULARY: Do not exceed CEFR <<CEFR_LEVEL>> in any question or answer. If a concept requires a word above this level, replace it with a simpler synonym at or below <<CEFR_LEVEL>>. Do not keep the harder word just because it is more precise — always prefer the simpler alternative. Example substitutions: "valuable" → "special" or "important"; "terrified" → "very scared"; "exhausted" → "very tired"; "enormous" → "very big". Apply the sentence structure guide above.
- All questions and answers must be in English. acceptableCriteria must be in Korean.
- age must be a single specific number (e.g., "10 years old"), never a range or "not specified". If the story does not state the age explicitly, infer it from context and commit to a number.
- openingLine must be a single string of natural connected speech, not an array.
