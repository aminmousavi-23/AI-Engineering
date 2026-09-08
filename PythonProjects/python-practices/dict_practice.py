# ------------------------------------------------------
# Model Configuration
# ------------------------------------------------------
model_config = {
    "model_name": "classification_model",
    "learning_rate": 0.001,
    "epochs": 20,
    "batch_size": 32,
}

model_config["learning_rate"] = 0.002
model_config["is_optimized"] = True
model_config.pop("epochs")

print(model_config["model_name"])
print(model_config["learning_rate"])
print(model_config["is_optimized"])
print("batch_size" in model_config)

for k,v in model_config.items():
    print(f"{k} : {v}")

# ------------------------------------------------------
# Training Metrics
# ------------------------------------------------------
metrics = {
    "accuracy": 0.91,
    "precision": 0.87,
    "recall": 0.84,
    "f1_score": 0.85,
}

def get_best_metric(metrics):
    max_key = ""
    max_value = 0

    for k,v in metrics.items():
        if (v > max_value):
            max_value = v
            max_key = k

    print(max_key)

def get_metrics_above(metrics, threshold):
    for k,v in metrics.items():
        if (v >= threshold):
            print(f"{k} : {v}")


get_best_metric(metrics)
get_metrics_above(metrics, 0.85)

# ------------------------------------------------------
# Dataset Sample
# ------------------------------------------------------
sample = {
    "id": 101,
    "age": 25,
    "height": 183,
    "weight": 82,
    "label": "healthy",
}

bmi = sample["weight"] / ((sample["height"] / 100) ** 2)
sample["bmi"] = bmi

print(sample)

# ------------------------------------------------------
# Prediction Result
# ------------------------------------------------------
predictions = {
    101: 0.91,
    102: 0.32,
    103: 0.76,
    104: 0.48,
    105: 0.88,
}

threshold = 0.7

predictions_sign = {}
for k,v in predictions.items():
    if (v > threshold):
        predictions_sign[k] = "positive"
    else:
        predictions_sign[k] = "negative"

print(predictions_sign)

# ------------------------------------------------------
# Nested Dict
# ------------------------------------------------------
experiment = {
    "model": {
        "name": "classifier",
        "version": "1.0",
    },
    "training": {
        "epochs": 20,
        "batch_size": 32,
        "learning_rate": 0.001,
    },
    "metrics": {
        "accuracy": 0.92,
        "f1": 0.89,
    }
}

def get_model_name(experiment):
    print(experiment["model"]["name"])

def get_learning_rate(experiment):
    print(experiment["training"]["learning_rate"])

def get_best_metric(experiment):
    best_metric = 0
    for k,v in experiment["metrics"].items():
        if (v > best_metric):
            best_metric = v
    print(best_metric)

def update_learning_rate(experiment, new_rate):
    experiment["training"]["learning_rate"] = new_rate

def summarize_experiment(experiment):
    summarized_experiment = {}
    summarized_experiment["model"] = experiment["model"]["name"]
    summarized_experiment["learning_rate"] = experiment["training"]["learning_rate"]
    summarized_experiment["accuracy"] = experiment["metrics"]["accuracy"]
    summarized_experiment["f1"] = experiment["metrics"]["f1"]

    print(summarized_experiment)

get_model_name(experiment)
get_learning_rate(experiment)
get_best_metric(experiment)
update_learning_rate(experiment, 0.002)

summarize_experiment(experiment)