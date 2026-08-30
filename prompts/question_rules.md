## Step 2. Generate Activities

Generate all activities and questions in **English**.

---

## Mandatory Generation Process

Do not generate Question, Target Answer, and Acceptable Criteria simultaneously or mechanically. Always follow this internal sequence:

1. Identify the most meaningful and assessable content in the story for the requested question type.
2. Generate multiple candidate questions — more than the required 5.
3. Verify that each candidate correctly belongs to the requested question type.
4. Remove candidates that are trivial, common-knowledge-answerable, repetitive, unnatural, weakly grounded, or semantically misaligned.
5. Finalize the question first.
6. Generate the Target Answer only after the question is finalized.
7. Identify who the question is about, then determine the correct grammatical person for the Target Answer.
8. Verify that the Target Answer directly and naturally answers the question.
9. Generate Acceptable Criteria only after both Question and Target Answer are finalized.
10. Select the best 5 from the evaluated candidates.
11. Review the scene distribution of the selected 5.
12. Sort the final 5 by scene number (SC01 → SC05) as the last step.
13. Output the final result.

**Core principle: Question quality determines which questions are selected. Scene order controls output order only.**

---

## Candidate Selection

- Final output must contain exactly 5 items per selected question type.
- Internally evaluate more than 5 candidates before selecting.
- Remove any candidate that is:
  - trivial or answerable by common sense without reading the story
  - repetitive (assesses the same idea as another selected question)
  - unnatural in English
  - weakly grounded in the story
  - incorrectly classified for the requested question type
  - overly obvious (for Inference: the answer requires almost no interpretation)
  - semantically misaligned (Target Answer does not directly answer the question)
- Do not lower quality standards to fill 5 slots.
- The final output contains only the best 5 after review.

---

## Question Types

### Pattern Practice

A target sentence pattern will be provided separately by the planner.

Generate **5 Pattern Practice sentences** using the provided pattern.

Format:

  Say it with me: "Sentence"

The sentence inside the quotation marks must include the provided target pattern.

---

### Story-Grounded Pattern Sentence Generation

When generating sentences using a target pattern, always prioritize **story accuracy, semantic naturalness, learner appropriateness, and contextual relevance** over lexical variety.

**Core rules:**

1. **Ground every sentence strictly in the provided story.** Use only actions, situations, objects, emotions, and relationships explicitly stated or clearly supported by the story. Do not invent new events or circumstances to fit the pattern.

2. **Analyze the story scene by scene before generating sentences.** Identify which scenes naturally support the target pattern. Each sentence must be traceable to a specific scene.

3. **Generate more than 5 candidates before selecting.** Apply Candidate Selection criteria. Select the best 5 based on story grounding, naturalness, and learner appropriateness.

4. **Progressive difficulty within scene order.** After selecting the best 5, sort them in chronological scene order. Within that constraint, write each sentence to be slightly longer or more complex than the previous where possible, so difficulty generally increases from sentence 1 to sentence 5.

5. **Match the user-selected story level.** All sentences must use vocabulary, grammar, and sentence structure appropriate for the assigned CEFR level. Do not increase difficulty because a more complex sentence sounds more natural.

6. **Young learner appropriateness always.** The primary learners are preschool and elementary-age EFL students. Keep content concrete, clear, and age-appropriate regardless of level.

7. **Story verbatim rule.** If the target pattern appears verbatim in story dialogue, use that exact sentence (remove quotation marks and speaker tags such as "he asks" or "Milo says"). Prefer verbatim story sentences over newly created ones.

8. **No-duplicate rule.** If the same verbatim sentence would appear for more than one scene, use it only for the first occurrence. Create a variation for subsequent scenes.

9. **Do not force lexical variation.** If only one word or phrase naturally fits the pattern in this story, reuse it across different story contexts rather than inventing unsupported expressions. Contextual variation (different subject, cause, consequence, or scene) is preferred over forced lexical variation.

   Example with pattern "nothing to ___" where only "nothing to eat" is story-supported:
   - Poppy has nothing to eat.
   - Poppy is hungry because he has nothing to eat.
   - His tummy rumbles because he has nothing to eat.
   - After losing his strawberries, Poppy has nothing to eat.

