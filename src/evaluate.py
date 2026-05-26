import pandas as pd
import yaml
import joblib
import os

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# -----------------------------------
# LOAD PARAMETERS
# -----------------------------------

with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

PROCESSED_DATA_DIR = params["data"]["processed_data_dir"]

MODEL_DIR = params["model"]["model_dir"]
MODEL_FILE = params["model"]["model_file"]

# -----------------------------------
# LOAD TEST DATA
# -----------------------------------

print("Loading test datasets...")

X_test = pd.read_csv(
    f"{PROCESSED_DATA_DIR}/X_test.csv"
)

y_test = pd.read_csv(
    f"{PROCESSED_DATA_DIR}/y_test.csv"
).squeeze()

print("Test datasets loaded successfully")

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

model_path = f"{MODEL_DIR}/{MODEL_FILE}"

print(f"Loading model from: {model_path}")

model = joblib.load(model_path)

print("Model loaded successfully")

# -----------------------------------
# MAKE PREDICTIONS
# -----------------------------------

print("Making predictions...")

y_pred = model.predict(X_test)

# -----------------------------------
# CALCULATE METRICS
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

# -----------------------------------
# PRINT RESULTS
# -----------------------------------

print("\nModel Evaluation Metrics")
print("-" * 40)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

# -----------------------------------
# CLASSIFICATION REPORT
# -----------------------------------

report = classification_report(
    y_test,
    y_pred,
    zero_division=0
)

print("\nClassification Report")
print(report)

# -----------------------------------
# CONFUSION MATRIX
# -----------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

# -----------------------------------
# SAVE REPORT
# -----------------------------------

os.makedirs("reports", exist_ok=True)

with open("reports/model_evaluation.txt", "w") as f:

    f.write("Loan Risk Prediction Model Evaluation\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Accuracy  : {accuracy:.4f}\n")
    f.write(f"Precision : {precision:.4f}\n")
    f.write(f"Recall    : {recall:.4f}\n")
    f.write(f"F1 Score  : {f1:.4f}\n\n")

    f.write("Classification Report\n")
    f.write("-" * 40 + "\n")

    f.write(report)

    f.write("\n\nConfusion Matrix\n")
    f.write(str(cm))

print("\nEvaluation report saved successfully")

print("\nEvaluation Pipeline Completed Successfully")