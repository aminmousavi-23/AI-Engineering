import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(
            f"{func.__name__} completed "
            f"in {elapsed:.4f} seconds"
        )

        return result

    return wrapper

@measure_time
def generate_embedding(text: str) -> list[float]:
    # Simulate embedding generation
    time.sleep(0.5)

    return [0.12, -0.45, 0.78]


@measure_time
def generate_answer(prompt: str) -> str:
    # Simulate LLM generation
    time.sleep(1)

    return "AI generated answer"


embedding = generate_embedding(
    "Python is useful for AI"
)

answer = generate_answer(
    "Explain RAG"
)