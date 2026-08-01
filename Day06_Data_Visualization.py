import pandas as pd
import matplotlib.pyplot as plt

print("========== Day 6 - Data Visualization ==========")

df = pd.read_csv("student_scores.csv")

print("\nStudent Score Dataset")
print(df)

plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Score"])
plt.title("Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df["Student"], df["Score"])
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,4))
plt.plot(df["Study_Hours"], df["Score"], marker="o")
plt.title("Line Chart")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()

print("\nData Visualization Completed Successfully")