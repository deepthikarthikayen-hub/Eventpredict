# EventPredict

## Overview

EventPredict is a Machine Learning and Generative AI application developed as part of the ABB Mini Project.

The application predicts event attendance using a Linear Regression model and provides AI-powered event planning suggestions using Google Gemini.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Google Gemini API

---

## Features

- Predicts expected event attendance.
- Accepts event details through a Streamlit interface.
- Uses Linear Regression for prediction.
- Generates AI recommendations using Google Gemini.

---

## Project Files

| File | Description |
|------|-------------|
| app.py | Streamlit application |
| dataset.py | Creates the synthetic dataset |
| train_model.py | Trains the Linear Regression model |
| gemini.py | Generates AI suggestions |
| dataset.csv | Historical dataset |
| attendance_model.pkl | Trained ML model |
| label_encoders.pkl | Saved label encoders |
| requirements.txt | Python dependencies |

---

## How to Run

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Workflow

1. Enter event details.
2. Predict attendance using Linear Regression.
3. Send prediction and event details to Gemini.
4. Display AI-generated suggestions.

---

## Author

Deepthi Karthikayen