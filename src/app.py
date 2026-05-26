from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import joblib
import numpy as np

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

MODEL_PATH = "models/loan_risk_model.pkl"

print("Loading trained model...")

model = joblib.load(MODEL_PATH)

print("Model loaded successfully")

# -----------------------------------
# FASTAPI APP
# -----------------------------------

app = FastAPI(
    title="Loan Risk Prediction API",
    description="MLOps-based Loan Default Risk Prediction System",
    version="1.0"
)

# -----------------------------------
# ENABLE CORS
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# INPUT SCHEMA
# -----------------------------------

class LoanData(BaseModel):

    loan_amnt: float
    term: int
    int_rate: float
    installment: float
    grade: int
    sub_grade: int
    emp_length: int
    home_ownership: int
    annual_inc: float
    verification_status: int
    purpose: int
    dti: float
    delinq_2yrs: int
    fico_range_low: int
    inq_last_6mths: int
    open_acc: int
    pub_rec: int
    revol_bal: float
    revol_util: float
    total_acc: int
    application_type: int

# -----------------------------------
# HOME ROUTE
# -----------------------------------

@app.get("/")
def home():

    return {
        "message": "Loan Risk Prediction API is Running Successfully"
    }

# -----------------------------------
# PREDICTION ROUTE
# -----------------------------------

@app.post("/predict")
def predict(data: LoanData):

    # Convert input to numpy array
    input_data = np.array([[
        data.loan_amnt,
        data.term,
        data.int_rate,
        data.installment,
        data.grade,
        data.sub_grade,
        data.emp_length,
        data.home_ownership,
        data.annual_inc,
        data.verification_status,
        data.purpose,
        data.dti,
        data.delinq_2yrs,
        data.fico_range_low,
        data.inq_last_6mths,
        data.open_acc,
        data.pub_rec,
        data.revol_bal,
        data.revol_util,
        data.total_acc,
        data.application_type
    ]])

    # Prediction
    # Probability
    probability = model.predict_proba(input_data)[0][1]

# Custom threshold
    threshold = 0.35

    prediction = 1 if probability > threshold else 0

    # Probability
    probability = model.predict_proba(input_data)[0][1]

    # Risk Label
    risk_label = (
        "High Risk Customer"
        if prediction == 1
        else "Safe Customer"
    )

    return {
        "prediction": int(prediction),
        "risk_label": risk_label,
        "default_probability": round(float(probability), 4)
    }