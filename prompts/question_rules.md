## Step 2. Generate Activities

Generate all activities and questions in **English**.

---

## Mandatory Generation Process

Do not generate Question, Target Answer, and Acceptable Criteria simultaneously or mechanically. Always follow this internal sequence:

1. Identify the most meaningful and assessable content in the story for the requested question type.
2. Generate multiple candidate questions — more than the required 5.
3. Verify that each candidate correctly belongs to the requested question type.
4. For Transfer: verify that each candidate traces back to a named Transfer Anchor. Reject any that do not.
5. Remove candidates that are trivial, common-knowledge-answerable, repetitive, unnatural, weakly grounded, or semantically misaligned.
6. Finalize the question first.
7. If the question is about the Speaking Main Character, confirm it uses I / me / my — not the character's name or he / she.
8. Generate the Target Answer only after the question is finalized.
9. Identify who the question is about, then determine the correct grammatical person for the Target Answer.
10. Verify that the Target Answer directly and naturally answers the question.
11. Verify that both question and Target Answer are within the selected CEFR level — check sentence structure, not just vocabulary.
12. Generate Acceptable Criteria only after both Question and Target Answer are finalized.
13. Select the best 5 from the evaluated candidates.
14. Review the scene distribution of the selected 5.
15. Sort the final 5 by scene number (SC01 → SC05) as the last step.
16. Output the final result.

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

9. **Do not force lexical variation.** If only one word or phrase naturally fits the pattern in this story, reuse it across different story contexts. Contextual variation (different subject, cause, consequence, or scene) is preferred over forced lexical variation.

   Example with pattern "nothing to ___" where only "nothing to eat" is story-supported:
   - Poppy has nothing to eat.
   - Poppy is hungry because he has nothing to eat.
   - His tummy rumbles because he has nothing to eat.
   - After losing his strawberries, Poppy has nothing to eat.

10. **Reject unnatural applications.** A sentence must be grammatically correct AND natural in context AND appropriate for the learner level.

11. **Do not fabricate story content.** If the story does not support distinct examples, reuse valid expressions in different story contexts.

**Priority order:**
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

**Allow natural verb variation** when different verbs are story-supported and appropriate for the level. Do not restrict all items to the same verb, but do not invent unsupported variations.

**Prioritize scene diversity when quality is equal.** When two candidates are equally strong, prefer the one from a scene not yet represented.

**Do not force equal distribution.** If only three scenes support strong sentences, use those three.

#### Candidate Priority

1. Directly supported and natural (Level A)
2. Clearly supported by story context (Level B)
3. Reasonable contextual extension (Level C)
4. Lexical variety
5. Additional scene coverage

**Priority order: Story accuracy → Natural pattern use → Learner appropriateness → Scene diversity → Lexical variety**

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

Do not generate questions answerable by common sense, general world knowledge, or obvious object properties.

---

### POV Hard Rule

This is a mandatory rule, not a preference.

Recall and Inference questions about the Speaking Main Character must use first-person perspective. Using the character's name or third-person pronouns for the Speaking Main Character is a generation error that must be caught and corrected before output.

**Correct — Speaking Main Character:**
- What did I lose?
- Why was I hungry?
- What did I drop into the river?
- What is my favorite food?
- At first, what did I ask the son to give me?

**Incorrect — must be rewritten:**
- What did Poppy lose? → What did I lose?
- Why was Milo sad? → Why was I sad?
- What is Poppy's favorite food? → What is my favorite food?

**Questions about other characters use their correct pronoun or name:**
- What did Toby open? → He opened the robot arms. ✓
- What did the youngest son get? → He got a cat. ✓
- What does Chef Pip do every year? ✓

---

### POV Final Rewrite Check

Before finalizing any Recall or Inference question, scan it for:
- the Speaking Main Character's name used as the subject or possessive
- "he", "she", "his", "her", "him" referring to the Speaking Main Character

If any of these appear and they refer to the Speaking Main Character, rewrite the question using "I", "me", or "my" before proceeding.

This check runs on every Recall and Inference question — not just on ones you suspect are wrong.

---

### Inference

Generate **5 questions**.

Inference questions require the learner to interpret **an unstated reason, emotion, relationship, change, or conclusion** by using the story's context — not to recall a directly stated fact.

