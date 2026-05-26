import pandas as pd
import yaml
import os
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# -----------------------------------
# LOAD PARAMETERS
# -----------------------------------

with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

PROCESSED_DATA_DIR = params["data"]["processed_data_dir"]

MODEL_DIR = params["model"]["model_dir"]
MODEL_FILE = params["model"]["model_file"]

N_ESTIMATORS = params["training"]["n_estimators"]
MAX_DEPTH = params["training"]["max_depth"]
MIN_SAMPLES_SPLIT = params["training"]["min_samples_split"]
RANDOM_STATE = params["preprocessing"]["random_state"]

# -----------------------------------
# CREATE MODEL DIRECTORY
# -----------------------------------

os.makedirs(MODEL_DIR, exist_ok=True)

# -----------------------------------
# LOAD DATASETS
# -----------------------------------

print("Loading processed datasets...")

X_train = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_train.csv")
X_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_test.csv")

y_train = pd.read_csv(f"{PROCESSED_DATA_DIR}/y_train.csv").squeeze()
y_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/y_test.csv").squeeze()

print("Datasets loaded successfully")

# -----------------------------------
# INITIALIZE MLFLOW
# -----------------------------------

mlflow.set_experiment("Loan_Risk_Prediction")

# -----------------------------------
# START MLFLOW RUN
# -----------------------------------

with mlflow.start_run():

    print("Training Random Forest Model...")

    # Initialize model
    model = RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        max_depth=MAX_DEPTH,
        min_samples_split=MIN_SAMPLES_SPLIT,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    # Train model
    model.fit(X_train, y_train)

    print("Model training completed")

    # Predictions
    y_pred = model.predict(X_test)

    # -----------------------------------
    # EVALUATION METRICS
    # -----------------------------------

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\nModel Performance Metrics")
    print("-" * 40)

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    # -----------------------------------
    # LOG PARAMETERS TO MLFLOW
    # -----------------------------------

    mlflow.log_param("n_estimators", N_ESTIMATORS)
    mlflow.log_param("max_depth", MAX_DEPTH)
    mlflow.log_param("min_samples_split", MIN_SAMPLES_SPLIT)

    # -----------------------------------
    # LOG METRICS TO MLFLOW
    # -----------------------------------

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)

    # -----------------------------------
    # SAVE MODEL
    # -----------------------------------

    model_path = f"{MODEL_DIR}/{MODEL_FILE}"

    joblib.dump(model, model_path)

    print(f"\nModel saved at: {model_path}")

    # -----------------------------------
    # LOG MODEL TO MLFLOW
    # -----------------------------------

    mlflow.sklearn.log_model(model, "random_forest_model")

    print("\nMLflow logging completed")

print("\nTraining Pipeline Completed Successfully")