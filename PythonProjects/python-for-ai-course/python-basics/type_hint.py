from typing import TypedDict


class ModelResponse(TypedDict):
    answer: str
    tokens_used: int
    confidence: float


def generate_answer(prompt: str, temperature: float = 0.7) -> ModelResponse:

    # Simulate an AI model response
    answer = f"AI response to: {prompt}"

    return {"answer": answer, "tokens_used": 128, "confidence": 0.94}


response: ModelResponse = generate_answer(
    prompt="Explain machine learning in simple terms", temperature=0.5
)

print(response["answer"])
print(f"Tokens: {response['tokens_used']}")
print(f"Confidence: {response['confidence']}")
