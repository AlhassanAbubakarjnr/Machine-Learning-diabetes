


# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview

This project demonstrates a **complete Machine Learning lifecycle** for predicting whether a patient has diabetes based on medical attributes. The project also includes a **Streamlit dashboard** to showcase basic model deployment.

This is a **beginner-friendly educational project**, designed to teach students how Machine Learning works from data loading to deployment.

---

## 🎯 Problem Definition

**Objective:**
Build a Machine Learning model that predicts whether a patient has diabetes.

* **Problem Type:** Binary Classification
* **Target Variable:** `Outcome`

  * `0` → Not Diabetic
  * `1` → Diabetic

---

## 📂 Dataset Collection

* **Dataset Name:** Pima Indians Diabetes Dataset
* **Format:** CSV
* **Records:** 768 rows
* **Features:** 8 input features + 1 target column

---

## 🔍 Data Understanding

### Input Features

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

### Target Feature

* `Outcome`

---

## 🧹 Data Preprocessing

Steps performed:

* Loaded dataset using **Pandas**
* Separated input features (`X`) and target (`y`)
* Split data into training and testing sets (80% / 20%)

⚠️ *Note:* Data cleaning and handling of invalid values were skipped to keep the project simple for beginners.

---

## 📊 Exploratory Data Analysis (Basic)

* Inspected dataset shape and columns
* Checked target variable distribution

(No advanced visualization included.)

---

## 🤖 Model Selection

**Chosen Algorithm:** Logistic Regression

**Why Logistic Regression?**

* Simple and fast
* Easy to understand
* Suitable for binary classification
* Ideal for teaching Machine Learning fundamentals

---

## 🏋️ Model Training

* Trained Logistic Regression model on training data
* Used default parameters
* Set `max_iter = 1000` to ensure convergence

---

## 📈 Model Evaluation

**Evaluation Metric Used:** Accuracy

* Achieved approximately **75–78% accuracy** on test data
* Confirms the model learned basic patterns from the dataset

---

## 🔮 Model Prediction

* Model predicts:

  * `0` → Not Diabetic
  * `1` → Diabetic
* Predictions tested on unseen data
* Same trained model used in the Streamlit application

---

## 🚀 Streamlit Dashboard (Deployment)

A **Streamlit web application** was developed to demonstrate model deployment.

### Dashboard Features

* Sidebar for user input
* Real-time prediction
* Simple and interactive UI
* Educational demonstration of ML deployment

---

## 🗂️ Project Structure

```text
diabetes-ml-streamlit/
│── app.py                  # Streamlit application
│── model_training.py       # Model training script
│── diabetes.csv            # Dataset
│── README.md               # Project documentation
│── requirements.txt        # Project dependencies
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Git & GitHub

---

## ⚠️ Limitations

* No handling of missing or invalid values
* No feature scaling
* No hyperparameter tuning
* Not suitable for real medical diagnosis

---

## 🔮 Future Improvements

* Data cleaning and imputation
* Feature scaling
* Use advanced ML models
* Save trained model using `joblib`
* Improve evaluation metrics
* Cloud deployment

---

## ✅ Conclusion

This project demonstrates a **complete Machine Learning workflow**, from problem definition to deployment, making it ideal for **students and beginners** learning ML fundamentals.

---

📌 *Disclaimer:* This project is for educational purposes only and should not be used for medical decision-making.
