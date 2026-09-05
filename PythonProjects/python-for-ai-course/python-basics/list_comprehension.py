
documents = [
    "  Python is great for AI  ",
    "Machine Learning is powerful ",
    "  Deep Learning is interesting",
    "AI"
]

# Clean and filter documents : [expression for item in iterable if condition]
processed_documents = [
    document.strip()
    for document in documents
    if len(document.strip()) >= 10
]

print(processed_documents[1])