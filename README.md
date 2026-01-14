# 🎓 Student Score Prediction – Machine Learning Project

## 🔍 Project Overview
This project builds an end-to-end Machine Learning pipeline to predict students’ **Math scores** using academic performance and demographic features.  
The goal is to demonstrate a complete ML workflow — from data analysis to deployment-ready modeling.

---

## 🎯 Objective
To develop a robust regression model that accurately predicts **Math scores** while ensuring a **leakage-free and production-ready pipeline**.

---

## 📂 Dataset
The dataset contains student demographic information along with academic scores in reading and writing.  
Both numerical and categorical features are included and handled using appropriate preprocessing techniques.

---

## 🧪 Methodology
1. Data Cleaning & Preparation  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Selection & Training  
5. Cross-Validation  
6. Feature Importance Analysis  
7. Final Model Saving & Inference  

---

## 📊 Exploratory Data Analysis (EDA)
EDA was performed on all score-related variables to understand distributions, correlations, and patterns.  
After analysis, **Math score** was selected as the modeling target to ensure a **leakage-free pipeline**.

---

## 🛠 Feature Engineering
- One-hot encoding for categorical variables  
- Standard scaling for numerical features  
- Unified preprocessing using `ColumnTransformer`  

---

## 🤖 Model Training & Evaluation
The following regression models were trained and evaluated:
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Random Forest  

**Best Performing Model:** Lasso Regression

---

## 📈 Final Model Performance
- **R² Score:** 0.88  
- **RMSE:** 5.38  
- **MAE:** 4.21  

---

## 🔁 Model Validation
5-Fold Cross-Validation was performed using a full preprocessing + modeling pipeline to ensure model stability and generalization.

---

## 🔍 Feature Importance & Interpretation
Key insights from the model:
- Writing score is the strongest predictor of math performance  
- Reading score also has significant influence  
- Gender, lunch type, and test preparation impact outcomes  
- Parental education provides additional predictive signal  

---

## 💾 Model Saving & Inference
The final preprocessing + modeling pipeline was saved using `joblib`, enabling direct prediction on unseen data without manual preprocessing.

---

## 📌 Project Status
✅ Completed — Model trained, validated, interpreted, and saved for deployment.

---

## 🚀 Future Work
- Hyperparameter tuning with GridSearchCV  
- Model deployment using Streamlit or REST API  
- Evaluation on external or real-world datasets  

---

## 🧰 Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-Learn  
- Jupyter Notebook  

---

## 📬 Contact
**Alamin Refat**  
📧 Email: your- alaminrefat2017@gmail.com  
🔗 GitHub: https://github.com/Alamin-refat 



