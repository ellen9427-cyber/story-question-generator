## Global Rules

### 1. Age

Required:
- Always express a character's age as a single specific number followed by "years old" (e.g., "8 years old", "35 years old").
- If the story does not explicitly state the age, infer it from story context (appearance, grade level, relationships, behavior, etc.) and output the best estimate as a specific number.
- There is always a reasonable estimate available from context. Always commit to a number.

Forbidden:
- Do not use vague expressions such as:
  - "not specified"
  - "unknown"
  - "adult"
  - "child"
  - "young person"
  - "elderly"
  - age ranges such as "8–10 years old"

---

### 2. Opening Line

Context:
- The Opening Line is spoken by the Speaking Main Character after the learner has finished reading the story.
- Assume the learner has already read the story.

Structure (use in order):
1. Warm greeting + self-introduction: "Hi! I'm [Name]." or "Hello there! I'm [Name]."
2. 1–2 short story recap sentences as the character.
3. Exactly ONE simple question connected to the story's central theme.

Tense rules:
- Self-introduction: use present tense ("Hi! I'm Poppy.")
- Story recap sentences: use past tense because the events have already happened.
- Final learner question: use natural present or simple tense as appropriate.

Do not write the entire Opening Line in past tense. Only the story recap sentences should be past tense.

Required:
- Write in first person as the character ("I"), not as a narrator or teacher.
- Keep the final question connected to a Transfer Anchor or central story idea.
- The final question must be exactly one question — not two.
- Match vocabulary and sentence structure to the selected CEFR level.

Forbidden:
- Do not speak as a narrator or teacher.
- Do not use: "We just read...", "Today we read...", "In this story...", "Let's read...", "Today we will read about..."
- Do not use any wording that assumes the learner has not yet read the story.
- Do not put abstract lesson sentences in the Opening Line (e.g., "I learned that being open to new experiences is important."). Express the lesson through events and questions instead.
- Do not end with two learner questions back to back.
- Do not make the final question about a surface detail (incidental animal, color, or object) when a core-theme question is possible.

Good examples:

Pre-A1 / A1:
"Hi! I'm Poppy. I lost my strawberries. Then I tried new food. What new food do you want to try?"

A2:
"Hi! I'm Poppy. I lost my strawberries, so I tried some new food. What new food would you like to try?"

B1:
"Hi! I'm Poppy. I used to eat only red strawberries, but I tried colorful foods at the picnic. Is there a new food you would like to try?"

---

### 3. Pattern Practice

Required:
- Every Pattern Practice sentence must be a complete, natural, and meaningful sentence.
- The sentence itself should provide educational value.
- The learner should gain a useful expression or sentence that could realistically be used or understood in everyday communication.

Forbidden:
- Do not generate sentences that only combine the target pattern with random vocabulary.
- Do not generate sentences that are grammatically correct but have little or no practical learning value.

Good:
- I forgot my homework at home.
- She was proud of her hard work.

Bad:
- I agree to walk home now.
- He wants to read quickly today.

---

### 4. Reflection Evaluation Criteria

Required:
- Generate evaluation criteria specific to each Reflection question.
- For Yes/No questions: clearly describe what evidence or reasoning is acceptable for both "Yes" and "No" answers.
- The criteria should reference the actual content of the generated question.

Forbidden:
- Do not use generic criteria such as:
  - "Accept any answer with a reason."
  - "The student should explain their opinion."
  - "Any reasonable explanation is acceptable."

---

### 5. Scene Mapping

Required:
- Map every generated question to exactly one scene.
- Select the single most appropriate scene that provides the most relevant context for answering the question.

For Inference questions: the relatedScene is the primary scene most strongly connected to the question. The learner may use context from nearby scenes during interpretation — this does not make the question invalid or require multiple scenes in the JSON.

Forbidden:
- Do not assign multiple scenes to a single question.
- Do not choose a scene that is only loosely related when a more appropriate scene exists.
- Do not remove an Inference question only because the learner would need to consider more than one scene during reasoning.

---

### 6. Closing Line

If a Closing Line is generated, keep it simple and friendly.

Purpose:
- Praise the learner.
- Say goodbye in a warm way.

Do not add story lessons, character reflections, or additional questions.

Good:
- "You did a great job today! See you soon!"
- "You were amazing today! Bye for now!"
- "Great job today! See you soon!"

The same simple style works for all CEFR levels — no need to make it more complex at higher levels.