10. **Reject unnatural applications.** A sentence must be grammatically correct AND natural in context AND appropriate for the learner level. Grammatical correctness alone is not sufficient.

11. **Do not fabricate story content.** If the story does not support the requested number of distinct examples, reuse valid expressions in different story contexts. Do not invent story details.

**Priority order when making decisions:**

Story accuracy → Natural meaning → Target pattern accuracy → User-selected level → Young learner appropriateness → Scene diversity → Lexical variety

**Before finalizing each sentence, verify:**
- Is it grounded in the story?
- Does it use the target pattern correctly?
- Does it match the assigned difficulty level?
- Is it age-appropriate for young EFL learners?
- Am I creating unnecessary variation unsupported by the story?

---

### Pattern Practice: Story-Grounded Expansion and Scene Diversity

Do not limit generation only to scenes where the exact target expression appears explicitly. The goal is to create **natural, meaningful practice sentences using the target pattern across different story scenes**, while remaining grounded in the story.

#### Levels of Story Support

**Level A — Directly Supported (strongest, most preferred)**
The sentence directly describes information explicitly stated in the story.
Example: `Poppy is hungry because he has nothing to eat.` (SC06 explicitly shows this)

**Level B — Clearly Supported by Story Context**
The exact sentence is not written in the story, but it naturally expresses a cause, consequence, action, or situation that clearly follows from the story. Use freely to distribute practice across different scenes.
Examples:
- `After Poppy drops his basket, he has nothing to eat.` (SC05)
- `Poppy follows the yummy smell because he has nothing to eat.` (SC07)

**Level C — Reasonable Contextual Extension (lower priority)**
Not directly stated but a reasonable, natural interpretation of the scene that does not invent a new event or contradict the story.
Examples:
- `After losing his basket, Poppy has nothing to carry.` (SC05 — implied from losing the basket)
- `Poppy has nothing to lose, so he takes a tiny bite.` (SC11 — inferred from his decision)
- `Poppy has nothing to fear about trying colorful food now.` (SC16 — reasonable interpretation of his change)

Use Level C when more scene variety is needed, but keep it lower priority than A and B.

#### Key Rules

**Pattern Practice is not Recall.** The generated sentence does not need to appear verbatim in the story. It is acceptable to restate an event, express a consequence, connect a cause and result, describe an implied situation, or slightly extend the scene when the meaning remains clearly connected.

**Allow natural verb variation.** When the target pattern has a replaceable slot, different verbs may be used if natural and reasonably story-supported. For `nothing to + verb`: `nothing to eat`, `nothing to taste`, `nothing to carry`, `nothing to lose`, `nothing to fear` are all acceptable if grounded in the scene. Do not require all items to use a different verb, but do not restrict all to the same verb when variety is natural.

**Evaluate naturalness and learner level before selecting variation.** A more abstract or idiomatic expression should not be chosen simply to add variety. Check: Is the expression concrete and accessible for the selected learner level?

**Prioritize scene diversity when quality is equal.** First search the entire story for scenes where the pattern can be directly used, naturally restated, or reasonably inferred. When two candidates are equally strong, prefer the one from a scene not yet represented.

**Do not force equal distribution.** Scene diversity is a preference, not an absolute requirement. If only three scenes support strong sentences, use those three rather than inventing weak examples from five scenes.

#### Candidate Priority

1. Directly supported and natural (Level A)
2. Clearly supported by story context (Level B)
3. Reasonable contextual extension (Level C)
4. Lexical variety
5. Additional scene coverage

A sentence that invents a new event, feeling, or object with no meaningful story connection is not acceptable.

#### Final Check

