import pandas as pd
import os

# Load CSV from same folder as script
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "titanic.csv")
data = pd.read_csv(csv_path)

# First rows
print("First 5 rows:")
print(data.head())

# Dataset info
print("\nDataset Info:")
print(data.info())

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Survival count (FIXED)
print("\nSurvival Count:")
print(data["survived"].value_counts())

# Survival percentage
print("\nSurvival Percentage:")
print(data["survived"].value_counts(normalize=True) * 100)
