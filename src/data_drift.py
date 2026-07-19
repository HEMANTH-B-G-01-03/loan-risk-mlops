import os
import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.read_csv("data/processed/X_train.csv")
current_data = pd.read_csv("data/processed/X_test.csv")

report = Report([
    DataDriftPreset()
])

# IMPORTANT: capture the return value
my_eval = report.run(reference_data, current_data)

os.makedirs("reports", exist_ok=True)

# Save HTML
my_eval.save_html("reports/data_drift_report.html")

print("Done!")