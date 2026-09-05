def read_documents(file_path: str):
    """
    Lazily read documents from a file.
    One document is produced at a time.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            document = line.strip()

            if document:
                yield document


# Documents are processed one by one
for document in read_documents("data/documents.txt"):
    print(document)