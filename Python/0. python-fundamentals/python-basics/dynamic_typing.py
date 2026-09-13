class OpenAIModel:
    def generate(self, prompt: str) -> str:
        return "OpenAI response"


class LocalModel:
    def generate(self, prompt: str) -> str:
        return "Local model response"


model = OpenAIModel()

print(model.generate("Explain RAG"))

# Python allows the same variable
# to reference an object of another type.
model = LocalModel()

print(model.generate("Explain RAG"))