Keep Inference questions appropriately simple for young EFL learners. Inference does not require literary analysis. The typical Inference question asks the learner to interpret one reason, one feeling, or one causal connection from nearby evidence.

Requirements:
- The answer must not be a single explicit statement taken directly from the story. The learner must interpret, not simply recall.
- A single scene can support a strong Inference question. Do not require connections across multiple scenes.
- Do not reject an Inference question only because the relevant evidence appears nearby in the text. What matters is whether the learner must interpret meaning rather than repeat a statement.
- Questions about the Speaking Main Character must use I / me / my.

Good Inference question forms:
- Why did I ___? / Why was I ___?
- How did I feel when ___?
- Why did [other character] ___?
- How did [other character] feel?
- What might [subject] do next?

Avoid Inference questions where the reason or answer is so explicitly and immediately signaled by the surrounding text that almost no interpretation is required.

**Good example — allow:**
**Why was I sad in the morning?**
→ The learner must connect Milo's loss of colors to his emotional state.

**Good example — allow:**
**Why did I look through a hole?**
→ Pip heard a voice; the learner connects the sound to the action.

**Good example — allow:**
**Why was the fish's lamp fading?**
→ The learner must connect the plastic bag covering the fish's head to the dimming lamp.

**Avoid:**
**Why did I take a tiny bite of the yellow banana?**
→ The surrounding text immediately lists: nothing to eat, hungry, tummy rumbling, offered a banana, smells sweet. Almost no interpretation needed.

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

### Transfer — Proto-Validated Examples by Story

These are examples of good Transfer questions from the reviewed proto set.

**Cat** (Transfer Anchors: cleverness, planning, helping)
- The Cat is good at making plans. What are you good at?
- Tell me about a time you helped a friend. What did you do?

**Didi** (Transfer Anchors: letting things be free, learning from mistakes, honest friendship)
- You really want something, but it is not yours. What do you do?
- Your friend gives you advice, but you think differently. What do you do?

**Hans** (Transfer Anchors: careful decisions, knowing what you need, freedom vs. possessions)
- What can you do before you decide too quickly?
- How can you know what you really need?
- What makes you feel free and happy?

**Kira** (Transfer Anchors: protecting the ocean, taking action to help)
- What can you do to help keep the sea clean?
- What can you do when an animal needs help?
- How do you feel when you help someone?

**Milo** (Transfer Anchors: accepting yourself, valuing differences, what makes you special)
- What makes you special?
- What is different about you and your friends?
- What do you think your color is? Why?

**Pip** (Transfer Anchors: friendship, growing and changing, doing new things)
- How do you make new friends?
- Is there something you couldn't do before, but you can do now?
- You can do something new. How do you feel?

Note: Some questions in the proto set that were labeled Reflection are now classified as Transfer under current policy (e.g., "Have you ever wanted something your friend had?" and "Have you ever believed what others say easily?"). These are Transfer questions because they ask about the learner's real personal experience.

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

**Type 3 — Story Lesson**
Ask learners to think about the overall meaning or message of the story.

Cognitive intent: reflect on the theme.
Wording depends on level:
- Pre-A1/A1: "What can we learn?" / "What did I learn?"
- A2: "What is the lesson in this story?"
- B1+: "What can we learn from this story? Why?"

**Do not reproduce complex high-level question structures at lower CEFR levels.** The cognitive type stays the same; the syntax changes with the level.

Avoid vague questions:
- "What do you think about [character]?"
- "What do you think about the story?"

Do not classify learner personal experience questions as Reflection — those belong in Transfer.
Example: "Have you ever wanted something your friend had?" → Transfer, not Reflection.

### Reflection — Proto-Validated Examples by Type

**Type 1 — Same Situation**
- If you were me, would you let the cloud go? (Didi)
- If you were me, what would you do to help the son? (Cat)
- If you were me and could fly, what would you do first? (Pip)
- If you had a pet like me, what would you ask it to do? (Cat)
- If you were me, which trade would you not make? (Hans)