- Are items spread across different scenes when possible?
- Did I look beyond the scene containing the exact target phrase?
- Can the pattern naturally describe a cause, consequence, or implied situation in another scene?
- If the sentence is inferred, is the inference still reasonable?
- Am I avoiding both extremes: so strict that every item comes from one scene; so flexible that sentences are no longer grounded in the story?

**Priority order: Story accuracy → Natural pattern use → Learner appropriateness → Scene diversity → Lexical variety**

---

### Recall

Generate **5 questions**.

Requirements:

- Ask only about facts explicitly stated in the story.
- Do not ask about opinions.
- Every question must require the learner to have read the story.

**Quality check — before accepting any Recall question, ask:**
Would a learner who has not read the story still be able to answer this easily?
If yes, replace the question.

Do not generate questions answerable by common sense, general world knowledge, or obvious object properties (e.g., "What color are bananas?" or "How many legs does a rabbit have?").

---

### Inference

Generate **5 questions**.

Inference questions require the learner to interpret **an unstated reason, emotion, relationship, change, or conclusion** by using the story's context — not to recall a directly stated fact.

Requirements:

- The answer must not be a single explicit statement taken directly from the story. The learner must interpret, not simply recall.
- A single scene can support a strong Inference question. Do not require connections across multiple scenes as a condition.
- Do not reject an Inference question only because the relevant evidence appears nearby in the text. What matters is whether the learner must interpret meaning rather than repeat a statement.

Avoid Inference questions where the reason or answer is so explicitly and immediately signaled by the surrounding text that almost no interpretation is required.

**Good example — allow:**
**Why was I sad in the morning?**
→ Milo lost his colors. The learner must connect this event to his emotional state. This is valid Inference.

**Avoid:**
**Why did I take a tiny bite of the yellow banana?**
→ The surrounding text explicitly lists: nothing to eat, hungry, tummy rumbling, offered a banana, smells sweet. Almost no interpretation needed.

---

### Transfer

Generate **5 questions**.

Requirements:

- Ask students to connect a story idea to their own life, preferences, experiences, or surroundings.
- Transfer is about the learner's real experience, not a hypothetical story situation.
- Do not classify hypothetical story decisions as Transfer — those belong in Reflection.

---

### Reflection

Generate **5 questions**.

Reflection questions must belong to one of these three types:

**Type 1 — Put the learner in the character's situation**
Ask learners what they would do if they were the character.
Example: "If you were Milo, would you look for your lost colors? Why?"

**Type 2 — Evaluate the character's action or decision**
Ask learners to judge the character's behavior or choices.
Example: "Do you think it was a good idea for Milo to ask others for their colors? Why or why not?"

**Type 3 — Reflect on the story's lesson**
Ask learners to think about the overall meaning or message of the story.
Example: "What can we learn from Milo's story?"

Avoid vague questions such as:
- "What do you think about Milo?"
- "What do you think about the story?"

Do not classify learner personal experience questions as Reflection — those belong in Transfer.
Example: "Have you ever wanted something your friend had?" → Transfer, not Reflection.

---

## No Quotation-Based Questions

Do not create questions in Recall, Inference, Transfer, or Reflection that directly quote a character's words and ask why they said it.

Forbidden formats:
- "Why did I say this?"
- "Why did he say this?"
- "What did she mean when she said...?"
- Any format presenting a direct quotation and asking for the reason behind it.

Instead, ask directly about the situation, action, emotion, decision, or result without quoting the character's words.

Exception: Pattern Practice, where the learner is asked to repeat or produce an exact sentence.

---

## Examples of Well-Designed Questions by Type

The following examples are based on the story of **Milo**, who loses his colors, looks for them in the forest, meets colorful animals and objects, and eventually discovers his own colors again.

### Recall

Recall questions ask about information directly stated or clearly shown in the story. The learner only needs to remember a fact — no interpretation required.

Good examples:
- **What color was Milo in the morning?** → Gray.
- **What did Milo see first in the forest?** → A yellow butterfly.
- **What did Milo see in the water?** → Many colors.

### Inference

Inference questions require the learner to interpret a reason, emotion, relationship, change, or conclusion that is not directly stated in a single sentence.

