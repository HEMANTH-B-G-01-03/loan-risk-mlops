# 🚀 Loan Risk Prediction MLOps Pipeline

## 📌 Project Overview

This project is a **production-grade End-to-End MLOps and DevOps pipeline** developed for predicting loan default risk using Machine Learning and modern MLOps practices.

The system automates the complete machine learning lifecycle including:

- Data Ingestion
- Data Preprocessing
- Model Training
- Model Evaluation
- Experiment Tracking
- Data & Model Versioning
- REST API Deployment
- Docker Containerization
- CI/CD Automation
- Monitoring & Drift Detection
- DevSecOps Security Integration

The project is designed to simulate how real-world AI systems are built and deployed in production environments.

---

# 🎯 Objective

The objective of this project is to build an intelligent loan risk prediction system that can determine whether a customer is likely to default on a loan based on financial and personal attributes.

The project also demonstrates:
- Reproducible ML workflows
- Automated CI/CD pipelines
- Secure deployment practices
- Monitoring and drift detection
- Industry-standard MLOps lifecycle implementation

---

# 🧠 Problem Statement

Financial institutions face significant risks while approving loans. Manual risk assessment is often time-consuming and inconsistent.

This project uses Machine Learning to automate loan risk prediction by analyzing customer-related information such as:
- Loan amount
- Income
- Credit history
- Interest rate
- Employment details
- Debt-to-income ratio
- Loan status history

The system predicts:
- ✅ Safe Customer
- ❌ Potential Defaulter

---

# 🏗️ System Architecture

```text
Dataset
   ↓
Data Validation
   ↓
Preprocessing Pipeline
   ↓
Model Training
   ↓
Model Evaluation
   ↓
MLflow Experiment Tracking
   ↓
DVC Data & Model Versioning
   ↓
FastAPI REST API
   ↓
Docker Containerization
   ↓
CI/CD Pipeline
   ↓
Deployment
   ↓
Monitoring & Drift Detection
   ↓
Security Validation
```

---

# 📂 Project Structure

```text
loan-risk-mlops/
│
├── .dvc/                      # DVC configuration
├── .github/                   # GitHub Actions workflows
│   └── workflows/
│
├── data/
│   ├── raw/                   # Raw datasets
│   └── processed/             # Processed datasets
│
├── models/                    # Trained ML models
├── notebooks/                 # Jupyter notebooks
├── reports/                   # Reports and metrics
│
├── src/
│   ├── preprocess.py          # Data preprocessing pipeline
│   ├── train.py               # Model training
│   ├── evaluate.py            # Model evaluation
│   ├── predict.py             # Prediction logic
│   └── app.py                 # FastAPI application
│
├── tests/                     # Unit tests
│
├── Dockerfile                 # Docker configuration
├── dvc.yaml                   # DVC pipeline
├── params.yaml                # Hyperparameters
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore
```

---

# 📊 Dataset Information

## Dataset Used
**Lending Club Loan Dataset**

Dataset Link:  
https://www.kaggle.com/datasets/wordsforthewise/lending-club

### Dataset Features
- Loan Amount
- Annual Income
- Interest Rate
- Credit Score
- Employment Length
- Debt-to-Income Ratio
- Loan Status
- Home Ownership
- Purpose of Loan

### Dataset Size
- Large-scale real-world financial dataset
- ~1.5GB data
- Millions of loan records

---

# ⚙️ Technologies Used

## Programming
- Python

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## MLOps Tools
- DVC
- MLflow

## API Development
- FastAPI

## Containerization
- Docker

## CI/CD
- GitHub Actions

## Monitoring
- Prometheus
- Grafana

## Drift Detection
- Evidently AI

## Testing
- Pytest
- Flake8

---

# 🔄 MLOps Workflow

## 1️⃣ Data Versioning using DVC
DVC is used to:
- Track large datasets
- Version ML artifacts
- Ensure reproducibility

---

## 2️⃣ Experiment Tracking using MLflow
MLflow tracks:
- Hyperparameters
- Metrics
- Models
- Training experiments

---

## 3️⃣ Modular ML Pipeline
The pipeline is divided into reusable modules:
- Preprocessing
- Training
- Evaluation
- Prediction

---

## 4️⃣ API Deployment
The trained model is deployed using FastAPI with REST endpoints for predictions.

---

## 5️⃣ Dockerized Deployment
The application is containerized using Docker for:
- Portability
- Consistency
- Scalability

---

## 6️⃣ CI/CD Automation
GitHub Actions automates:
- Testing
- Linting
- Pipeline execution
- Docker builds

---

## 7️⃣ Monitoring & Drift Detection
The system monitors:
- API metrics
- Request performance
- Data drift
- Model behavior

---

# 🔐 DevSecOps Features

The project follows secure deployment practices:
- Environment variable protection
- GitHub Secrets
- Docker image vulnerability scanning
- Secure configuration management

---

# 🚀 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/loan-risk-mlops.git
cd loan-risk-mlops
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 DVC Setup

Initialize DVC:

```bash
dvc init
```

Track dataset:

```bash
dvc add data/raw/accepted_2007_to_2018Q4.csv
```

---

# 🧪 Running the Pipeline

## Preprocessing

```bash
python src/preprocess.py
```

## Training

```bash
python src/train.py
```

## Evaluation

```bash
python src/evaluate.py
```

---

# 🌐 Run FastAPI Server

```bash
uvicorn src.app:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

# 🐳 Docker Commands

## Build Docker Image

```bash
docker build -t loan-risk-mlops .
```

## Run Docker Container

```bash
docker run -p 8000:8000 loan-risk-mlops
```

---

# 📈 Future Enhancements

- Kubernetes Deployment
- Automated Retraining
- Cloud Deployment (AWS/GCP)
- Explainable AI Integration
- Real-Time Dashboard
- Streamlit Frontend
- Advanced Drift Detection

---

# 📚 Learning Outcomes

This project demonstrates:
- End-to-End MLOps lifecycle
- Production-ready ML deployment
- CI/CD integration
- Data reproducibility
- Monitoring & observability
- DevSecOps practices

---

# 👨‍💻 Author

**Hemanth B G**  
M.Tech CSE Student  
BMS College of Engineering
Banglore, Karnataka

---

# 📄 License

This project is licensed under the MIT License.