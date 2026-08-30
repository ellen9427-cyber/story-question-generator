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
        "question": "Say it with me: 'I [pattern sentence]'",
        "relatedScene": "SC##",
        "targetAnswer": "I [pattern sentence]",
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
- patternPractice: use the provided core patterns as the sentences to repeat. The question says "Say it with me: 'I [pattern]'" and targetAnswer must start with "I".
- recall: questions are from the character's first-person POV using "I" (e.g., "What sport did I love?"). The learner answers addressing the character, so ALL targetAnswers must start with "You" (e.g., "You loved tennis."). NEVER use "she", "he", or the character's name in targetAnswers for recall.
- inference: same POV rule as recall — questions use "I", ALL targetAnswers must start with "You". NEVER use "she", "he", or the character's name in targetAnswers for inference.
- transfer: questions use "you" to address the learner directly (e.g., "What do you do when...?"). targetAnswers use "I" because the learner talks about themselves.
- reflection: open-ended questions about the story. targetAnswers use "I think..." or "I believe..." because the learner expresses their own opinion.
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
