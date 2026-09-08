# ------------------------------------------------------
# Dataset Samples
# ------------------------------------------------------
samples = [
    12.5,
    15.2,
    8.7,
    19.3,
    22.1,
    17.8,
    9.4,
    25.6,
]

count = 0
total = 0
min_value = samples[0]
max_value = samples[0]

greater_than_average_samples = []

for sample in samples:
    count += 1
    total += sample

    if sample > max_value:
        max_value = sample

    if sample < min_value:
        min_value = sample

for sample in samples:
    if(sample > (total / count)):
        greater_than_average_samples.append(sample)

print(count)
print(total)
print(total / count)
print(min_value)
print(max_value)
print(greater_than_average_samples)
print(samples)

# ------------------------------------------------------
# Feature Vector
# ------------------------------------------------------
features = [0.72, 1.4, 0.33, 0.91, 2.7]
i = 0

for feature in features:
    i += 1
    print(f"Feature {i} -> {feature}")

features[0] = 0.28
print(features)

features.pop()
print(features)

features.append(3.98)
print(features)

first_feature = features[0]

features[0] = features[1]
features[1] = first_feature
print(features)

# ------------------------------------------------------
# Prediction Results
# ------------------------------------------------------
predictions = [
    0.91,
    0.34,
    0.78,
    0.12,
    0.66,
    0.83,
    0.41,
    0.95,
]

threshold = 0.7

predictions_sign = []

for prediction in predictions:
    if(prediction - threshold > 0):
        predictions_sign.append("positive")
    elif(prediction - threshold < 0):
        predictions_sign.append("negative")
    else:
        predictions_sign.append("zero")

for sign in predictions_sign:
    print(sign)

# ------------------------------------------------------
# Data Cleaning
# ------------------------------------------------------
data = [
    12,
    None,
    15,
    -3,
    18,
    None,
    0,
    21,
    -7,
    16,
]

cleaned_data = []

removed_data_count = 0
cleaned_data_count = 0

for i in data:
    if(i == None):
        removed_data_count += 1
        continue
    if(i < 0):
        removed_data_count += 1
        continue

    cleaned_data.append(i)

total = 0
for c in cleaned_data:
    total += c
    cleaned_data_count += 1

print(removed_data_count)
print(cleaned_data)
print(total / cleaned_data_count)

# ------------------------------------------------------
# Batch Processing
# ------------------------------------------------------
samples = [
    "image_001",
    "image_002",
    "image_003",
    "image_004",
    "image_005",
    "image_006",
    "image_007",
    "image_008",
    "image_009",
    "image_010",
]

batch_size = 3

def create_batches(samples, batch_size):
    batched_list = []
    batch = []
    processed_batch = 0

    for sample in samples:
        if processed_batch < batch_size:
            batch.append(sample)
            processed_batch += 1
        else:
            batched_list.append(batch)

            batch = [sample]
            processed_batch = 1

    if batch:
        batched_list.append(batch)

    return batched_list


batched_data = create_batches(samples, batch_size)

for batch in batched_data:
    print(batch)