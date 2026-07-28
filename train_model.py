
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("dataset.csv")
baseline_prediction = df["actual_attendance"].mean()
print("Baseline Prediction:", round(baseline_prediction, 2))
#data preprocessing- cleaning and selection
print(df.head())
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)
event_encoder = LabelEncoder()
day_encoder = LabelEncoder()
df["event_type"] = event_encoder.fit_transform(df["event_type"])
df["day_of_week"] = day_encoder.fit_transform(df["day_of_week"])
X = df.drop("actual_attendance", axis=1)
y = df["actual_attendance"]
#model training using linear regression model
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()

model.fit(X_train, y_train)
predictions=model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)
print("Linear Regression Model trained successfully.")
joblib.dump(model, "attendance_model.pkl")
joblib.dump(event_encoder, "event_encoder.pkl")
joblib.dump(day_encoder, "day_encoder.pkl")
#to show prediction comparission to evaluate the performance
comparison = pd.DataFrame({
    "Actual Attendance": y_test.values,
    "Predicted Attendance": predictions
})

print(comparison.head())