## Step 2. Generate Activities

Generate all activities and questions in **English**.

---

## Mandatory Generation Process

Do not generate Question, Target Answer, and Acceptable Criteria simultaneously or mechanically. Always follow this internal sequence:

1. Identify the most meaningful and assessable content in the story for the requested question type.
2. Generate multiple candidate questions — more than the required 5.
3. Verify that each candidate correctly belongs to the requested question type.
4. For Transfer: verify that each candidate traces back to a named Transfer Anchor. Reject any that do not.
5. For Recall / Inference: if the question asks about an event, action, feeling, state, or change that occurred in the completed story, confirm it uses Simple Past (did / was / were). Rewrite any candidate that uses present tense for a completed story event.
6. Remove candidates that are trivial, common-knowledge-answerable, unnatural, weakly grounded, or semantically misaligned.
7. Finalize the question first.
8. If the question is about the Speaking Main Character, confirm it uses I / me / my — not the character's name or he / she.
9. Generate the Target Answer only after the question is finalized.
10. Identify who the question is about, then determine the correct grammatical person for the Target Answer.
11. Verify that the Target Answer directly and naturally answers the question.
12. Verify that both question and Target Answer are within the selected CEFR level — check sentence structure, not just vocabulary.
13. Generate Acceptable Criteria only after both Question and Target Answer are finalized.
14. Assign an answer concept to each remaining candidate. Reject any candidate whose answer concept is substantially the same as another already selected candidate (see Answer Diversity Rule).
15. Select the best 5 from the evaluated candidates.
16. Review the scene distribution of the selected 5.
17. Sort the final 5 by scene number (SC01 → SC05) as the last step.
18. Output the final result.

**Core principle: Question quality determines which questions are selected. Scene order controls output order only.**

---

## Candidate Selection

- Final output must contain exactly 5 items per selected question type.
- Internally evaluate more than 5 candidates before selecting.
- Remove any candidate that is:
  - trivial or answerable by common sense without reading the story
  - a duplicate in answer concept: the expected core answer is substantially the same as another selected question, even if the wording differs (see Answer Diversity Rule)
  - unnatural in English
  - weakly grounded in the story
  - incorrectly classified for the requested question type
  - overly obvious (for Inference: the answer requires almost no interpretation)
  - semantically misaligned (Target Answer does not directly answer the question)
  - for Recall / Inference: asking about a completed story event in present tense instead of Simple Past
  - for Transfer: not traceable to a Transfer Anchor identified in Story Analysis
  - for Recall/Inference about the Speaking Main Character: uses the character's name or he/she instead of I/me/my
  - structurally too complex for the selected CEFR level (even if vocabulary is easy)
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

5. **Match the user-selected story level.** All sentences must use vocabulary, grammar, and sentence structure appropriate for the assigned CEFR level.

6. **Young learner appropriateness always.** Keep content concrete, clear, and age-appropriate regardless of level.

7. **Story verbatim rule.** If the target pattern appears verbatim in story dialogue, use that exact sentence (remove quotation marks and speaker tags). Prefer verbatim story sentences over newly created ones.

8. **No-duplicate rule.** If the same verbatim sentence would appear for more than one scene, use it only for the first occurrence. Create a variation for subsequent scenes.

9. **Slot Variation Rule.** When the pattern contains a replaceable slot, first search the whole story for different natural slot values. Prefer meaningful slot variation when it is genuinely story-supported and appropriate for the level.

   **Preferred — different slot values, each story-grounded:**
   With pattern "nothing to ___": `nothing to eat`, `nothing to carry`, `nothing to taste` — each in a different story context, if all are genuinely supported and level-appropriate.

   **Fallback — same slot value, different story context:**
   Only when there are not enough strong slot variations, reuse the strongest slot value in different story-supported contexts:
   - Poppy has nothing to eat.
   - Poppy is hungry because he has nothing to eat.
   - After losing his strawberries, Poppy has nothing to eat.

   Do not force a slot variation that is unnatural, unsupported, too abstract, or above the selected CEFR level. Do not reuse the same slot value repeatedly as the default strategy when alternatives are available.

10. **Reject unnatural applications.** A sentence must be grammatically correct AND natural in context AND appropriate for the learner level.

11. **Do not fabricate story content.** Do not invent new plot events or situations. If the story supports multiple slot values, use them. If only one slot value is strongly supported, reuse it in different story-supported contexts rather than inventing variations.

**Priority order:**
Story accuracy → Target pattern accuracy → Natural meaning → User-selected level → Young learner appropriateness → Natural slot variation → Scene diversity → Contextual variation using the same slot → Additional lexical variety

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
The sentence naturally expresses a cause, consequence, action, or situation that clearly follows from the story.
Examples:
- `After Poppy drops his basket, he has nothing to eat.` (SC05)
- `Poppy follows the yummy smell because he has nothing to eat.` (SC07)

**Level C — Reasonable Contextual Extension (lower priority)**
A reasonable, natural interpretation of the scene that does not invent new events.
Examples:
- `After losing his basket, Poppy has nothing to carry.` (SC05)
- `Poppy has nothing to lose, so he takes a tiny bite.` (SC11)
- `Poppy has nothing to fear about trying colorful food now.` (SC16)

Use Level C when more scene variety is needed, but keep it lower priority than A and B. Evaluate learner level before choosing abstract expressions: `nothing to eat` is more concrete and accessible than `nothing to lose`.

#### Key Rules

**Pattern Practice is not Recall.** A sentence may restate an event, express a consequence, or slightly extend a scene — as long as it remains clearly connected to the story.

**Natural slot variation is preferred.** When the pattern has a replaceable slot, prefer candidates that use a different slot value over candidates that repeat the same slot value in a different context — provided the slot variation is story-grounded and level-appropriate. Contextual variation (same slot, different surrounding text) is the fallback when natural slot alternatives are not available.

**Allow natural slot variation** when different slot values are story-supported and appropriate for the level. Do not restrict all items to the same slot value, but do not invent unsupported variations.

**Prioritize scene diversity when quality is equal.** When two candidates are equally strong, prefer the one from a scene not yet represented.

**Do not force equal distribution.** If only three scenes support strong sentences, use those three.

#### Candidate Priority

1. Level A or B — natural different slot value (preferred variation strategy)
2. Level A or B — same slot value, different story context (fallback variation strategy)
3. Level C — natural slot variation (when level-appropriate and clearly supported)
4. Level C — same slot, contextual extension
5. Additional scene coverage

#### Final Check

