# ------------------------------------------------------
# Unique Labels
# ------------------------------------------------------
labels = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "car",
    "bird",
]

hash_set = set()

for label in labels:
    if (label not in hash_set):
        hash_set.add(label)

print(hash_set)
print("cat" in labels)