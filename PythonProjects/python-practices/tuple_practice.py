# ------------------------------------------------------
# Model Input
# ------------------------------------------------------
features = (0.72, 1.4, 0.33, 0.91)

print(features[2])
print(features[0])
print(features[-1])
print(0.91 in features)

count = 0
for feature in features:
    count += 1

print(count)

# ------------------------------------------------------
# Dataset Metadata
# ------------------------------------------------------
dataset_info = (
    "MNIST",
    60000,
    784,
    10,
)

def describe_dataset(dataset_info):
    named_dataset = {}

    named_dataset["Dataset"] = dataset_info[0]
    named_dataset["Samples"] = dataset_info[1]
    named_dataset["Features"] = dataset_info[2]
    named_dataset["Classes"] = dataset_info[3]

    for k,v in named_dataset.items():
        print(f"{k}: {v}")

describe_dataset(dataset_info)

# ------------------------------------------------------
# Multiple Return Values
# ------------------------------------------------------
def calculate_statistics(values):
    minimum = values[0]
    maximum = values[0]
    total = 0
    count = 0

    for v in values:
        if(v < minimum):
            minimum = v

        elif(v > maximum):
            maximum = v

        count += 1
        total += v

    return(minimum, maximum, total/count)



minimum, maximum, average = calculate_statistics([10, 20, 30, 40])
print(minimum)
print(maximum)
print(average)

# ------------------------------------------------------
# Tuple as Dataset Record
# ------------------------------------------------------
dataset = [
    ("image_001.jpg", 0),
    ("image_002.jpg", 1),
    ("image_003.jpg", 0),
    ("image_004.jpg", 1),
    ("image_005.jpg", 1),
]


def count_labels(dataset):
    label_counts = {}

    for image_path, label in dataset:
        if label not in label_counts:
            label_counts[label] = 0

        label_counts[label] += 1

    return label_counts


result = count_labels(dataset)

print(result)