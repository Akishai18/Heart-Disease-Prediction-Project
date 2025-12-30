# ❤️ Heart Disease Prediction System

**AI-Powered Proactive Heart Disease Risk Assessment**

An intelligent medical application that combines machine learning with an intuitive GUI to predict an individual's risk of heart disease. Built with Python, Scikit-Learn, and Tkinter, this system helps healthcare professionals and individuals assess cardiovascular health through comprehensive data analysis and real-time visualization.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=flat&logo=python&logoColor=white)

---

## 🌟 Overview

Heart disease remains one of the leading causes of death worldwide. Early detection and risk assessment are crucial for prevention and treatment. This Heart Disease Prediction System leverages machine learning to analyze 13 critical medical parameters and provide instant risk assessments, empowering both patients and healthcare providers to make informed decisions about cardiovascular health.

The system features a user-friendly graphical interface that allows for easy data entry, real-time visualization of health metrics, and comprehensive patient reports.

---

## ✨ Key Features

### 🤖 Machine Learning Model
- **Logistic Regression Algorithm** for binary classification (at-risk vs. not at-risk)
- **Trained on comprehensive heart disease dataset** with validated medical parameters
- **High accuracy** achieved through stratified train-test split
- **Real-time predictions** based on 13 clinical features
- **Proactive risk assessment** for early intervention

### 🖥️ Interactive GUI Application
- **Patient Registration System** with unique ID tracking
- **Comprehensive Data Entry** for all medical parameters
- **Real-time Visualization** with 4 dynamic graphs
- **Instant Results** with color-coded risk assessment
- **Report Generation** with numbered tracking
- **Professional Medical Interface** designed for clinical use

### 📊 Data Visualization
Four real-time graphs displaying:
1. **Categorical Features** - Sex, FBS, Exang
2. **Vital Signs** - Age, Blood Pressure, Cholesterol, Heart Rate
3. **Cardiac Metrics** - Oldpeak, RestECG, Chest Pain Type
4. **Advanced Indicators** - Slope, CA, Thal

### 🔍 Medical Parameters Analyzed

**13 Critical Features:**
1. **Age** - Patient's age in years
2. **Sex** - Gender (1 = Male, 0 = Female)
3. **CP** - Chest Pain Type (0-3)
4. **Trestbps** - Resting Blood Pressure (mm Hg)
5. **Chol** - Serum Cholesterol (mg/dl)
6. **FBS** - Fasting Blood Sugar > 120 mg/dl
7. **RestECG** - Resting Electrocardiographic Results (0-2)
8. **Thalach** - Maximum Heart Rate Achieved
9. **Exang** - Exercise Induced Angina (1 = Yes, 0 = No)
10. **Oldpeak** - ST Depression Induced by Exercise
11. **Slope** - Slope of Peak Exercise ST Segment (0-2)
12. **CA** - Number of Major Vessels (0-3)
13. **Thal** - Thalassemia (0-3)

---

## 🏗️ Architecture

### System Flow

```
Patient Data Entry (GUI)
    ↓
Data Validation
    ↓
Feature Extraction (13 parameters)
    ↓
Data Preprocessing (NumPy array conversion)
    ↓
Model Prediction (Logistic Regression)
    ↓
Risk Assessment (0 = No Risk, 1 = At Risk)
    ↓
Visualization (4 Real-time Graphs)
    ↓
Report Generation (Color-coded results)
```

### Machine Learning Pipeline

```
Heart Disease Dataset (heart.csv)
    ↓
Data Loading & Exploration
    ↓
Feature Selection (X) & Target (Y)
    ↓
Train-Test Split (80/20, Stratified)
    ↓
Logistic Regression Model
    ↓
Model Training
    ↓
Accuracy Evaluation
    ↓
Model Serialization
    ↓
Real-time Prediction
```

---

## 🧩 Tech Stack

**Machine Learning:**
- Scikit-Learn (Logistic Regression)
- Pandas (Data manipulation)
- NumPy (Numerical operations)

**GUI Framework:**
- Tkinter (Main application)
- ttk (Modern widgets)

**Data Visualization:**
- Matplotlib (Graph generation)
- matplotlib.backends.backend_tkagg (Tkinter integration)

**Additional Libraries:**
- datetime (Date handling)
- messagebox (User alerts)

---

## 🔬 Machine Learning Model

### Algorithm: Logistic Regression

**Why Logistic Regression?**
- Ideal for binary classification (risk vs. no risk)
- Provides probability estimates
- Interpretable coefficients
- Fast training and prediction
- Works well with medical datasets

---
## 🔍 Parameter Definitions

### Age
- Patient's age in years
- Risk factor: Increases with age

### Sex
- 1 = Male
- 0 = Female
- Males typically at higher risk

### CP (Chest Pain Type)
- 0 = Typical angina
- 1 = Atypical angina
- 2 = Non-anginal pain
- 3 = Asymptomatic

### Trestbps (Resting Blood Pressure)
- Measured in mm Hg
- Normal: < 120 mm Hg
- Elevated: 120-129 mm Hg
- High: ≥ 130 mm Hg

### Chol (Serum Cholesterol)
- Measured in mg/dl
- Desirable: < 200 mg/dl
- Borderline high: 200-239 mg/dl
- High: ≥ 240 mg/dl

### FBS (Fasting Blood Sugar)
- 1 = True (> 120 mg/dl)
- 0 = False (≤ 120 mg/dl)
- Indicates diabetes risk

### RestECG (Resting Electrocardiographic Results)
- 0 = Normal
- 1 = Having ST-T wave abnormality
- 2 = Showing probable or definite left ventricular hypertrophy

### Thalach (Maximum Heart Rate Achieved)
- Measured during exercise test
- Higher values generally better
- Age-adjusted norms apply

### Exang (Exercise Induced Angina)
- 1 = Yes (chest pain during exercise)
- 0 = No
- Significant risk indicator

### Oldpeak (ST Depression)
- ST depression induced by exercise relative to rest
- Measured in depression units
- Higher values indicate more severe condition

### Slope (Peak Exercise ST Segment)
- 0 = Upsloping (better)
- 1 = Flat
- 2 = Downsloping (worse)

### CA (Number of Major Vessels)
- 0-3 vessels colored by fluoroscopy
- More vessels = higher risk

### Thal (Thalassemia)
- 0 = Normal
- 1 = Fixed defect
- 2 = Reversible defect
- 3 = Reversible defect

---

## ⚠️ Medical Disclaimer

**IMPORTANT NOTICE:**

This Heart Disease Prediction System is designed as a **supportive tool** and should **NOT** replace professional medical diagnosis or treatment. 

- **For Educational and Research Purposes:** This application demonstrates machine learning in healthcare
- **Not a Medical Device:** Not approved or certified for clinical diagnosis
- **Consult Healthcare Professionals:** Always seek advice from qualified medical practitioners
- **Emergency Situations:** Call emergency services immediately if experiencing chest pain or cardiac symptoms
- **Risk Assessment Only:** Predictions indicate probability, not definitive diagnosis
---
## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
