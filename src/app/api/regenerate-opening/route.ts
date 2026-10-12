import { NextRequest, NextResponse } from "next/server";
import OpenAI from "openai";
import { GoogleGenerativeAI } from "@google/generative-ai";

export async function POST(request: NextRequest) {
  try {
    const {
      currentOpeningLine,
      modificationRequest,
      characterInfo,
      coreMessage,
      storyText,
      protagonistName,
      apiProvider,
      apiKey,
    } = await request.json();

    if (!apiKey) {
      return NextResponse.json({ error: "API 키를 입력해주세요." }, { status: 400 });
    }

    const systemPrompt = `You are an English learning content designer for children aged 9-11.
You generate character opening lines for educational storytelling sessions.
Always respond with valid JSON only. No markdown, no explanation outside JSON.`;

    const userPrompt = `Here is the current opening line for a character:
"${currentOpeningLine}"

Character Info:
${characterInfo || "(not provided)"}
${protagonistName ? `Protagonist Name: ${protagonistName}` : ""}
Core Message: ${coreMessage || "(not provided)"}

Story (for context):
${storyText || "(not provided)"}

Modification request: ${modificationRequest}

Please rewrite the opening line based on the modification request above.
Keep it natural, child-friendly, and in-character.

Return JSON with this exact structure:
{ "openingLine": "rewritten opening line here" }`;

    let rawText = "";

    if (apiProvider === "openai") {
      const openai = new OpenAI({ apiKey });
      const completion = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          { role: "system", content: systemPrompt },
          { role: "user", content: userPrompt },
        ],
        response_format: { type: "json_object" },
        temperature: 0.8,
      });
      rawText = completion.choices[0].message.content || "{}";
    } else {
      const genAI = new GoogleGenerativeAI(apiKey);
      const model = genAI.getGenerativeModel({
        model: "gemini-2.0-flash",
        generationConfig: {
          responseMimeType: "application/json",
          temperature: 0.8,
        },
      });
      const result = await model.generateContent(
        `${systemPrompt}\n\n${userPrompt}`
      );
      rawText = result.response.text();
    }

    const parsed = JSON.parse(rawText);
    return NextResponse.json({ openingLine: parsed.openingLine });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "알 수 없는 오류";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
