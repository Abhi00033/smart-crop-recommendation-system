# 🌾 Smart Crop Recommendation System

## Project Overview

The Smart Crop Recommendation System is a Machine Learning-based application that recommends the most suitable crop based on soil nutrients and environmental conditions.

The system helps farmers and agricultural stakeholders make better crop selection decisions by analyzing:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

The model predicts the most suitable crop and also provides the top 3 crop recommendations with confidence scores.

---

## Problem Statement

Farmers often face challenges in selecting the right crop due to varying soil conditions, rainfall patterns, and climate changes.

Incorrect crop selection can lead to:

- Reduced crop yield
- Financial losses
- Poor resource utilization

This project aims to assist in selecting the most appropriate crop using Machine Learning.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Pickle

---

## Machine Learning Workflow

### 1. Data Collection

Datasets Used:

- Crop Recommendation Dataset
- Indian Rainfall Dataset

### 2. Data Preprocessing

- Data inspection
- Missing value analysis
- Statistical analysis

### 3. Exploratory Data Analysis (EDA)

Performed:

- Crop Distribution Analysis
- Correlation Heatmap
- Temperature Distribution
- Rainfall Distribution
- pH Distribution
- Outlier Detection using Boxplots

### 4. Model Training

Models Trained:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

### 5. Model Evaluation

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 98.18%   |
| Decision Tree       | 97.95%   |
| Random Forest       | 99.55%   |
| SVM                 | 98.41%   |

Selected Model:

**Random Forest Classifier**

---

## Feature Importance

Top contributing features:

1. Rainfall
2. Humidity
3. Potassium (K)
4. Phosphorus (P)
5. Nitrogen (N)
6. Temperature
7. pH

Feature importance visualization is available in:

```text
reports/feature_importance.png
```

---

## Project Structure

```text
Smart_Crop_Recommendation
│
├── app
│   └── app.py
│
├── data
│   └── raw
│       ├── Crop_recommendation.csv
│       └── rainfall_india.csv
│
├── models
│   └── crop_model.pkl
│
├── notebooks
│   └── crop_recommendation.ipynb
│
├── reports
│   └── feature_importance.png
│
├── README.md
└── requirements.txt
```

---

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit application:

```bash
python -m streamlit run app/app.py
```

---

## Features

- Crop Prediction
- Top 3 Crop Recommendations
- Confidence Score
- Feature Importance Visualization
- Interactive Dashboard
- Random Forest Model Integration

---

## Future Enhancements

- Weather API Integration
- Live Rainfall Data
- Fertilizer Recommendation System
- Mobile Application
- Government Agricultural Dataset Integration
- Multi-language Support

---

## Results

Best Model:

**Random Forest Classifier**

Accuracy:

**99.55%**

---

## Author

Abhishek Bante

Machine Learning Mini Project