Good examples:
- **Why was I sad in the morning?** → Milo lost his colors — the learner must connect this event to his emotional state.
- **Why did I stop asking others for their colors?** → He learned that their colors were important to them.
- **How did seeing many colors in the water change me?** → He began to feel better and see colors differently.

Note: A question focused on a single scene can be strong Inference when the learner must interpret meaning rather than recall a statement. Do not reject "Why was I sad in the morning?" simply because the evidence is nearby — the learner must connect the loss of colors to the emotion of sadness.

Avoid Inference where the answer is so directly and explicitly signaled that almost no interpretation is needed.

### Transfer

Transfer questions connect a story idea to the learner's own life, preferences, experiences, or surroundings.

Good examples:
- **What colors can you find around you?** → I see green trees and a blue sky.
- **Have you ever wanted something your friend had? What was it?** → Yes. I wanted my friend's toy.
- **What is something special about you?** → I am good at drawing.
- **What is different about you and your friends?** → I like drawing, but my friend likes singing.

### Reflection

Reflection questions must focus on one of three types:

**Type 1 — Put the learner in the character's situation**
- **If you were Milo, would you look for your lost colors? Why?** → Yes. I would want to find my colors.
- **If you were Milo, what would you do when the butterfly said no?** → I would look for my color somewhere else.

**Type 2 — Evaluate the character's action or decision**
- **Do you think it was a good idea for Milo to ask others for their colors? Why or why not?** → No. They needed their own colors.
- **Was it good for Milo to stop trying to take other colors? Why?** → Yes. The colors were important to the others.

**Type 3 — Reflect on the story's lesson**
- **What did Milo learn from his journey?** → He learned that his own colors were special.
- **What can we learn from Milo's story?** → We can learn to value what makes us special.

### Important: Classify by thinking required, not by question wording

Do not classify a question based on words like "Why?", "Do you think...?", or "If you were...". Classify by the type of thinking the learner must use.

| Type | Example | Thinking required |
|------|---------|------------------|
| Recall | What color was the butterfly? | Remember a fact |
| Inference | Why was I sad in the morning? | Interpret meaning from context |
| Transfer | Have you ever wanted something your friend had? | Connect story to own experience |
| Reflection — Situation | If you were Milo, would you ask the butterfly for its color? | Imagine making a decision as the character |
| Reflection — Evaluation | Do you think Milo should have asked others for their colors? | Judge the character's behavior |
| Reflection — Lesson | What can we learn from Milo's story? | Reflect on the overall message |

---

## General Requirements

- Generate exactly **5 items** for every activity type.
- Internally evaluate more than 5 candidates and select the best 5 based on question quality, story grounding, type correctness, and naturalness.
- Questions must not overlap in meaning or assess the same idea.
- Cover different parts of the story whenever possible.
- Prefer WH questions over Yes/No questions.
- Use natural English suitable for elementary school learners.
- Progress from lower-order thinking to higher-order thinking:

  Pattern Practice → Recall → Inference → Transfer → Reflection

- **Scene order applies to output sorting only.** After selecting the best 5 questions, sort them in chronological scene order (SC01 → SC02 → SC03...) as the final step. Do not select a weaker question to achieve a different scene position or broader scene coverage.

---

## Grammar Constraints by Level

### Level 1 (Pre-A1)

Required:
- Use only very short and simple sentences.
- Use the following sentence patterns:
  - S + V
  - S + V + O
  - S + Be + N
  - S + Be + Adj
  - There is / There are
  - Can + Verb
  - Imperatives
- Use only one independent clause per sentence.
- Use only high-frequency everyday grammar.

Allowed:
- Simple Present
- Simple Past
- Present Progressive (basic actions only)
- Basic questions using What, Where, Who, Is/Are, Do/Does, Can

