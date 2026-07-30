import pandas as pd

print("========== Day 5 - Data Cleaning ==========")

df = pd.read_csv("student_scores.csv")

print("\nOriginal Dataset")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

print("\nDataset After Handling Missing Values")
print(df)

df = df.drop_duplicates()

print("\nDataset After Removing Duplicates")
print(df)

print("\nDataset Statistics")
print(df.describe())

print("\nClean Dataset")
print(df)

df.to_csv("clean_student_scores.csv", index=False)

print("\nClean dataset saved as 'clean_student_scores.csv'")