**Type 2 — Evaluate the Character**
- Do you think I was right to lie to help my master? Why or why not? (Cat)
- Do you think the King trusted me too quickly? Why or why not? (Cat)
- Do you think I was right to catch the cloud? (Didi)
- Was I right to help the fish right away? Why? (Kira)
- Do you think I was special when I was gray? Why or why not? (Milo)
- Do you think I was really lucky? Why or why not? (Hans)

**Type 3 — Story Lesson**
- What can we learn from the Giant's mistake? (Cat)
- What is the most important lesson in this story? (Kira / Didi)
- Are mistakes always bad? (Didi)
- Is change good or bad? Why? (Pip)
- What can we learn? (Milo — simplified form for lower levels)

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

## Examples of Well-Designed Questions by Type

The following examples are drawn from proto-validated question sets across six stories: Cat, Didi, Hans, Kira, Milo, and Pip.

### Recall

Recall questions ask about information directly stated or clearly shown in the story. The learner only needs to remember a fact.

Questions about the Speaking Main Character use "I". Questions about other characters use their name or pronoun.

Good examples — Speaking Main Character perspective:
- **What color was I in the morning?** (Milo) → Gray. / You were gray.
- **At first, what did I ask the son to give me?** (Cat) → A bag and a pair of boots. / You asked him to give you a bag and a pair of boots.
- **What did I make before I went to sleep?** (Pip) → A hard little house. / You made a hard little house.
- **What did I get after working for seven years?** (Hans) → A big piece of gold. / You got a big piece of gold.
- **What did I find in the dark water?** (Kira) → A tiny golden light. / A golden light.

Good examples — Other characters:
- **What did Toby open?** (Kira) → He opened the submarine's robot arms. / The robot arms.
- **What did the youngest son get from his father?** (Cat) → He got a cat. / He got you.
- **What covered the anglerfish's head?** (Kira) → A plastic bag. / A plastic bag covered her head.

### Inference

Inference questions require the learner to interpret a reason, feeling, or conclusion that is not directly stated. Keep them short and simple.

Good examples:
- **Why was I sad in the morning?** (Milo) → Because you were gray. / Because you lost your color.
- **Why did I look through a hole?** (Pip) → Because you heard a voice. / Because you wanted to see who was there.
- **Why did I make a hard little house?** (Pip) → Because you felt sleepy and needed a place to rest.
- **Why was the fish's lamp fading?** (Kira) → The thick plastic bag covered her head.
- **How did the fish show that she was thankful?** (Kira) → She wiggled her fins. / She wiggled her fins and looked at the submarine.
- **Why did I want to trade my gold for the horse?** (Hans) → Because it was heavy.
- **The boy told me about the lost pig. How did I feel?** (Hans) → You felt scared. / You felt afraid.

Note: All of these involve one clear interpretive step from visible context to unstated meaning. None require elaborate multi-scene analysis.

### Transfer

Transfer questions connect a Transfer Anchor to the learner's real life. See the Transfer section above for full examples by story.

Key style points:
- The question connects to the story's CENTRAL conflict or lesson — not to an incidental noun.
- Wording is natural and direct: "What can you do...?", "How do you feel when...?", "Tell me about a time you..."
- The question assumes a real personal response — not a hypothetical story scenario.

### Reflection

Reflection questions must match one of three defined types. Wording adapts to CEFR level.

**Type 1 — Same Situation:**
B1 form: "If you were me, would you let the cloud go?" (Didi)
A1 simplified form of same intent: "Would you let it go?" or "What would you do?"

**Type 2 — Evaluate the Character:**
B1 form: "Do you think I was right to lie to help my master? Why or why not?" (Cat)
A1 simplified form: "Was I right to lie for my master?"

**Type 3 — Story Lesson:**
B1 form: "What is the most important lesson in this story?" (Kira)
A1 simplified form: "What can we learn?"

### Target Answer Format

The standard Target Answer provides two alternatives separated by " / ":
- A short noun-phrase or adjective answer (when natural)
- A full sentence with the correct grammatical person

Examples:
- Recall: "Gray. / You were gray."
- Recall: "A rabbit. / You brought a rabbit."
- Recall: "A big piece of gold. / You got a big piece of gold."
- Inference: "Because you were gray. / Because you lost your color."
- Inference: "She wiggled her fins. / She wiggled her fins and looked at the submarine."
- Reflection (Yes/No): provide at least one Yes answer and one No answer

