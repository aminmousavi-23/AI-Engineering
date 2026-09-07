# ============================================================
# Iterator
# ============================================================

class DocumentIterator:

    def __init__(self, documents):
        self.documents = documents
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.documents):
            raise StopIteration

        document = self.documents[self.index]

        self.index += 1

        return document


# AI / RAG example

documents = [
    "Python is useful for AI",
    "RAG uses retrieval",
    "Transformers use attention",
]

documents_iterator = DocumentIterator(documents)


for document in documents_iterator:
    print(document)