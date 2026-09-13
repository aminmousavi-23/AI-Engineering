# ============================================================
# Lambda
# ============================================================

# A lambda is a small anonymous function.
# Syntax:
# lambda arguments: expression


# Simple example
square = lambda x: x ** 2

print(square(5))


# Multiple arguments
add = lambda a, b: a + b

print(add(10, 20))


# AI / RAG example
results = [
    {"text": "Python is a programming language", "score": 0.72},
    {"text": "RAG uses retrieval", "score": 0.94},
    {"text": "Transformers use attention", "score": 0.87},
]

# Sort search results by similarity score
results = sorted(
    results,
    key=lambda result: result["score"],
    reverse=True
)

for result in results:
    print(result["score"], result["text"])


# Extract document texts
texts = [result["text"] for result in results]

print(texts)


# ------------------------------------------------------------
# Practice
# ------------------------------------------------------------

search_results = [
    {
        "id": 1,
        "text": "Python is widely used in AI engineering.",
        "score": 0.72,
        "metadata": {"source": "python.pdf"}
    },
    {
        "id": 2,
        "text": "RAG combines retrieval with generation.",
        "score": 0.95,
        "metadata": {"source": "rag.pdf"}
    },
    {
        "id": 3,
        "text": "Transformers use attention mechanisms.",
        "score": 0.88,
        "metadata": {"source": "transformers.pdf"}
    },
    {
        "id": 4,
        "text": "Python lists can store multiple values.",
        "score": 0.61,
        "metadata": {"source": "python-basics.pdf"}
    },
    {
        "id": 5,
        "text": "Embeddings represent text as vectors.",
        "score": 0.91,
        "metadata": {"source": "embeddings.pdf"}
    }
]

def return_prepared_context(results, min_score=0.80):
    result = [result for result in results if result["score"] >= min_score]

    sorted_results = sorted(result, key=lambda x: x["score"], reverse=True)

    texts = [result["text"] for result in sorted_results]

    for text in texts:
        print(text)

return_prepared_context(search_results)