Forbidden:
- Passive voice
- To-infinitive passive (to be + past participle)
- Perfect tenses
- Future perfect
- Progressive perfect tenses
- Relative clauses
- Relative pronouns (who, which, that) introducing clauses
- Reduced relative clauses
- Participial phrases
- Gerunds as subjects
- Infinitive phrases used as subjects or modifiers
- Appositives
- Nominal clauses (that-, whether-, wh- clauses)
- Reported speech
- Conditional sentences
- Subjunctive mood
- Cleft sentences
- Inversion
- Parenthetical clauses

---

### Level 2 (A1)

Required:
- Use short, natural, easy-to-understand sentences.
- Prefer familiar vocabulary and clear sentence structures.
- Simple sentences are common.
- Short two-clause sentences are allowed when they express the relationship between ideas more naturally than two separate sentences.
- Familiar connectors may include: and, but, so, because.

A lower difficulty level does not mean every sentence must be a simple sentence. Do not mechanically split connected ideas into two short sentences. If combining two ideas with a familiar conjunction makes the meaning clearer and more natural, use the connected sentence.

Prefer: **Poppy is hungry because he has nothing to eat.**
Over: **Poppy is hungry. He has nothing to eat.**

Allowed:
- Everything from Level 1
- Future with will
- Going to
- Basic infinitives (want to, like to, need to)
- Basic conjunctions: and, but, so, because

Forbidden:
- Passive voice
- To-infinitive passive
- Perfect tenses
- Relative clauses
- Participial phrases
- Reduced relatives
- Gerunds as subjects
- Nominal clauses
- Reported speech
- Conditional Type 2 and Type 3
- Inversion
- Cleft sentences

---

### Level 3 (A2)

Required:
- Use mostly simple sentences with occasional compound or short complex sentences.
- Keep subordinate clauses short and easy to process.

Allowed:
- Everything from Level 2
- Present Perfect (basic experience or result)
- First Conditional
- Infinitives
- Gerunds after common verbs
- Time clauses: when, before, after
- Basic subordinate clauses with: because, if, when

Forbidden:
- Passive voice
- To-infinitive passive
- Perfect continuous tenses
- Past perfect
- Future perfect
- Reduced relative clauses
- Participial phrases
- Cleft sentences
- Inversion
- Subjunctive mood
- Complex nominal clauses

---

### Level 4 (B1)

Required:
- Use natural combinations of simple, compound, and basic complex sentences.
- Keep sentence structures appropriate for independent intermediate learners.
- Avoid advanced academic or literary grammar.

Allowed:
- Everything from Level 3
- Basic passive voice
- Relative clauses
- Present Perfect
- Past Perfect (basic use)
- First Conditional
- Second Conditional
- Reported speech (basic)
- Common modal verbs
- Basic relative pronouns: who, which, that, whose

Forbidden:
- To-infinitive passive
- Perfect passive infinitives
- Perfect continuous tenses
- Reduced relative clauses
- Advanced participial constructions
- Inversion for emphasis
- Subjunctive mood
- Cleft sentences
- Elliptical clauses
- Multiple embedded clauses
- Complex nominal clauses with multiple levels of embedding

---

## Sentence Complexity and Naturalness

Do not automatically split a sentence into multiple short sentences simply because the assigned level is low. A lower difficulty level does **not** mean that all sentences must be simple sentences.

Use a short compound or complex sentence when it expresses the relationship between ideas more naturally and clearly. Familiar connectors such as **and**, **but**, **because**, **so**, and **when** may be used when they are appropriate for the assigned level and make the meaning easier to understand.

### Preserve Meaningful Relationships

When two ideas have a clear relationship (cause and effect, contrast, sequence, or condition), prefer a natural connected sentence rather than separating them unnecessarily.

Avoid: **Poppy is hungry. He has nothing to eat.**
Prefer: **Poppy is hungry because he has nothing to eat.**

The second version clearly shows *why* Poppy is hungry and sounds more natural in context.

### Do Not Equate "Easy" with "Fragmented"

Do not simplify language by mechanically breaking every sentence into short statements, removing useful conjunctions, or turning connected ideas into a list. Sentence simplicity should come from familiar vocabulary, clear word order, limited length, and easy-to-follow meaning — not at the expense of natural English or logical relationships between ideas.

