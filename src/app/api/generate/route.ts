import { NextRequest, NextResponse } from "next/server";
import OpenAI from "openai";
import { GoogleGenerativeAI } from "@google/generative-ai";

const SYSTEM_PROMPT = `You are an English learning content designer for children aged 9-11.
Your job is to generate educational question pools based on a given story.
Always respond with valid JSON only. No markdown, no explanation outside JSON.`;

function buildPrompt(
  storyText: string,
  patterns: string,
  characterInfo: string,
  coreMessage: string,
  openingLine: string,
  selectedTypes: string[],
  protagonistName: string
): string {
  const protagonistLine = protagonistName.trim()
    ? `Protagonist Name: ${protagonistName.trim()}`
    : "";

  return `
Story Text:
${storyText}

Core Patterns for Pattern Practice:
${patterns}

Character Info:
${characterInfo}
${protagonistLine}

Core Message: ${coreMessage}
Opening Line: ${openingLine}

Generate the following question types: ${selectedTypes.join(", ")}

Return a JSON object with this exact structure:
{
  "characterPersona": {
    "name": "character name",
    "age": "age range",
    "gender": "gender",
    "personality": "personality description",
    "coreMessage": "core message",
    "openingLine": "opening line"
  },
  "questions": {
    "patternPractice": [
      {
        "question": "Say it with me: '[pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "[exact pattern sentence]",
        "acceptableCriteria": "grading criterion in Korean"
      }
    ],
    "recall": [
      {
        "question": "factual question from the character's POV using 'I' (e.g., 'What sport did I love?')",
        "relatedScene": "SC##",
        "targetAnswers": ["You [verb]...", "You [verb]..."],
        "acceptableCriteria": "grading criterion in Korean"
      }
    ],
    "inference": [
      {
        "question": "inference question from the character's POV using 'I' (e.g., 'Why did I feel scared?')",
        "relatedScene": "SC##",
        "targetAnswers": ["You [verb]...", "You [verb]..."],
        "acceptableCriteria": "grading criterion in Korean"
      }
    ],
    "transfer": [
      {
        "question": "question connecting story to learner's own life (e.g., 'What do you do when you feel scared?')",
        "relatedScene": "SC##",
        "targetAnswers": ["I [verb]...", "I [verb]..."],
        "acceptableCriteria": "grading criterion in Korean"
      }
    ],
    "reflection": [
      {
        "question": "open-ended reflection question about the story",
        "relatedScene": "SC##",
        "targetAnswers": ["I think...", "I think..."],
        "acceptableCriteria": "grading criterion in Korean"
      }
    ]
  }
}

Rules:
- Generate exactly 5 questions for each selected type (omit unselected types from the JSON).
- patternPractice: Each question: "Say it with me: '[pattern sentence]'". The targetAnswer is the exact same sentence. The sentence can start with any subject — do NOT force "I". Story verbatim rule: if the pattern appears verbatim in story dialogue, use it (remove quotes and speaker tags). No-duplicate rule: if the same sentence would repeat across scenes, use it only for the first scene and create a variation for other scenes. Scene order is the primary sort key (SC01 before SC02, etc.). Within that constraint, write each sentence slightly longer or more complex than the previous where possible so difficulty generally increases from sentence 1 to 5.
- recall: questions from the character's "I" POV. targetAnswers address the character with "You [verb]..." but short noun-phrase alternatives are also fine (e.g., "A rabbit. / You brought a rabbit."). NEVER use the character's name or "she"/"he" to refer to the main character in targetAnswers.
- inference: same POV as recall — questions use "I". targetAnswers use "You [verb]..." for the main character. For other characters' actions/emotions, their pronoun ("he", "she") is acceptable.
- transfer: questions use "you" to address the learner. targetAnswers start with "I".
- reflection: for yes/no questions use "Yes, because [reason]. / No, because [reason]." For open-ended questions use "I think..." or "I believe...".
- Acceptable criteria must be written in Korean.
- All questions and answers must be in English.
`;
}

export async function POST(request: NextRequest) {
  try {
    const {
      storyText,
      patterns,
      characterInfo,
      coreMessage,
      openingLine,
      selectedTypes,
      apiProvider,
      apiKey,
      protagonistName,
    } = await request.json();

    if (!apiKey) {
      return NextResponse.json({ error: "API 키를 입력해주세요." }, { status: 400 });
    }

    const userPrompt = buildPrompt(
      storyText,
      patterns,
      characterInfo,
      coreMessage,
      openingLine,
      selectedTypes,
      protagonistName ?? ""
    );

    let rawText = "";

    if (apiProvider === "openai") {
      const openai = new OpenAI({ apiKey });
      const completion = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          { role: "system", content: SYSTEM_PROMPT },
          { role: "user", content: userPrompt },
        ],
        response_format: { type: "json_object" },
        temperature: 0.7,
      });
      rawText = completion.choices[0].message.content || "{}";
    } else {
      const genAI = new GoogleGenerativeAI(apiKey);
      const model = genAI.getGenerativeModel({
        model: "gemini-2.0-flash",
        generationConfig: {
          responseMimeType: "application/json",
          temperature: 0.7,
        },
      });
      const result = await model.generateContent(
        `${SYSTEM_PROMPT}\n\n${userPrompt}`
      );
      rawText = result.response.text();
    }

    const parsed = JSON.parse(rawText);
    return NextResponse.json({ result: parsed });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "알 수 없는 오류";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
