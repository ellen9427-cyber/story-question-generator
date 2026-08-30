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
- patternPractice: Each question format: "Say it with me: '[pattern sentence]'". The targetAnswer is the exact same sentence. The sentence can start with any subject (I, He, She, There, Can, The character's name, etc.) — do NOT force "I" as the subject. Story verbatim rule: if the pattern appears as dialogue or a sentence in the story, use that exact text (strip quotation marks and speaker tags). No-duplicate rule: if the same verbatim sentence would repeat across scenes, use it only once (first scene); create a variation for other scenes. Progressive difficulty: arrange 5 sentences from simplest/shortest (sentence 1) to most complex/longest (sentence 5). acceptableCriteria format: "발음을 명확하게 하지 않아도 '[핵심 구조]'를 포함해서 말하면 정답으로 인정한다."
- recall: questions use character's "I" POV (e.g., "What sport did I love?"). targetAnswers should address the character with "You [verb]..." but short noun-phrase answers are also acceptable as alternatives (e.g., "A rabbit. / You brought a rabbit." or "Gray. / You were gray."). Never use "she", "he", or the character's name in targetAnswers when referring to the main character. acceptableCriteria must name the exact required keyword(s).
- inference: same POV rule as recall — questions use "I". targetAnswers use "You [verb]..." for answers about the main character. When the answer is about another character's action or emotion, that character's pronoun ("he", "she") is acceptable. acceptableCriteria must name exact keyword(s) or meaning required.
- transfer: questions address the learner with "you". targetAnswers start with "I" (learner talks about themselves). acceptableCriteria must specify what type of content counts as correct.
- reflection: for yes/no questions use "Yes, because [reason]. / No, because [reason]." format; for open-ended questions use "I think..." or "I believe...". acceptableCriteria must specify what evidence or reasoning makes a strong answer for both Yes and No responses.
- VOCABULARY: Do not exceed CEFR <<CEFR_LEVEL>> in any question or answer. If a concept requires a word above this level, replace it with a simpler synonym at or below <<CEFR_LEVEL>>. Do not keep the harder word just because it is more precise — always prefer the simpler alternative. Example substitutions: "valuable" → "special" or "important"; "terrified" → "very scared"; "exhausted" → "very tired"; "enormous" → "very big". Apply the sentence structure guide above.
- All questions and answers must be in English. acceptableCriteria must be in Korean.
- age must be a single exact number (e.g., "10 years old"), not a range.
- openingLine must be a single string of natural connected speech, not an array.
