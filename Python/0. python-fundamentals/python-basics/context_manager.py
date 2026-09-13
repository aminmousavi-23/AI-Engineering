import time
from contextlib import contextmanager


@contextmanager
def ai_inference_session(model_name: str):
    """
    Context manager for managing an AI inference session.

    Handles:
    - Resource initialization
    - Inference execution
    - Cleanup
    - Exception handling
    """

    print(f"[START] Loading model: {model_name}")

    start_time = time.perf_counter()

    try:
        # This is the beginning of the context.
        # Resources can be initialized here.
        model = {"name": model_name, "status": "loaded"}

        yield model

    except Exception as error:
        print(f"[ERROR] Inference failed: {error}")
        raise

    finally:
        # This code always runs,
        # even if an exception occurs.
        elapsed = time.perf_counter() - start_time

        model["status"] = "released"

        print(f"[CLEANUP] Model '{model_name}' released after {elapsed:.4f}s")


# ------------------------------------------------------------
# Using the Context Manager
# ------------------------------------------------------------

with ai_inference_session("my-local-llm") as model:
    print(f"Model status: {model['status']}")

    prompt = "Explain RAG in simple terms"

    print(f"Generating answer for: {prompt}")

    answer = "RAG combines retrieval with generation."

    print(f"Answer: {answer}")


print("Session finished.")


# ------------------------------------------------------------
# Practice
# ------------------------------------------------------------


class AIClientSession:

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.is_active = False
        self.start_time = None

    def __enter__(self):
        self.is_active = True
        self.start_time = time.perf_counter()
        return self

    def generate(self, message: str) -> str:
        return "This is a test answer to the message: " + message

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start_time
        self.is_active = False
        print(f"Session closed after {elapsed:.4f}s")
        return True

with AIClientSession("my-local-llm") as session:
    result = session.generate("Hello, how are you?")
    print(result)