import pandas as pd
import numpy as np
import yaml
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# -----------------------------------
# LOAD PARAMETERS FROM params.yaml
# -----------------------------------

with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

RAW_DATA_PATH = params["data"]["raw_data_path"]
PROCESSED_DATA_DIR = params["data"]["processed_data_dir"]

SAMPLE_SIZE = params["data"]["sample_size"]

TEST_SIZE = params["preprocessing"]["test_size"]
RANDOM_STATE = params["preprocessing"]["random_state"]

# -----------------------------------
# CREATE OUTPUT DIRECTORY
# -----------------------------------

os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# -----------------------------------
# LOAD DATASET
# -----------------------------------

print("Loading dataset...")

df = pd.read_csv(
    RAW_DATA_PATH,
    low_memory=False
)

print(f"Original Dataset Shape: {df.shape}")

# -----------------------------------
# SAMPLE DATA
# -----------------------------------

print(f"Sampling {SAMPLE_SIZE} rows...")

df = df.sample(
    n=SAMPLE_SIZE,
    random_state=RANDOM_STATE
)

print(f"Sampled Dataset Shape: {df.shape}")

# -----------------------------------
# SELECT IMPORTANT FEATURES
# -----------------------------------

selected_columns = [
    'loan_amnt',
    'term',
    'int_rate',
    'installment',
    'grade',
    'sub_grade',
    'emp_length',
    'home_ownership',
    'annual_inc',
    'verification_status',
    'purpose',
    'dti',
    'delinq_2yrs',
    'fico_range_low',
    'inq_last_6mths',
    'open_acc',
    'pub_rec',
    'revol_bal',
    'revol_util',
    'total_acc',
    'application_type',
    'loan_status'
]

df = df[selected_columns]

print("Important features selected")

# -----------------------------------
# CREATE TARGET VARIABLE
# -----------------------------------

print("Creating target variable...")

def classify_loan_status(status):

    bad_status = [
        'Charged Off',
        'Default',
        'Late (31-120 days)',
        'Late (16-30 days)'
    ]

    if status in bad_status:
        return 1
    else:
        return 0

df['target'] = df['loan_status'].apply(classify_loan_status)

# Remove original target column
df.drop('loan_status', axis=1, inplace=True)

print("Target variable created successfully")

# -----------------------------------
# HANDLE MISSING VALUES
# -----------------------------------

print("Handling missing values...")

# Numerical columns
numerical_cols = df.select_dtypes(include=np.number).columns

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns
categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values handled")

# -----------------------------------
# ENCODE CATEGORICAL COLUMNS
# -----------------------------------

print("Encoding categorical columns...")

encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

print("Encoding completed")

# -----------------------------------
# SPLIT FEATURES & TARGET
# -----------------------------------

X = df.drop('target', axis=1)
y = df['target']

# -----------------------------------
# TRAIN TEST SPLIT
# -----------------------------------

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)

print(f"X_train Shape: {X_train.shape}")
print(f"X_test Shape: {X_test.shape}")

# -----------------------------------
# SAVE PROCESSED DATA
# -----------------------------------

print("Saving processed datasets...")

X_train.to_csv(
    f"{PROCESSED_DATA_DIR}/X_train.csv",
    index=False
)

X_test.to_csv(
    f"{PROCESSED_DATA_DIR}/X_test.csv",
    index=False
)

y_train.to_csv(
    f"{PROCESSED_DATA_DIR}/y_train.csv",
    index=False
)

y_test.to_csv(
    f"{PROCESSED_DATA_DIR}/y_test.csv",
    index=False
)

print("Processed datasets saved successfully")

print("Preprocessing Pipeline Completed Successfully")