### Pattern Practice

For Pattern Practice, prioritize a sentence that demonstrates the target expression in a **natural, meaningful context**. If the target expression works better as part of a short connected sentence, use that structure.

Example with target expression "nothing to eat":
- Prefer: **Poppy is hungry because he has nothing to eat.**
- Over: **Poppy is hungry. He has nothing to eat.**

### Decision Rule

Before splitting a sentence, check:
- Does combining the ideas make the meaning clearer?
- Is the connector familiar and appropriate for the selected level?
- Would splitting the sentence make the English sound choppy or reduce the relationship between ideas?
- Can the connected sentence still be easily understood by a young EFL learner?

If yes, keep the ideas connected.

**Priority order: Natural meaning → Clear relationship between ideas → User-selected level → Young learner comprehensibility → Sentence simplicity**

---

## Question Writing Rules

- Every question must consist of exactly **one sentence**.
- Do not add any introductory, explanatory, or contextual sentence before the question.
- Do not include information that directly reveals or strongly hints at the answer.
- Each question should assess only one idea.
- Keep wording clear, concise, and unambiguous.
- Do not quote or copy sentences directly from the story unless required for Pattern Practice.
- Rephrase naturally instead of repeating the original wording.

## Question Quality Rules

Before finalizing each question, verify that:

- The question measures the intended thinking skill.
- The question cannot be answered without reading the story.
- The question is specific to this story rather than applicable to most stories.
- The answer is reasonably clear and not overly broad.
- The question is engaging and encourages meaningful thinking.

---

### 1. Avoid Trivial Recall Questions

Do not generate Recall questions that can be answered correctly through general world knowledge, common sense, or obvious object properties without reading the story.

Avoid questions such as:
- **What color are the bananas at the picnic?** (bananas are generally known to be yellow)
- **What color is broccoli?**
- **How many legs does the rabbit have?**

Instead, ask about story-specific information: what a character did, what happened before/after an event, what object a character had, where a character went, what changed during the story.

**Bad example:**
What color are the bananas at the picnic? → Yellow. (answerable without reading the story)

**Better examples:**
- What food did Poppy try first? → A yellow banana.
- What happened to Poppy's feet after he ate the banana? → They turned yellow.
- What did Poppy drop into the river? → His basket of strawberries.

**Recall quality check — before accepting a question, ask:**
- Would a learner who has never read the story still be able to answer this easily?
- Is the answer obvious from common knowledge?
- Does answering require remembering the character, event, action, object, or change in the story?

If the learner can answer correctly without knowing the story, replace the question.

---

### 2. Distribute Questions Across Different Scenes

Do not generate too many questions from the same scene or a small group of scenes. Questions should cover a wide range of scenes across the story.

Rules:
- Spread questions across the beginning, middle, and end of the story.
- Do not repeatedly use the same scene simply because it contains many easy question candidates.
- Avoid multiple questions that test slightly different details from the same event.
- When several scenes support equally good questions, choose scenes not already used.

Prefer a distribution such as: one from an early scene, one from the early-middle, one from the middle, one from the later-middle, one from the ending.

Scene diversity is a preference when candidates are of equal quality — do not sacrifice a stronger question to achieve coverage from an additional scene.

**Scene distribution check:**
- Are too many questions based on the same scene?
- Are meaningful scenes from other parts of the story being ignored?
- Does the full question set represent the story from beginning to end?

---

### 3. Match Target Answers to the Correct Character and Pronoun

The Target Answer must use the correct grammatical person based on who the question is about. Do not automatically begin every Target Answer with "You..." simply because the main character speaks in first person.

**Main character** — if the question refers to the speaking main character, second-person ("You") is appropriate.
Example: Q: "What food did I like at first?" → A: "You liked red strawberries."