- Are items spread across different scenes when possible?
- Did I search the whole story for different natural slot values before reusing the same one?
- Did I look beyond the scene containing the exact target phrase?
- If the sentence is inferred, is the inference reasonable?
- Am I avoiding both extremes?

**Priority order: Story accuracy → Target pattern accuracy → Natural meaning → Learner appropriateness → Natural slot variation → Scene diversity → Contextual variation using the same slot → Additional lexical variety**

---

### Required Candidate Process for Pattern Practice

Follow this sequence when generating Pattern Practice sentences:

**Step 1** — Identify the fixed part and replaceable slot of the pattern.
Example: `nothing to {verb}` → Fixed frame: `nothing to` / Replaceable slot: `{verb}`

**Step 2** — Search the whole story for different natural values for the slot.
Example candidate search: eat / carry / taste / drink / do

**Step 3** — Filter candidates by: (1) story grounding, (2) semantic naturalness, (3) CEFR level, (4) young learner appropriateness.

**Step 4** — Reject slot variations that are unsupported, unnatural, too abstract, idiomatic above the learner level, or created only for variety.

For the Poppy story at A1: `nothing to eat` and `nothing to carry` are potentially strong. `nothing to lose` and `nothing to fear` are likely too abstract — do not select them merely to achieve slot variation.

**Step 5** — Use as many strong slot variations as naturally available.

**Step 6** — Only if fewer than 5 strong examples remain after Steps 1–5, reuse the strongest slot value in different story-supported contexts.

---

### Recall

Generate **5 questions**.

Requirements:
- Ask only about facts explicitly stated in the story.
- Do not ask about opinions.
- Every question must require the learner to have read the story.
- Questions about the Speaking Main Character must use I / me / my — not the character's name or he / she.

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
- Questions about the Speaking Main Character must use I / me / my.

Inference questions should be appropriately simple for young EFL learners:
- Why did I...? / Why was I...?
- How did I feel when...?
- Why did [other character]...?
- How did [other character] feel?

Avoid Inference questions where the reason or answer is so explicitly and immediately signaled by the surrounding text that almost no interpretation is required.

**Good example — allow:**
**Why was I sad in the morning?**
→ Milo lost his colors. The learner must connect this event to his emotional state.

**Avoid:**
**Why did I take a tiny bite of the yellow banana?**
→ The surrounding text immediately lists: nothing to eat, hungry, tummy rumbling, offered a banana, smells sweet. Almost no interpretation needed.

---

### Recall / Inference Tense Rule

**When asking about actions, events, feelings, states, or changes that occurred in the completed story, use the Simple Past.**

Recall and Inference are about a story the learner has already read. Story events are completed. Use `did + base verb` or `was / were`.

Do not mechanically copy present-tense phrasing from story summaries or draft questions.

| Bad | Good |
|-----|------|
| What do I drop into the river? | What did I drop into the river? |
| Why do I follow the yummy smell? | Why did I follow the yummy smell? |
| How do I feel before I try the banana? | How did I feel before I tried the banana? |
| Why am I hungry? | Why was I hungry? |
| What food do I try first? | What food did I try first? |
| What happens to my feet? | What happened to my feet? |
| Why does Chef Pip give me a banana? | Why did Chef Pip give me a banana? |

**Tense validation — before finalizing every Recall and Inference question:**
1. Does the question refer to an event, action, feeling, state, choice, or change that occurred in the story?
2. If yes: use Simple Past. Check `do/does → did`, `is/am/are → was/were`, verb after `did` stays base form.
3. Reject and rewrite any question that asks about a completed story event in the present tense.

**Exception — do not force past tense when the question genuinely asks about a general truth outside the completed story.** Transfer questions about the learner's current life use present tense naturally. Reflection tense depends on the question form. Pattern Practice follows the tense required by its target pattern.

---

### Transfer

Generate **5 questions**.

Transfer questions must connect a **central story idea** to the learner's real life.

Every Transfer question must be traceable to one of the Transfer Anchors identified in Story Analysis.

**Before accepting any Transfer question, answer internally:**
Which Transfer Anchor does this question connect to?

If you cannot name a clear Transfer Anchor, reject the question.

Requirements:
- Questions must address the learner using "you".
- Connect to a central conflict, character change, decision, or lesson — not to incidental objects, settings, or minor characters.
- Transfer is about the learner's real experience, not a hypothetical story situation.
- Do not classify hypothetical story decisions as Transfer — those belong in Reflection.

**The same question may be valid for one story but invalid for another.**
A question's validity depends on whether it connects to the central idea of the current story.

Example:
"What do you usually do with your friends?" is reasonable for Pip (friendship is central).
The same question is not appropriate for Poppy (friendship is incidental — the story is about trying new food).

### Poppy — Transfer Example

Good (connected to Transfer Anchors):
- What new food do you want to try?
- Do you like trying new food?
- What do you do when you see a new food?
- Have you tried a food you did not like before?

Bad (surface detail — not connected to core conflict or change):
- What is your favorite animal?
- What do you like to do with your friends?
- What is your favorite color?

#### Meaningful Transfer Responses

Transfer questions should give the learner something concrete to talk about.

Whenever natural, prefer `When`, `What`, `Who`, `Where`, or `How` questions over Yes/No questions.

Examples:
- `Do you get scared?` → `When do you get scared?`
- `Do you feel brave?` → `What helps you feel brave?`
- `Do you guess things?` → `What do you do when you see something strange?`
- `Do you like new friends?` → `How do you feel when you make a new friend?`

Level-appropriate target answers can remain short but must be concrete and complete:
- `I get scared at night.`
- `My mom helps me feel brave.`
- `I look at it carefully.`
- `I feel happy.`

Use a Yes/No Transfer question only when that format is the most natural choice. When the question asks about an opinion, preference, or willingness, add `Why or why not?` when appropriate and include reasons in both the target answers and evaluation criteria.

---

### Reflection

Generate **5 questions**.

Reflection questions must belong to one of these three types:

**Type 1 — Same Situation**
Ask learners what they would do if they were in the character's situation.

Cognitive intent: imagine making a decision as the character.
Wording depends on level:
- Pre-A1/A1: "Would you ___ too?" / "What would you do?"
- A2: "What would you do if ___?"
- B1+: "If you were me, would you ___? Why?"

**Type 2 — Evaluate the Character**
Ask learners to judge the character's action or choice.

Cognitive intent: assess whether the character's behavior was appropriate.
Wording depends on level:
- Pre-A1/A1: "Was I right to ___?" / "Was my choice good?"
- A2: "Was it a good choice? Why?"
- B1+: "Do you think I made a good choice? Why?"

