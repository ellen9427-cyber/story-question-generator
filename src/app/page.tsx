"use client";

import { useState } from "react";

type QuestionItem = {
  question: string;
  relatedScene: string;
  targetAnswer?: string;
  targetAnswers?: string[];
  acceptableCriteria: string;
};

type QuestionSet = {
  patternPractice?: QuestionItem[];
  recall?: QuestionItem[];
  inference?: QuestionItem[];
  transfer?: QuestionItem[];
  reflection?: QuestionItem[];
};

type GeneratedResult = {
  characterPersona: {
    name: string;
    age: string;
    gender: string;
    personality: string;
    coreMessage: string;
    openingLine: string;
  };
  questions: QuestionSet;
};

const QUESTION_TYPES = [
  { key: "patternPractice", label: "Pattern Practice" },
  { key: "recall", label: "Comprehension — Recall" },
  { key: "inference", label: "Comprehension — Inference" },
  { key: "transfer", label: "Extension — Transfer" },
  { key: "reflection", label: "Extension — Reflection" },
];

const TAB_KEYS = QUESTION_TYPES.map((t) => t.key);

export default function Home() {
  const [storyText, setStoryText] = useState("");
  const [patterns, setPatterns] = useState("");
  const [characterInfo, setCharacterInfo] = useState("");
  const [coreMessage, setCoreMessage] = useState("");
  const [openingLine, setOpeningLine] = useState("");
  const [apiProvider, setApiProvider] = useState<"openai" | "gemini">("openai");
  const [apiKey, setApiKey] = useState("");
  const [selectedTypes, setSelectedTypes] = useState<string[]>(TAB_KEYS);
  const [result, setResult] = useState<GeneratedResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [activeTab, setActiveTab] = useState("patternPractice");
  const [copied, setCopied] = useState(false);

  const toggleType = (key: string) => {
    setSelectedTypes((prev) =>
      prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
    );
  };

  const handleGenerate = async () => {
    if (!storyText.trim()) {
      setError("스토리 텍스트를 입력해주세요.");
      return;
    }
    if (!apiKey.trim()) {
      setError("API 키를 입력해주세요.");
      return;
    }
    if (selectedTypes.length === 0) {
      setError("질문 유형을 하나 이상 선택해주세요.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          storyText,
          patterns,
          characterInfo,
          coreMessage,
          openingLine,
          selectedTypes,
          apiProvider,
          apiKey,
        }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "생성 실패");
      setResult(data.result);
      if (selectedTypes.length > 0) setActiveTab(selectedTypes[0]);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  const handleCopyAll = () => {
    if (!result) return;
    const text = JSON.stringify(result, null, 2);
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const activeQuestions =
    result?.questions[activeTab as keyof QuestionSet] ?? [];

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <header className="bg-white border-b border-gray-200 px-6 py-4">
        <h1 className="text-xl font-bold text-gray-800">
          Story Question Generator
        </h1>
        <p className="text-sm text-gray-500 mt-0.5">
          스토리 텍스트와 패턴을 입력하면 질문 풀을 자동 생성합니다.
        </p>
      </header>

      <div className="flex flex-1 overflow-hidden">
        {/* Left Panel — Inputs */}
        <aside className="w-96 bg-white border-r border-gray-200 flex flex-col overflow-y-auto p-5 gap-5">
          {/* API Settings */}
          <section>
            <h2 className="text-sm font-semibold text-gray-700 mb-2">
              API 설정
            </h2>
            <div className="flex gap-2 mb-3">
              {(["openai", "gemini"] as const).map((p) => (
                <button
                  key={p}
                  onClick={() => setApiProvider(p)}
                  className={`flex-1 py-1.5 rounded text-sm font-medium border transition-colors ${
                    apiProvider === p
                      ? "bg-blue-600 text-white border-blue-600"
                      : "bg-white text-gray-600 border-gray-300 hover:bg-gray-50"
                  }`}
                >
                  {p === "openai" ? "OpenAI" : "Gemini"}
                </button>
              ))}
            </div>
            <input
              type="password"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder={
                apiProvider === "openai"
                  ? "sk-... (OpenAI API Key)"
                  : "AI... (Gemini API Key)"
              }
              className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </section>

          {/* Story Text */}
          <section>
            <h2 className="text-sm font-semibold text-gray-700 mb-2">
              스토리 전문
            </h2>
            <textarea
              value={storyText}
              onChange={(e) => setStoryText(e.target.value)}
              placeholder={"SC01 — Judy loved tennis...\nSC02 — One day, Judy found..."}
              className="w-full h-48 border border-gray-300 rounded px-3 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
            />
          </section>

          {/* Core Patterns */}
          <section>
            <h2 className="text-sm font-semibold text-gray-700 mb-2">
              핵심 패턴 (Pattern Practice용)
            </h2>
            <textarea
              value={patterns}
              onChange={(e) => setPatterns(e.target.value)}
              placeholder={"You're not worried anymore.\nYou're not weak anymore.\n..."}
              className="w-full h-28 border border-gray-300 rounded px-3 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
            />
          </section>

          {/* Character Info */}
          <section>
            <h2 className="text-sm font-semibold text-gray-700 mb-2">
              캐릭터 정보
            </h2>
            <textarea
              value={characterInfo}
              onChange={(e) => setCharacterInfo(e.target.value)}
              placeholder={"이름: Judy\n나이: 9-11세\n성별: female\n성격: ..."}
              className="w-full h-24 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
            />
            <input
              type="text"
              value={coreMessage}
              onChange={(e) => setCoreMessage(e.target.value)}
              placeholder="Core Message (예: Judy learned that her strength was inside her.)"
              className="w-full mt-2 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              type="text"
              value={openingLine}
              onChange={(e) => setOpeningLine(e.target.value)}
              placeholder='Opening Line (예: Hi! I am Judy...)'
              className="w-full mt-2 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </section>

          {/* Question Types */}
          <section>
            <h2 className="text-sm font-semibold text-gray-700 mb-2">
              생성할 질문 유형
            </h2>
            <div className="flex flex-col gap-2">
              {QUESTION_TYPES.map((t) => (
                <label
                  key={t.key}
                  className="flex items-center gap-2 cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={selectedTypes.includes(t.key)}
                    onChange={() => toggleType(t.key)}
                    className="rounded border-gray-300 text-blue-600"
                  />
                  <span className="text-sm text-gray-700">{t.label}</span>
                </label>
              ))}
            </div>
          </section>

          {/* Generate Button */}
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="w-full py-2.5 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white font-medium rounded transition-colors text-sm"
          >
            {loading ? "생성 중..." : "질문 풀 생성"}
          </button>

          {error && (
            <p className="text-red-600 text-sm bg-red-50 border border-red-200 rounded p-2">
              {error}
            </p>
          )}
        </aside>

        {/* Right Panel — Output */}
        <main className="flex-1 overflow-y-auto p-6">
          {!result && !loading && (
            <div className="flex items-center justify-center h-full text-gray-400 text-sm">
              왼쪽에서 정보를 입력하고 생성 버튼을 눌러주세요.
            </div>
          )}

          {loading && (
            <div className="flex items-center justify-center h-full text-blue-500 text-sm">
              AI가 질문 풀을 생성하고 있습니다...
            </div>
          )}

          {result && (
            <div>
              {/* Character Persona */}
              <div className="bg-white border border-gray-200 rounded-lg p-5 mb-5">
                <div className="flex items-center justify-between mb-3">
                  <h2 className="text-base font-semibold text-gray-800">
                    캐릭터 페르소나
                  </h2>
                  <button
                    onClick={handleCopyAll}
                    className="text-xs text-gray-500 hover:text-gray-700 border border-gray-300 rounded px-2 py-1"
                  >
                    {copied ? "복사됨!" : "전체 JSON 복사"}
                  </button>
                </div>
                <div className="grid grid-cols-2 gap-3 text-sm">
                  <div>
                    <span className="text-gray-500">이름</span>
                    <p className="font-medium text-gray-800">
                      {result.characterPersona.name}
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">나이</span>
                    <p className="font-medium text-gray-800">
                      {result.characterPersona.age}
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">성별</span>
                    <p className="font-medium text-gray-800">
                      {result.characterPersona.gender}
                    </p>
                  </div>
                  <div className="col-span-2">
                    <span className="text-gray-500">성격</span>
                    <p className="font-medium text-gray-800">
                      {result.characterPersona.personality}
                    </p>
                  </div>
                  <div className="col-span-2">
                    <span className="text-gray-500">Core Message</span>
                    <p className="font-medium text-gray-800">
                      {result.characterPersona.coreMessage}
                    </p>
                  </div>
                  <div className="col-span-2">
                    <span className="text-gray-500">Opening Line</span>
                    <p className="font-medium text-gray-800 italic">
                      &ldquo;{result.characterPersona.openingLine}&rdquo;
                    </p>
                  </div>
                </div>
              </div>

              {/* Question Tabs */}
              <div className="bg-white border border-gray-200 rounded-lg overflow-hidden">
                <div className="flex border-b border-gray-200 overflow-x-auto">
                  {QUESTION_TYPES.filter((t) =>
                    selectedTypes.includes(t.key)
                  ).map((t) => (
                    <button
                      key={t.key}
                      onClick={() => setActiveTab(t.key)}
                      className={`px-4 py-3 text-xs font-medium whitespace-nowrap transition-colors ${
                        activeTab === t.key
                          ? "border-b-2 border-blue-600 text-blue-600"
                          : "text-gray-500 hover:text-gray-700"
                      }`}
                    >
                      {t.label}
                    </button>
                  ))}
                </div>

                <div className="p-5">
                  {activeQuestions.length === 0 ? (
                    <p className="text-gray-400 text-sm">
                      이 유형의 질문이 없습니다.
                    </p>
                  ) : (
                    <div className="flex flex-col gap-4">
                      {(activeQuestions as QuestionItem[]).map((q, i) => (
                        <div
                          key={i}
                          className="border border-gray-100 rounded-lg p-4 bg-gray-50"
                        >
                          <div className="flex items-start gap-3 mb-3">
                            <span className="flex-shrink-0 w-6 h-6 bg-blue-600 text-white text-xs rounded-full flex items-center justify-center font-bold">
                              {i + 1}
                            </span>
                            <div className="flex-1">
                              <p className="font-medium text-gray-800 text-sm">
                                {q.question}
                              </p>
                              <span className="text-xs text-gray-400 mt-0.5 block">
                                {q.relatedScene}
                              </span>
                            </div>
                          </div>

                          <div className="pl-9 flex flex-col gap-2">
                            {q.targetAnswer && (
                              <div>
                                <span className="text-xs font-medium text-gray-500 uppercase tracking-wide">
                                  Target Answer
                                </span>
                                <p className="text-sm text-green-700 mt-0.5">
                                  {q.targetAnswer}
                                </p>
                              </div>
                            )}
                            {q.targetAnswers && q.targetAnswers.length > 0 && (
                              <div>
                                <span className="text-xs font-medium text-gray-500 uppercase tracking-wide">
                                  Target Answers
                                </span>
                                <ul className="mt-0.5 flex flex-col gap-0.5">
                                  {q.targetAnswers.map((a, ai) => (
                                    <li
                                      key={ai}
                                      className="text-sm text-green-700"
                                    >
                                      • {a}
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}
                            <div>
                              <span className="text-xs font-medium text-gray-500 uppercase tracking-wide">
                                채점 기준
                              </span>
                              <p className="text-sm text-gray-600 mt-0.5">
                                {q.acceptableCriteria}
                              </p>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