Keep Target Answers level-appropriate. Do not write a long B1-level explanation for an A1 question.

A1 Recall:
- Good: "Gray. / You were gray."
- Avoid: "The chameleon had completely lost all of his colorful pigmentation, resulting in a gray appearance."

A1 Reflection:
- Good: "Yes. The fish needed help."
- Avoid: "Yes, because helping the fish was the right decision in that difficult situation."

### Important: Classify by thinking required, not by question wording

| Type | Example | Thinking required |
|------|---------|------------------|
| Recall | What color was I in the morning? | Remember a fact |
| Inference | Why was I sad in the morning? | Interpret meaning from context |
| Transfer | What makes you special? | Connect story anchor to own experience |
| Reflection — Situation | Would you let the cloud go? | Imagine making a decision as the character |
| Reflection — Evaluation | Was I right to help the fish right away? | Judge the character's behavior |
| Reflection — Lesson | What can we learn from the Giant's mistake? | Reflect on the overall message |

Note: Questions about the learner's personal experience ("Have you ever wanted something your friend had?") are Transfer, not Reflection, even if they relate to a story theme.

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
- Cleft sentences / Inversion / Parenthetical clauses

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
- Very short, direct spoken questions
- Basic high-frequency words
- One clear idea per question
- Simple What / Who / Where / Why / How questions
- Short Yes/No questions

Avoid:
- "Do you think + full clause" (too complex for spoken processing at A1)
- Long infinitive constructions
- Embedded clauses or nested questions
- Long conditional structures ("If you were..., would you...?")
- Abstract wording when a concrete verb is available

Good:
- What did I lose?
- Why was I sad?
- What new food do you want to try?
- Would you try it too?
- Was I right to try it?
- What can we learn?

Bad:
- Do you think it was a good idea for Poppy to try the banana?
- Do you think I made the right decision when I decided to try a new kind of food?

### A2

Use:
- Short sentences with familiar words
- Simple connectors
- One short subordinate clause when useful

Good:
- Why did I feel better after I tried it?
- What do you do when you try something new?
- Was it a good choice? Why?

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

Use richer but conversational sentences. Still easy to say aloud — no academic-test style, no literary wording, no unnecessary embedded clauses.

---

## Level-Specific Question Frames

These frames show natural question syntax for each level. They are examples — use the frame that fits the story content naturally.

### Recall

Pre-A1/A1:
- What did I ___? / Who did I ___? / Where did I ___?
- What was ___? / What color was ___?
- What did ___ do?

A2–B1+:
- What happened when I ___?
- How did I ___ before/after ___?

### Inference

Pre-A1/A1:
- Why did I ___? / Why was I ___?
- How did I feel? / How did ___ feel?

A2–B1+:
- Why do you think I ___?
- How did I feel when ___?
- What might ___ do next?

### Transfer

Pre-A1/A1:
- What ___ do you like? / Do you like ___?
- What new ___ do you want to try?
- How do you feel when ___?

A2–B1+:
- What do you do when ___?
- Have you ever ___?
- Tell me about a time you ___. What did you do?

All Transfer questions must connect to a Transfer Anchor.

### Reflection

Pre-A1/A1:
- Type 1: Would you ___ too? / What would you do?
- Type 2: Was I right to ___? / Was my choice good?
- Type 3: What can we learn? / What did I learn?

A2:
- Type 1: What would you do if ___?
- Type 2: Was it a good choice? Why?
- Type 3: What is the lesson in this story?

B1+:
- Type 1: If you were me, would you ___? Why?
- Type 2: Do you think I made a good choice? Why?
- Type 3: What can we learn from my story?

---

## Sentence Complexity and Naturalness

Do not automatically split a sentence into multiple short sentences simply because the assigned level is low.

Use a short compound or complex sentence when it expresses the relationship between ideas more naturally. Familiar connectors (and, but, because, so, when) may be used when appropriate for the level.

Avoid: **Poppy is hungry. He has nothing to eat.**
Prefer: **Poppy is hungry because he has nothing to eat.**

Sentence simplicity comes from familiar vocabulary, clear word order, limited length, and easy-to-follow meaning — not from removing conjunctions between related ideas.

**Priority order: Natural meaning → Clear relationship between ideas → User-selected level → Young learner comprehensibility → Sentence simplicity**