**Type 3 — Story Lesson (fallback only)**
Ask learners to think about the overall meaning or message of the story. Use only when there are not enough meaningful, non-duplicative, scene-based Reflection questions. Generate no more than one.

Cognitive intent: reflect on the theme.
Wording depends on level:
- Pre-A1/A1 and A2: "What did you learn from my story?"
- B1+: "What is the most important lesson in the story?"

Never use: `What can we learn?` / `What did I learn?` / `What is the lesson in this story?` / `What can we learn from my story?`

**Do not reproduce complex high-level question structures at lower CEFR levels.** The cognitive type stays the same; the syntax changes with the level.

Avoid vague questions:
- "What do you think about [character]?"
- "What do you think about the story?"

Do not classify learner personal experience questions as Reflection — those belong in Transfer.
Example: "Have you ever wanted something your friend had?" → Transfer, not Reflection.

---

## POV Hard Rule

This is a mandatory rule, not a preference.

Recall and Inference questions about the Speaking Main Character must use first-person perspective. Using the character's name or third-person pronouns for the Speaking Main Character is a generation error that must be caught and corrected before output.

**Correct:**
- What did I lose?
- Why was I hungry?
- What did I drop into the river?
- What is my favorite food?

**Incorrect — must be rewritten:**
- What did Poppy lose? → What did I lose?
- Why was Poppy hungry? → Why was I hungry?
- What did Poppy drop into the river? → What did I drop into the river?
- What is Poppy's favorite food? → What is my favorite food?

Questions about other characters (not the Speaking Main Character) use that character's name or correct pronoun:
- What does Chef Pip do every year? ✓
- What did Chef Pip bring me? ✓

---

## POV Final Rewrite Check

Before finalizing any Recall or Inference question, scan it for:
- the Speaking Main Character's name used as the subject or possessive
- "he", "she", "his", "her", "him" referring to the Speaking Main Character

If any of these appear and they refer to the Speaking Main Character, rewrite the question using "I", "me", or "my" before proceeding.

This check runs on every Recall and Inference question — not just on ones you suspect are wrong.

---

## No Quotation-Based Questions

Do not create questions in Recall, Inference, Transfer, or Reflection that directly quote a character's words and ask why they said it.

Forbidden formats:
- "Why did I say this?"
- "Why did he say this?"
- "What did she mean when she said...?"
- Any format presenting a direct quotation and asking for the reason behind it.

Instead, ask directly about the situation, action, emotion, decision, or result.

Exception: Pattern Practice, where the learner is asked to repeat or produce an exact sentence.

---

## Answer Diversity Rule

**Do not select multiple questions whose expected answers express substantially the same core meaning, even when the questions are worded differently.**

Different wording does not make two questions meaningfully different if the learner would give essentially the same answer.

### What counts as the same answer?

Treat answers as duplicates when their **core semantic content** is the same, even if wording differs.

Examples that count as the same answer:
- Because you were hungry.
- You were hungry.
- Because you had nothing to eat.
- You wanted food because you were hungry.

If all of these assess essentially the same cause — Poppy's hunger — they share one answer concept.

Similarly:
- You felt sad. / You were sad. / You felt unhappy.
may count as the same answer concept when they refer to the same event and same emotion.

### Poppy Bad Example — do not generate

| Question | Core answer concept |
|----------|---------------------|
| Why did I follow the yummy smell? | HUNGER |
| Why did I go to the Rainbow Picnic? | HUNGER |
| Why did my tummy rumble? | HUNGER |

All three expect `Because you were hungry.` Keep only the strongest one; replace the others with questions that assess different information.

### Answer Concept Check

For each candidate question, internally assign a short answer concept label.

Examples:
- Why did I follow the yummy smell? → HUNGER
- How did I feel after I lost my strawberries? → SADNESS
- Why did I keep trying colorful food? → NEW FOOD TASTED GOOD
- What food did I try first? → BANANA

Before selecting the final 5:
1. Compare all answer concepts.
2. Do not select multiple items with the same answer concept.
3. Prefer questions that assess different events, reasons, feelings, actions, changes, or story facts.
4. Replace semantic duplicates before output.

### Important distinction

Do not ban the same keyword automatically. Two answers may share a word but still test different information.

Example:
- What food did I try first? → A banana. (fact about food choice)
- What happened after I ate the banana? → Your feet turned yellow. (consequence)

These are different answer concepts even though both involve the banana scene.

The rule is about **duplicate answer meaning** — not duplicate vocabulary.

---

## Examples of Well-Designed Questions by Type

The following examples are based on the story of **Milo**, who loses his colors, looks for them in the forest, meets colorful animals and objects, and eventually discovers his own colors again.

### Recall

Ask about information directly stated or clearly shown in the story. The learner only needs to remember a fact.

Good examples:
- **What color was I in the morning?** → Gray.
- **What did I see first in the forest?** → A yellow butterfly.
- **What did I see in the water?** → Many colors.

### Inference

Require the learner to interpret a reason, emotion, relationship, or conclusion not directly stated.

Good examples:
- **Why was I sad in the morning?** → You lost your colors.
- **Why did I stop asking others for their colors?** → You learned that their colors were important to them.
- **How did seeing many colors in the water change me?** → You began to feel better.

Note: "Why was I sad in the morning?" is valid Inference — the learner must connect the loss of colors to the emotion of sadness, even though the evidence is nearby.

Avoid questions where the answer is so explicitly and immediately signaled that almost no interpretation is needed.

### Transfer

Connect a central story idea to the learner's real life, traceable to a Transfer Anchor.

Milo's Transfer Anchors: accepting what makes you special, valuing differences, losing something and finding it again.

Good examples:
- **What makes you special?** → I am good at drawing.
- **What is different about you and your friends?** → I like drawing, but my friend likes singing.