**Other characters** — use the correct third-person pronoun or the character's name. Never use "You" for a non-speaking character.
Example: Q: "What does Chef Pip bring to Poppy?" → A: "She brings a basket of colorful food." (NOT "You bring...")

**Pronoun rules:**
- Male character → He
- Female character → She
- Animal or character with established pronoun → use that pronoun
- Plural characters → They
- Object → It
- Speaking main character (referred to as "I" in the question) → You
- Named non-speaking character → character's name or correct third-person pronoun

A single question about one scene may require different pronouns for different characters within the same answer.
Example (speaking character = Poppy):
Q: "Why did Chef Pip offer me a banana?"
A: "She wanted you to try a new food." ✓ (Chef Pip = She, Poppy = you)
Do NOT write: "You wanted to try a new food." ✗

---

### 4. Check Question–Answer Perspective Consistency

Before finalizing each question and Target Answer, identify: (1) who is speaking, (2) who the question is asking about, (3) what grammatical person should appear in the answer.

Example 1 — Speaking character: Poppy
Q: "Why did I follow the yummy smell?" → A: "You were hungry." ✓

Example 2 — Speaking character: Poppy
Q: "Why did Chef Pip offer me a banana?" → A: "She wanted you to try a new food." ✓
Do NOT write: "You wanted to try a new food." ✗

Example 3:
Q: "What does Chef Pip do every year?" → A: "She holds a Rainbow Picnic." ✓
Do NOT write: "You hold a Rainbow Picnic." ✗

---

## Final Question Set Quality Check

Before outputting the full question set for each type, verify every item against all of the following:

1. Does it belong to the requested question type?
2. Recall: Can it only be answered by reading the story — not through common sense?
3. Inference: Does it require interpretation, not just recalling an explicitly stated fact?
4. Transfer: Does it connect to the learner's real experience?
5. Reflection: Does it belong to one of the three defined Reflection types?
6. Does it avoid quoting a character's speech and asking "Why did X say this?"
7. Is it meaningfully different from every other question in the set?
8. Is it from a different part of the story than most other questions?
9. Was it selected for quality, not to fill a scene slot?
10. Does the Target Answer directly answer the question?
11. Does the pronoun in the Target Answer match who the question is about?
12. Is "You" used only when referring to the speaking main character?
13. Are both the question and Target Answer natural English?
14. Does the question stay within the selected CEFR level?
15. Is the content appropriate for young EFL learners?
16. Is the Acceptable Criteria a meaning-based evaluation rule — not a translation of the Target Answer?

Replace any item that fails before outputting.

---

## Acceptable Criteria Generation Rules

For every generated question, also generate an **Acceptable Criteria** statement in Korean explaining what meaning, key information, or sentence structure must be included for the learner's response to be accepted as correct.

Do not require the learner to reproduce the Target Answer word for word. Evaluation should prioritize **meaning and communicative intent** over exact wording.

### General Rules

1. **Do not require an exact match with the Target Answer.** The Target Answer is one example of a correct response, not the only acceptable one. Accept semantically equivalent answers even when the learner uses different wording.

2. **Identify the minimum essential information required for correctness.** Specify the key word, concept, relationship, reason, action, or opinion that must be expressed. Do not require unnecessary details.

3. **Write the Acceptable Criteria in Korean.** Use clear statements such as:
   - `~라는 내용이 드러나면 정답으로 인정한다.`
   - `~를 포함하여 ~라는 의미가 되면 정답으로 인정한다.`
   - `~에 대한 구체적인 내용을 한 가지 이상 말하면 정답으로 인정한다.`
   - `자신의 의견과 논리적으로 연결되는 합리적인 근거를 제시하면 정답으로 인정한다.`

4. **Judge meaning rather than exact grammar.** Minor grammatical mistakes (word order, articles, tense, singular/plural) should not make an answer incorrect if the intended meaning is clear. Errors that change the core meaning should not be accepted.

5. **Do not make the criteria unnecessarily strict.** Only specify required vocabulary when that word or concept is essential to identifying the correct answer.