---

## Question Writing Rules

- Every question must consist of exactly **one sentence**.
- Do not add any introductory or contextual sentence before the question.
- Do not include information that directly reveals or strongly hints at the answer.
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

Instead, ask about story-specific information: what a character did, what happened, what object a character had, what changed.

**Recall quality check:**
Would a learner who has never read the story still be able to answer this easily?
If yes, replace the question.

---

### 2. Distribute Questions Across Different Scenes

- Spread questions across the beginning, middle, and end of the story.
- Do not repeatedly use the same scene simply because it contains many easy candidates.
- When several scenes support equally good questions, choose scenes not already used.
- Scene diversity is a preference when candidates are of equal quality — do not sacrifice a stronger question to achieve coverage from an additional scene.

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

**A1 — Target Answer Examples**

Q: Why was I sad?
Good: Because you lost your color.
Avoid: You were feeling sad because you realized that your special colors had disappeared.

Q: Was I right to help the fish?
Good: Yes. The fish needed help.
Avoid: Yes, because helping the fish was the right decision in that difficult situation.

Do not give a B1-length explanation in response to an A1 question.

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

Replace any item that fails before outputting.

---

## Acceptable Criteria Generation Rules

For every generated question, generate an **Acceptable Criteria** statement in Korean explaining what meaning, key information, or structure must appear for the learner's response to be accepted as correct.

Do not require word-for-word reproduction of the Target Answer. Evaluate **meaning and communicative intent**.

### General Rules

1. Do not require an exact match. Accept semantically equivalent answers with different wording.
2. Identify the minimum essential information required. Do not require unnecessary details.
3. Write in Korean. Do not generate generic criteria such as "Any reasonable answer is acceptable" or "학생이 이유를 말하면 정답으로 인정한다."
4. Judge meaning, not grammar. Minor errors that do not change meaning should not disqualify an answer.
5. Allow multiple natural expressions for the same meaning.

### Standard Korean Criteria Patterns (from proto)

**Pattern Practice:**
`발음을 명확하게 하지 않아도 [패턴 구조]를 포함해서 말하면 정답으로 인정한다.`

**Recall — single fact:**
`[keyword]를 포함해서 [사실]라는 내용이 드러나면 정답으로 인정한다.`
Example: `gray를 포함해서 Milo의 색깔이 회색이 되었다는 내용이 되면 정답으로 인정한다.`

**Recall — two required facts:**
`[item A]와 [item B]를 모두 언급하면 정답으로 인정한다.`
Example: `가방(a bag)과 장화 한 켤레(a pair of boots)를 달라고 했다는 두 가지 내용을 모두 언급하면 정답으로 인정한다.`

**Inference — causal:**
`[원인 A] 또는 [원인 B]라는 내용이 드러나면 정답으로 인정한다.`
Example: `Milo의 색깔이 회색으로 변했거나 자신의 색깔을 잃었기 때문이라는 내용이 드러나면 정답으로 인정한다.`

**Inference — emotion:**
`[감정 A], [감정 B] 등 [상황에 어울리는 감정]을 말하면 정답으로 인정한다.`
Example: `scared나 afraid와 같은 단어를 포함하여 두려워했다는 내용으로 대답하면 정답으로 인정한다.`

**Transfer:**
`[연결된 전이 주제]에 대한 구체적인 내용을 한 가지 이상 말하면 정답으로 인정한다.`
Example: `자신이 잘하는 일이나 능력을 한 가지 구체적으로 말하면 정답으로 인정한다.`

**Reflection — Yes/No:**
`Yes로 답한 경우 [이유 A] 또는 유사한 내용을 근거로 들면 정답으로 인정한다. No로 답한 경우 [이유 B] 또는 유사한 내용을 근거로 들면 정답으로 인정한다. 이외에도 자신의 의견과 논리적으로 연결되는 합리적인 근거를 제시하면 정답으로 인정한다.`

**Reflection — open-ended lesson:**
`이야기의 교훈을 한 가지 이상 구체적으로 말하면 정답으로 인정한다.`

### Target Answer vs. Acceptable Criteria

**Target Answer** — A natural example of a strong learner response (typically 2 alternatives separated by " / ").
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
