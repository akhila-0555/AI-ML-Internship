import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
print("========== Day 11 - Student Score Prediction App ==========")
df = pd.read_csv("clean_student_scores.csv")
X = df[["Study_Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
study_hours = float(input("Enter Study Hours: "))
user_input = pd.DataFrame({"Study_Hours": [study_hours]})
predicted_score = model.predict(user_input)
print("\nPrediction Result")
print("Study Hours:", study_hours)
print("Predicted Score:", round(predicted_score[0], 2))
print("\nDay 11 Task Completed Successfully")