Bad examples (surface detail — not connected to Milo's central theme):
- "What color do you like?" — colors in Milo are a metaphor, not the topic of Transfer.
- "Have you seen a butterfly?" — a butterfly is incidental.

### Reflection

Questions must belong to one of three types. Wording adapts to CEFR level.

**Type 1 — Same Situation (level examples)**

Pre-A1/A1: Would you look for your colors too?
A2: What would you do if you lost your colors?
B1+: If you were me, would you look for your lost colors? Why?

**Type 2 — Evaluate the Character (level examples)**

Pre-A1/A1: Was I right to ask others for their colors?
A2: Was it a good choice to ask others for their colors? Why?
B1+: Do you think it was a good idea to ask others for their colors? Why or why not?

**Type 3 — Story Lesson (level examples, fallback only)**

Pre-A1/A1 and A2: What did you learn from my story?
B1+: What is the most important lesson in the story?

### Important: Classify by thinking required, not by question wording

| Type | Example | Thinking required |
|------|---------|------------------|
| Recall | What color was I in the morning? | Remember a fact |
| Inference | Why was I sad in the morning? | Interpret meaning from context |
| Transfer | What makes you special? | Connect story to own experience |
| Reflection — Situation | Would you look for your colors too? | Imagine making a decision as the character |
| Reflection — Evaluation | Was I right to ask others for their colors? | Judge the character's behavior |
| Reflection — Lesson | What did you learn from my story? | Reflect on the overall message |

---

## General Requirements

- Generate exactly **5 items** for every activity type.
- Internally evaluate more than 5 candidates and select the best 5 based on question quality, story grounding, type correctness, and naturalness.
- Do not select questions whose expected answers express substantially the same core meaning (see Answer Diversity Rule).
- Cover different parts of the story whenever possible.
- Prefer WH questions over Yes/No questions.
- Use natural English suitable for elementary school learners.
- Progress from lower-order thinking to higher-order thinking:

  Pattern Practice → Recall → Inference → Transfer → Reflection

- **Scene order applies to output sorting only.** After selecting the best 5 questions, sort them in chronological scene order (SC01 → SC02 → SC03...) as the final step. Do not select a weaker question to achieve a different scene position.

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

Allowed:
- Simple Present
- Simple Past
- Present Progressive (basic actions only)
- Basic questions using What, Where, Who, Is/Are, Do/Does, Can
- Basic `When` questions that invite a concrete answer:
  - `When do you get scared?`
- One short `when` or `after` clause when it is necessary to identify the story event:
  - `Where was I when I saw the dark shape?`
  - `How did I feel after I found the kitten?`
- A short purpose phrase when it clarifies an action:
  - `What did I take to check the shape?`

These structures are allowed only when they use familiar words and remain easy for a young learner to process.

A low level does not require removing essential context.

Forbidden:
- Passive voice
- Perfect tenses
- Relative clauses
- Participial phrases
- Gerunds as subjects
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

A lower difficulty level does not mean every sentence must be a simple sentence. Do not mechanically split connected ideas. If combining two ideas with a familiar conjunction makes the meaning clearer and more natural, use the connected sentence.

Prefer: **Poppy is hungry because he has nothing to eat.**
Over: **Poppy is hungry. He has nothing to eat.**

Allowed:
- Everything from Level 1
- Future with will / going to
- Basic infinitives (want to, like to, need to)
- Basic conjunctions: and, but, so, because

Forbidden:
- Passive voice
- Perfect tenses
- Relative clauses
- Participial phrases
- Gerunds as subjects
- Nominal clauses
- Reported speech
- Conditional Type 2 and Type 3
- "Do you think + full clause" structures
- Inversion / Cleft sentences

---

### Level 3 (A2)

Required:
- Use mostly simple sentences with occasional compound or short complex sentences.
- Keep subordinate clauses short and easy to process.

Allowed:
- Everything from Level 2
- Present Perfect (basic)
- First Conditional
- Infinitives
- Gerunds after common verbs
- Time clauses: when, before, after
- Basic subordinate clauses with: because, if, when

Forbidden:
- Passive voice
- Perfect continuous tenses
- Past perfect
- Reduced relative clauses
- Participial phrases
- Complex nominal clauses
- Cleft sentences / Inversion / Subjunctive

---

### Level 4 (B1)

Required:
- Use natural combinations of simple, compound, and basic complex sentences.
- Keep sentence structures appropriate for intermediate learners.
- Avoid advanced academic or literary grammar.

Allowed:
- Everything from Level 3
- Basic passive voice
- Relative clauses
- Past Perfect (basic use)
- Second Conditional
- Reported speech (basic)
- Common modal verbs
- Basic relative pronouns: who, which, that, whose

Forbidden:
- Perfect passive infinitives
- Perfect continuous tenses
- Reduced relative clauses
- Advanced participial constructions
- Inversion for emphasis
- Subjunctive mood
- Cleft sentences / Elliptical clauses
- Multiple embedded clauses

---

## Spoken Difficulty Guide by Level

CEFR controls both vocabulary and question sentence structure. Easy vocabulary alone does not make an easy question.

### Pre-A1 / A1

Use:
- Short, direct, and self-contained spoken questions
- Questions that preserve enough context to identify the relevant event
- WH questions that invite a concrete response
- Yes/No questions only when Yes/No is the most natural response format

Do not shorten a question until its meaning becomes unclear. At lower levels, simplify vocabulary and grammar rather than deleting necessary context.

Avoid:
- "Do you think + full clause" (too complex to process in spoken form)
- Long infinitive constructions
- Embedded clauses or nested questions
- Long conditional structures ("If you were..., would you...?")
- Abstract wording when a concrete verb is available
- Vague questions that could refer to more than one scene (e.g., `Where was I?`, `How did I feel then?`)

Good:
- What did I lose?
- Why was I sad?
- Where was I when I saw the dark shape?
- How did I feel after I found the kitten?
- What new food do you want to try?
- Would you try it too?
- Was I right to try it?

Bad:
- Do you think it was a good idea for Poppy to try the banana?
- Do you think I made the right decision when I decided to try a new kind of food?
- How did I feel then?
- Where was I?

### A2

Use:
- Short sentences with familiar words
- Simple connectors
- One short subordinate clause when useful

Good:
- Why did I feel better after I tried it?
- How did I feel when I saw the new food?
- What do you do when you try something new?

Avoid:
- Multiple clauses in one question
- "Do you think..." structures with long embedded clauses

### B1

Use:
- Natural medium-length sentences
- Clear everyday vocabulary
- Simple and compound sentences; basic complex sentences
- One natural subordinate clause when useful

The sentence should still sound like spoken English for a child, not an exam question.

Good: "Why do you think I changed my mind about the food?"

Do not add complexity simply because B1 allows it.

### B2 or Higher

Use:
- Richer but conversational sentences
- More flexible grammar and broader vocabulary

However:
- Still easy to say aloud
- No academic-test style or literary wording
- Avoid unnecessary embedded clauses
- Prioritize clear spoken English

---

## Level-Specific Question Frames

These frames show natural question syntax for each level. They are not formulas — use the frame that fits the story content. Do not use a frame if it does not fit naturally.

### Recall

Pre-A1/A1:

Do not use context-free frames mechanically. Use a short context phrase when the question could refer to more than one scene:

- Where was I when I ___?
- What did I see at ___?
- What did I take to ___?
- What was the ___ near ___?
- What came into ___?
- What did ___ do?

A2–B1+:
- What happened when I ___?
- How did I ___ before/after ___?

### Inference

Pre-A1/A1:
- How did I feel when ___?
- How did I feel after ___?
- How did ___ feel when ___?
- Why did I ___?
- Why was I ___?

Do not use vague questions such as `How did I feel then?`, `Why did I do that?`, or `What did I think after that?` Name the relevant event directly in the question.

A2–B1+:
- Why do you think I ___?
- How did I feel when ___?
- What does it tell us about ___?

### Transfer

Pre-A1/A1:

Preferred frames:
- When do you ___?
- What helps you ___?
- What do you do when ___?
- Who helps you ___?
- How do you feel when ___?

Do not default to `Do you ___?` or `Do you like ___?` when a WH question would give the learner more to talk about.

A2–B1+:
- What do you do when ___?
- Have you ever ___?
- How can you ___?

All Transfer questions must connect to a Transfer Anchor.

### Reflection

Pre-A1/A1:
- Type 1: Would you ___ too? / What would you do?
- Type 2: Was I right to ___? / Was my choice good?
- Type 3 (fallback only): What did you learn from my story?

A2:
- Type 1: What would you do if ___?
- Type 2: Was it a good choice? Why?
- Type 3 (fallback only): What did you learn from my story?

B1+:
- Type 1: If you were me, would you ___? Why?
- Type 2: Do you think I made a good choice? Why?
- Type 3 (fallback only): What is the most important lesson in the story?

---

## Sentence Complexity and Naturalness

Do not automatically split a sentence into multiple short sentences simply because the assigned level is low.

Use a short compound or complex sentence when it expresses the relationship between ideas more naturally. Familiar connectors (and, but, because, so, when) may be used when appropriate for the level.

### Preserve Meaningful Relationships

Avoid: **Poppy is hungry. He has nothing to eat.**
Prefer: **Poppy is hungry because he has nothing to eat.**

### Do Not Equate "Easy" with "Fragmented"

Sentence simplicity comes from familiar vocabulary, clear word order, limited length, and easy-to-follow meaning — not from removing conjunctions between related ideas.

### Decision Rule

Before splitting a sentence, check:
- Does combining the ideas make the meaning clearer?
- Is the connector familiar and appropriate for the selected level?
- Would splitting make the English sound choppy?
- Can the connected sentence be easily understood by a young EFL learner?

If yes, keep the ideas connected.

**Priority order: Natural meaning → Clear relationship between ideas → User-selected level → Young learner comprehensibility → Sentence simplicity**

---

## Question Writing Rules

- A Recall or Inference item should normally contain one self-contained question sentence. Include necessary context inside the question rather than relying on the scene number or previous item.
- A Reflection item may contain one short first-person context sentence followed by one closely connected evaluation question and `Why?` or `Why not?`
- Examples:
  - `Where was I when I saw the dark shape?`
  - `How did I feel after I found the kitten?`
  - `I took my flashlight to check the shape. Was that a good idea? Why?`
- Do not add context that reveals the answer. Include only the information needed to identify the event or action being discussed.
- Each question should assess only one idea.
- Keep wording clear, concise, and unambiguous.
- Do not quote or copy sentences directly from the story unless required for Pattern Practice.

---

## Question Quality Rules

Before finalizing each question, verify that:
- The question measures the intended thinking skill.
- The question cannot be answered without reading the story.
- The question is specific to this story rather than applicable to most stories.
- The answer is reasonably clear and not overly broad.
- The question is engaging and encourages meaningful thinking.

---

### 1. Avoid Trivial Recall Questions

Do not generate Recall questions answerable through general world knowledge, common sense, or obvious object properties.

Avoid:
- **What color are the bananas at the picnic?** (bananas are yellow — common knowledge)
- **What color is broccoli?**
- **How many legs does the rabbit have?**

Instead, ask about story-specific information: what a character did, what happened before/after an event, what object a character had, where a character went, what changed.

**Better examples:**
- What food did I try first? → You tried a yellow banana.
- What happened to my feet after I ate the banana? → They turned yellow.
- What did I drop into the river? → Your basket of strawberries.

**Recall quality check:**
- Would a learner who has never read the story still be able to answer this easily?
- Is the answer obvious from common knowledge?

If yes, replace the question.

---

### 2. Distribute Questions Across Different Scenes

- Spread questions across the beginning, middle, and end of the story.
- Do not repeatedly use the same scene simply because it contains many easy candidates.
- When several scenes support equally good questions, choose scenes not already used.
- Scene diversity is a preference when candidates are of equal quality — do not sacrifice a stronger question to achieve coverage from an additional scene.

**Scene distribution check:**
- Are too many questions based on the same scene?
- Does the full question set represent the story from beginning to end?

---

### 3. Match Target Answers to the Correct Character and Pronoun

The Target Answer must use the correct grammatical person based on who the question is about.

**Speaking Main Character** (referred to as "I" in the question):
→ Use "You" in the Target Answer.
Example: Q: "What food did I like at first?" → A: "You liked red strawberries."

**Other characters**:
→ Use their correct pronoun or name. Never use "You" for a non-speaking character.
Example: Q: "What does Chef Pip bring to Poppy?" → A: "She brings a basket of colorful food."

**Pronoun rules:**
- Male character → He
- Female character → She
- Plural characters → They
- Object → It
- Speaking Main Character → You
- Named non-speaking character → name or correct third-person pronoun

A single question may require different pronouns for different characters:
Example (Speaking character = Poppy):
Q: "Why did Chef Pip offer me a banana?"
A: "She wanted you to try a new food." ✓
Do NOT: "You wanted to try a new food." ✗

---

### 4. Check Question–Answer Perspective Consistency

Before finalizing each question and Target Answer, identify:
1. Who is speaking (the Speaking Main Character)
2. Who the question is asking about
3. What grammatical person should appear in the answer

Example 1:
Q: "Why did I follow the yummy smell?" → A: "You were hungry." ✓

Example 2:
Q: "Why did Chef Pip offer me a banana?" → A: "She wanted you to try a new food." ✓
Do NOT: "You wanted to try a new food." ✗

Example 3:
Q: "What does Chef Pip do every year?" → A: "She holds a Rainbow Picnic." ✓
Do NOT: "You hold a Rainbow Picnic." ✗

---

## Target Answer Level Check

After generating a Target Answer, verify that it matches the selected CEFR level in both vocabulary and sentence structure.

Target Answers must:
- Directly answer the question
- Match the selected CEFR level
- Use natural spoken English
- Use the correct pronoun
- Avoid extra explanation not required by the question

### A1 — Target Answer Examples

Q: Why was I sad?
Good: Because you lost your color.
Avoid: You were feeling sad because you realized that your special colors had disappeared.

Q: Was I right to help the fish?
Good: Yes. The fish needed help.
Avoid: Yes, because helping the fish was the right decision in that difficult situation.

Do not give a B1-length explanation in response to an A1 question. Match the answer length and structure to the question level.

---

## Final Question Set Quality Check

Before outputting the full question set for each type, verify every item:

1. Does it belong to the requested question type?
2. Recall: Can it only be answered by reading the story — not through common sense?
3. Inference: Does it require interpretation, not just recalling an explicitly stated fact?
4. Transfer: Does it connect to a named Transfer Anchor from Story Analysis?
5. Reflection: Does it belong to one of the three defined Reflection types?
6. Does it avoid quoting a character's speech and asking "Why did X say this?"
7. Is it meaningfully different from every other question in the set?
8. Is it from a different part of the story than most other questions?
9. Was it selected for quality, not to fill a scene slot?
10. For Recall/Inference about the Speaking Main Character: does it use I / me / my?
11. Does the Target Answer use the correct grammatical person?
12. Is "You" used only when referring to the Speaking Main Character?
13. Does the Target Answer directly answer the question?
14. Is the question vocabulary within the selected CEFR level?
15. Is the QUESTION SENTENCE STRUCTURE within the selected CEFR spoken difficulty?
16. Is the TARGET ANSWER structure within the selected CEFR level?
17. Is the language easy to say aloud?
18. Is the content appropriate for young EFL learners?
19. Is the Acceptable Criteria a meaning-based evaluation rule — not a translation of the Target Answer?
20. Story Tense (Recall / Inference only): Does this question ask about a completed story event? If yes, is it in Simple Past?
21. Answer Diversity: What is the core answer concept? Does another selected question in this set already expect substantially the same core answer? If yes, replace the weaker question.

Replace any item that fails before outputting.

---

## Acceptable Criteria Generation Rules

For every generated question, generate an **Acceptable Criteria** statement in Korean explaining what meaning, key information, or structure must appear for the learner's response to be accepted as correct.

Do not require word-for-word reproduction of the Target Answer. Evaluate **meaning and communicative intent**.

### General Rules

1. Do not require an exact match. Accept semantically equivalent answers with different wording.
2. Identify the minimum essential information required. Do not require unnecessary details.
3. Write in Korean using clear statements such as:
   - `~라는 내용이 드러나면 정답으로 인정한다.`
   - `~를 포함하여 ~라는 의미가 되면 정답으로 인정한다.`
   - `~에 대한 구체적인 내용을 한 가지 이상 말하면 정답으로 인정한다.`
4. Judge meaning, not grammar. Minor errors (articles, tense, word order) that do not change meaning should not disqualify an answer.
5. Do not generate generic criteria. Avoid: "Any reasonable answer is acceptable" / "학생이 이유를 말하면 정답으로 인정한다."
6. Allow multiple natural expressions for the same meaning.

### Criteria by Question Type

**Pattern Practice** — Target the grammatical frame, not perfect pronunciation.
Example: `발음을 명확하게 하지 않아도 nothing to + verb의 구조로 말하면 정답으로 인정한다.`

**Recall** — Specify the essential story fact or keyword.
Examples:
- `gray를 포함해서 Milo의 색깔이 회색이 되었다는 내용이 되면 정답으로 인정한다.`
- `butterfly를 포함해서 Milo가 나비를 봤다는 내용이 드러나면 정답으로 인정한다.`

**Inference** — Specify the inferred meaning or causal relationship. Accept different wording for the same valid inference.
Examples:
- `Milo의 색깔이 회색으로 변했거나 자신의 색깔을 잃었기 때문이라는 내용이 드러나면 정답으로 인정한다.`

**Transfer** — Accept any personal answer that connects to the Transfer Anchor and is concrete enough to communicate the learner's idea.
Examples:
- `학생이 직접 먹어 보고 싶은 음식을 한 가지 이상 구체적으로 말하면 정답으로 인정한다.`
- `자신의 외모, 성격, 능력 등에서 특별하다고 생각하는 점을 한 가지 이상 말하면 정답으로 인정한다.`

**Reflection** — Multiple reasonable answers are expected. Cover both Yes and No when applicable.
Example (Yes/No):
`Yes로 답한 경우 [이유 A] 또는 유사한 내용을 근거로 들면 정답으로 인정한다. No로 답한 경우 [이유 B] 또는 유사한 내용을 근거로 들면 정답으로 인정한다.`

### Target Answer vs. Acceptable Criteria

**Target Answer** — A natural example of a strong learner response.
**Acceptable Criteria** — The minimum semantic condition. Must generalize the Target Answer into a meaning-based evaluation rule, not translate it into Korean.

---

## Content Generation Priority Order

When rules compete, apply priorities in this order:

1. Correct question type
2. Story accuracy
3. Core-theme / Transfer Anchor relevance (for Transfer)
4. Correct Speaking Main Character POV (I / me / my)
5. Question–Target Answer semantic alignment
6. CEFR sentence-structure level
7. CEFR vocabulary level
8. Natural spoken English
9. Young learner appropriateness
10. Educational value
11. Scene diversity (tiebreaker among equally strong candidates)
12. Lexical variety
13. Output ordering — sort final selected items by scene number as the last step

---

## Question, Answer, and Evaluation Quality Rules

### 1. Selecting and Formatting Target Words in Acceptable Criteria

When writing `acceptableCriteria` in Korean, select the smallest essential English target word from the model answer.

#### Select the Smallest Meaningful Target Unit

Select the smallest English unit needed to identify the correct meaning.

Use:

1. one word when one word is sufficient;
2. a short phrase when separating it would weaken, broaden, change, or reverse the meaning;
3. a complete structure only when the structure itself is the Pattern Practice target.

One-word targets:
* `green`
* `yellow`
* `flashlight`
* `basket`

Acceptable short-phrase targets:
* `dark shape`
* `not scared`

`dark shape` may remain a phrase because `shape` alone loses an important part of what the learner must identify. `not scared` may remain a phrase because `scared` alone could match the opposite meaning.

Do not copy an unnecessarily long verb-and-object sequence when a smaller unit is sufficient.

Incorrect target: `see the shape`
Correct target: `shape`

The learner's complete response must still express the correct meaning. The presence of the target word or phrase alone is not sufficient when the surrounding response is incorrect or unrelated.

Examples:

Target Answer:

* Your tail turned green.

Target Word:

* green

Acceptable Criteria:

* green을 포함하여 꼬리가 초록색으로 변했다는 내용이 드러나면 정답으로 인정한다.

Target Answer:

* Your feet turned yellow.

Target Word:

* yellow

Acceptable Criteria:

* yellow를 포함하여 발이 노란색으로 변했다는 내용이 드러나면 정답으로 인정한다.

Target Answer:

* You liked red strawberries.

Target Word:

* strawberries

Acceptable Criteria:

* strawberries를 포함하여 Poppy가 좋아하는 음식이 빨간 딸기라는 내용이 드러나면 정답으로 인정한다.

Target Answer:

* You dropped your basket into the river.

Target Word:

* basket

Acceptable Criteria:

* basket을 포함하여 Poppy가 바구니를 강에 떨어뜨렸다는 내용이 드러나면 정답으로 인정한다.

Target Answer:

* You were hungry.

Target Word:

* hungry

Acceptable Criteria:

* hungry를 포함하여 Poppy가 배고팠다는 내용이 드러나면 정답으로 인정한다.

#### Formatting Rules

* Do not place single quotation marks, double quotation marks, or other quotation marks around the English target word.
* Do not translate the target word into Korean and present both versions as separate required target words.
* Do not copy the entire target answer or an unnecessarily long phrase into the criteria.
* Mention the English target word only once.
* Explain the complete required meaning only once in Korean.
* Do not repeat the same information in both English and Korean.

Incorrect:

* 'tail turned green' 또는 '꼬리가 초록색으로 변했다'를 포함하여 브로콜리를 먹은 후 Poppy의 꼬리가 초록색으로 변했다는 내용이 드러나면 정답으로 인정한다.

Incorrect:

* tail turned green을 포함하여 Poppy의 꼬리가 초록색으로 변했다는 내용이 드러나면 정답으로 인정한다.

Correct:

* green을 포함하여 브로콜리를 먹은 후 Poppy의 꼬리가 초록색으로 변했다는 내용이 드러나면 정답으로 인정한다.

#### Exception for Pattern Practice

When the learning target is a grammatical pattern rather than story content, the full target structure may be used instead of one word.

Example:

Target Pattern:

* nothing to carry

Acceptable Criteria:

* 발음을 명확하게 하지 않아도 nothing to carry의 구조를 포함해서 말하면 정답으로 인정한다.

Use this exception only for Pattern Practice or when producing the complete structure is the explicit learning objective. For Recall, Inference, Transfer, and Reflection questions, use one essential target word whenever possible.

### 2. Formatting Multiple Target Answers

In JSON, place each valid answer in a separate `targetAnswers` array element. Each element must be a complete and natural response. If the answers are later combined into one Excel or LCMS field, display them with `/` between answers.

Example JSON:

```json
"targetAnswers": [
  "Yes, I do. I can learn new things.",
  "No, I do not. I like what I already know."
]
```

Displayed form:

> Yes, I do. I can learn new things. / No, I do not. I like what I already know.

Each answer must be a complete and natural response. Do not place multiple slash-separated answers inside one JSON array element.

### 3. Evidence-Grounded Recall and Inference Questions

Every Recall and Inference question must have clear support in the story.

Before generating a question, verify all of the following:

1. The related scene contains enough information to answer the question.
2. The target answer can be explained using the story text, action, situation, or clearly described emotion.
3. The question does not require the learner to guess an emotion that is not supported by the story.
4. The question does not present an unsupported feeling as a definite fact.
5. The acceptable criteria do not include answers that are merely possible but unsupported by the story.

Do not generate a definite emotion question such as:

* How did I feel when my feet turned yellow?

if the story does not state or clearly show Poppy's emotion.

If the question is necessary, use tentative wording:

* How might I have felt when my feet turned yellow?

However, prefer questions with stronger story evidence over speculative questions.

For Inference questions, a reasonable inference must be based on a specific clue in the story. Do not generate an answer merely because it seems possible.

### 4. Natural Meaning and Logical Accuracy

Check the meaning and logic of every question, not only its grammar.

Do not describe a feeling, preference, desire, or uncontrollable event as a `choice`.

Incorrect:

* I did not want to go to the Rainbow Picnic. Was that a good choice?

Not wanting to attend is a feeling or preference, not necessarily a choice.

Better:

* I only ate red strawberries. Was that a good choice?

The action being evaluated must be something the character actually chose to do.

Before using words such as `choice`, `decision`, `action`, or `behavior`, verify that they logically describe the event in the story.

### 5. Reflection Questions Must Require Thinking and Reasons

A Reflection question must ask the learner to:

* evaluate a character's action;
* explain the result of an action;
* consider a meaningful alternative;
* explain the character's change; or
* identify the lesson of the story.

When a Reflection question asks whether something was good, right, helpful, or wise, add `Why?` or `Why not?`

Weak:

* I took a tiny bite of the banana. Was that a good choice?

Better:

* I took a tiny bite of the banana. Was that a good choice? Why?

The target answer must include both:

1. the learner's judgment; and
2. a relevant reason.

Example:

Question:

* I only ate red strawberries. Was that a good choice? Why?

Target Answer:

* No, it was not. You missed many tasty foods.

Acceptable Criteria:

* 좋은 선택이 아니었다고 판단하고, 여러 음식을 맛보지 못했거나 새로운 음식을 경험하지 못했다는 이유를 말하면 정답으로 인정한다.

Do not accept only `Yes` or `No` when the question asks for a reason.

### 6. Questions Must Focus on the Story's Central Message

Do not generate a question simply because an event appears in the story.

The event used in a question must contribute to at least one of the following:

* the character's main problem;
* the character's important action or decision;
* the character's change;
* the cause or result of that change;
* the story's central message.

Avoid questions about minor incidents that do not support the main learning point.

Do not generate:

* Oh no! I dropped my strawberries. What would you do?

This question unnaturally asks the learner what to do about the character's accident, and the accident itself is not the central message of the story.

Prefer questions connected to the character's meaningful change:

* I was afraid to try new food. What could I do?
* I tried a new food and liked it. What does that teach us?

### 7. Transfer Questions Must Request a Reason When Appropriate

For questions about the learner's opinion, preference, willingness, or personal choice, do not stop at a yes-or-no response when a reason would make the response more meaningful.

Weak:

* Do you like to try new things?

Better:

* Do you like to try new things? Why or why not?

The target answer must provide a complete example for each possible position.

Example:

Question:

* Do you like to try new things? Why or why not?

Target Answer:

* Yes, I do. I can learn new things. / No, I do not. I like what I already know.

Acceptable Criteria:

* Yes로 답한 경우 새로운 것을 시도하면서 배우거나 즐거운 경험을 할 수 있다는 등 긍정적인 이유를 말하면 정답으로 인정한다. No로 답한 경우 익숙한 것을 더 좋아하거나 새로운 것을 시도하기 어려운 이유를 말하면 정답으로 인정한다.

The acceptable criteria must evaluate both branches consistently:

* For `Yes`, require a relevant positive reason or benefit.
* For `No`, require a relevant reason based on the learner's preference, comfort, concern, or experience.
* Accept other simple and logically relevant reasons appropriate for the learner's level.
* Do not require the learner to reproduce the model answer word for word.
* Do not accept only `Yes` or `No` when the question asks `Why?` or `Why not?`

### 8. Avoid Duplicate Meanings Across Questions

Do not generate two questions that lead to the same central answer, even when the wording or question type is different.

For example, do not include both:

* Why was my tummy making a loud noise?
* How did I feel before I took a tiny bite of the banana?

if both questions are expected to produce `You were hungry`.

Before finalizing the questions, compare all target answers and remove questions that test the same:

* fact;
* feeling;
* reason;
* action;
* consequence; or
* lesson.

Each question must have a distinct learning purpose.

Possible distinctions include:

* the cause of the problem;
* the character's action;
* the result of the action;
* the character's change;
* the lesson of the story;
* the learner's own related experience.

`How did I feel? — You were hungry.` is grammatically possible, but do not use it when another question already tests Poppy's hunger or when the story provides stronger evidence for a different question.

### 9. Natural English Meaning Check

After generating every question and target answer, perform a separate meaning check.

Verify that:

* the English expresses the intended meaning naturally;
* the question and answer form a logical pair;
* the subject and pronouns are consistent;
* the tense matches the story event;
* the answer directly responds to the question;
* the wording is appropriate for the selected Book Level;
* a Korean idea has not been translated too literally into unnatural English;
* the question sounds natural when spoken by the story character;
* the target answer does not contain unsupported, redundant, or unnecessarily abstract ideas;
* a state, feeling, action, preference, and choice are not confused with one another.

For lower Book Levels, prefer short, concrete sentences and familiar vocabulary. For higher Book Levels, allow longer explanations and more abstract reasoning when appropriate.

### 10. Asking About the Story's Lesson

A general lesson question is a fallback Reflection question, not a required Reflection question.

First, try to generate Reflection questions about:

* an important action or decision;
* the reason an action was good or unhelpful;
* the consequences of an action;
* a meaningful alternative action;
* the character's change.

Use a general lesson question only when there are not enough meaningful, non-duplicative Reflection questions grounded in specific story events.

Choose the lesson question according to the Book Level.

For lower Book Levels, use:

* What did you learn from my story?

Example Target Answer:

* I learned that trying new things can be fun.

For higher Book Levels, the following question may be used:

* What is the most important lesson in the story?

Example Target Answer:

* The most important lesson is that trying new things can lead to positive experiences.

Do not use:

* What can we learn?
* What did I learn?
* What is the lesson in this story?
* What can we learn from my story?

Additional rules:

* Generate no more than one general lesson question.
* Do not generate both lesson-question forms in the same question set.
* Do not use a lesson question merely to fill the required number of Reflection items.
* Do not use a general lesson question when a more specific and meaningful scene-based Reflection question is available.
* Make sure the target answer states a lesson that is clearly supported by the character's experience and change.
* Adjust the vocabulary, sentence length, and level of abstraction to the selected Book Level.

Example for a lower Book Level:

Question:

* What did you learn from my story?

Target Answer:

* I learned that trying new things can be fun.

Acceptable Criteria:

* 새로운 것을 시도하면 즐거운 경험을 하거나 새로운 것을 발견할 수 있다는 이야기의 교훈을 말하면 정답으로 인정한다.

Example for a higher Book Level:

Question:

* What is the most important lesson in the story?

Target Answer:

* The most important lesson is that trying new things can lead to positive experiences.

Acceptable Criteria:

* 새로운 것을 시도하는 것이 새로운 발견이나 긍정적인 경험으로 이어질 수 있다는 핵심 교훈을 말하면 정답으로 인정한다.

### 11. Final Quality-Control Check

Before returning the final output, review all questions as one complete set and confirm that:

1. Each `acceptableCriteria` uses the smallest essential English target word whenever possible.
2. A short phrase is used when its words form a necessary meaning unit, such as `dark shape` or `not scared`. A complete sentence structure is used only when the structure itself is the Pattern Practice objective.
3. No English target word, phrase, sentence, or Pattern Practice structure is enclosed in quotation marks in `acceptableCriteria`.
4. English target words are not unnecessarily translated and repeated as Korean target words.
5. The English target word is mentioned only once.
6. JSON alternatives are stored as separate array elements and are joined with `/` only for single-field display.
7. Each answer is complete and natural.
8. Every Recall and Inference answer has sufficient story evidence.
9. No unsupported emotion is presented as a definite fact.
10. Every evaluated action is an actual action or choice.
11. Every evaluative or opinion question asks for a reason when appropriate.
12. Every target answer includes the reason requested by the question.
13. The acceptable criteria require the same essential information as the question and target answer.
14. Yes and No responses are evaluated according to consistent standards.
15. No two questions test the same meaning or produce substantially the same answer.
16. Every Reflection question is connected to the character's change or the central message.
17. Every question focuses on a meaningful story event rather than an incidental detail.
18. Every sentence is grammatically correct, logically natural, and appropriate for the selected Book Level.
19. A general lesson question is used only when there are not enough meaningful, non-duplicative, scene-based Reflection questions.
20. If a lesson question is used, it matches the Book Level.
21. No more than one general lesson question is generated.
22. `What did you learn from my story?` and `What is the most important lesson in the story?` do not appear together.
23. No question is included merely to fill the required number of items.
24. Every question is understandable without its `relatedScene` value.
25. Necessary context has not been removed merely to satisfy a lower CEFR level.
26. No Recall or Inference question uses vague wording such as `Where was I?`, `What did I see?`, or `How did I feel then?` when multiple contexts are possible.
27. Transfer questions use WH forms whenever they create a more concrete learner response.
28. Yes/No Transfer questions are used only when they are the most natural format.
29. Every target answer is a complete and natural response.
