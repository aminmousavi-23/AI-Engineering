class OpenAIModel:
    def generate(self, prompt: str) -> str:
        return f"OpenAI response: {prompt}"


class LocalModel:
    def generate(self, prompt: str) -> str:
        return f"Local model response: {prompt}"


def ask_model(model, prompt: str) -> str:
    # We don't care about the actual type of model.
    # We only care that it has a generate() method.
    return model.generate(prompt)


openai_model = OpenAIModel()
local_model = LocalModel()

print(ask_model(openai_model, "Explain machine learning"))

print(ask_model(local_model, "Explain machine learning"))