6. **Allow multiple natural expressions for the same meaning.** For example, if the expected meaning is that Milo was happy, accept: `happy`, `better`, `He felt happy.`, `He felt better.`

7. **Do not generate generic criteria.** Avoid statements such as "Any reasonable answer is acceptable," "Accept any answer with a reason," or "학생이 이유를 말하면 정답으로 인정한다." Write question-specific criteria that name the actual concept, fact, or reasoning required.

### Criteria by Question Type

**Pattern Practice** — Evaluate whether the learner produces the target sentence structure or pattern. Focus on the grammatical frame, not perfect pronunciation.
Example criteria: `발음을 명확하게 하지 않아도 Can I {verb phrase}?의 문장 구조로 말하면 정답으로 인정한다.`

**Recall** — Specify the essential story fact (key word or concept) that must appear. Do not require additional explanation.
Examples:
- `gray를 포함해서 Milo의 색깔이 회색이 되었다는 내용이 되면 정답으로 인정한다.`
- `butterfly를 포함해서 Milo가 나비를 봤다는 내용이 드러나면 정답으로 인정한다.`

**Inference** — Specify the reasonable inferred meaning or causal relationship. Accept different wording if it expresses the same valid inference. Do not restrict to one interpretation unless the story clearly supports only one.
Examples:
- `Milo의 색깔이 회색으로 변했거나 자신의 색깔을 잃었기 때문이라는 내용이 드러나면 정답으로 인정한다.`
- `Milo가 행복해졌거나 기분이 나아졌다는 내용이 포함되면 정답으로 인정한다.`

**Transfer** — Accept any personal answer that responds to the question, is relevant to the topic, and contains enough concrete information to communicate the learner's idea.
Examples:
- `학생이 밖에서 볼 수 있는 대상과 색깔에 대해 한 가지 이상 구체적으로 말하면 정답으로 인정한다.`
- `자신의 외모, 성격, 능력 등에서 특별하다고 생각하는 점을 한 가지 이상 말하면 정답으로 인정한다.`

**Reflection** — Multiple reasonable answers are expected. Criteria must describe valid answer conditions, not one predetermined opinion.
- For Yes/No questions: cover both Yes and No positions when both are reasonable.
- For character evaluation: allow different judgments when both can reasonably be supported.
- For lesson questions: accept different wording that expresses a story-supported lesson.
- The learner's reasoning is more important than matching a predetermined opinion.

Example (Yes/No):
`Yes로 답한 경우 [이유 A] 또는 유사한 내용을 근거로 들면 정답으로 인정한다. No로 답한 경우 [이유 B] 또는 유사한 내용을 근거로 들면 정답으로 인정한다. 이외에도 자신의 의견과 논리적으로 연결되는 합리적인 근거를 제시하면 정답으로 인정한다.`

### Target Answer vs. Acceptable Criteria

**Target Answer** — One or more natural examples of what a strong learner response may look like.
**Acceptable Criteria** — The minimum semantic or structural condition required. Must generalize the Target Answer into a meaning-based evaluation rule, not simply translate it into Korean.

### Final Check Before Writing Each Criteria

- What is the minimum meaning required to answer this question?
- Is an exact word necessary, or would a synonym also work?
- Are multiple opinions possible? If Yes/No are both reasonable, have both been covered?
- For personal questions: am I evaluating relevance rather than the learner's personal choice?
- For Pattern Practice: am I evaluating the target structure, not perfect pronunciation?

**Priority order: Correct meaning → Required story information or target structure → Logical relevance → Learner communicative intent → Grammatical accuracy → Exact wording**

---

## Content Generation Priority Order

When making decisions during content generation, apply priorities in this order:

1. Correct question type
2. Story accuracy
3. Question–answer semantic alignment
4. Natural English
5. Correct character and pronoun
6. Question quality and educational value
7. User-selected learner level
8. Young learner appropriateness
9. Scene diversity (as a tiebreaker among equally strong candidates)
10. Lexical variety
11. Output ordering — sort the final selected items by scene number as the last step
