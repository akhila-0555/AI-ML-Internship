import pandas as pd

print("========== Day 4 - Pandas ==========")

df = pd.read_csv("student_scores.csv")

print("\nStudent Score Dataset")
print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nRows and Columns")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())