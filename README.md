# 🎓 Student Score Prediction – Machine Learning Project

## 🎯 Project Overview
This project focuses on predicting a student’s **Math score** using factors such as reading score, writing score, gender, parental education, lunch type, and test preparation status.

The goal is to showcase a realistic, production-ready machine learning workflow rather than a simple notebook-based experiment.

---

## 🚀 Live Demo

- **Streamlit Cloud:** https://student-score-prediction-ml-zfcmhmfohejlxjlfq5kq8y.streamlit.app/  
- **Hugging Face Spaces:** https://huggingface.co/spaces/Alamin-refat/student-score-prediction

---

## ✨ Key Features

* **Lasso Regression:** Implements **L1 Regularization** to enhance model generalization and prevent overfitting.
* **Predictive Analytics:** Accurately predicts student scores based on providing data-driven academic insights.
* **Data Visualization:** Includes **EDA** with scatter plots and regression lines for clear data insights.
* **Performance Metrics:** Evaluated using **Mean Absolute Error (MAE)** to ensure prediction accuracy.
* **Streamlined Pipeline:** Efficient workflow covering data preprocessing, model training, and testing.

---

## 📊 Dataset

The dataset contains student performance records with the following attributes:

- Gender  
- Race/Ethnicity  
- Parental level of education  
- Lunch type  
- Test preparation course  
- Reading score  
- Writing score  
- Math score (target variable)

> **Note:** EDA was performed on all score variables, and **Math score** was selected as the final prediction target to ensure a leakage-free modeling pipeline.

---

## 🔍 Exploratory Data Analysis (EDA)

Key EDA steps included:

- Distribution analysis of student scores
- Outlier detection using box plots
- Numerical feature correlation analysis
- Categorical feature impact analysis
- Correlation heatmaps to identify relationships between scores

Insights from EDA guided feature selection and modeling decisions.

---

## 🧠 Technical Workflow

The project follows a structured Machine Learning pipeline to ensure reliable predictions:

1. **Data Acquisition:** Importing student dataset using `Pandas` for structured analysis.
2. **Exploratory Data Analysis (EDA):** Visualizing data distribution and correlation using `Matplotlib` and `Seaborn` to confirm linearity.
3. **Data Preprocessing:** Splitting the dataset into features ($X$) and target ($y$), followed by a **Train-Test Split** (80/20) to validate model performance.
4. **Model Training:** Initializing and training the **Lasso Regression** model with L1 Regularization to optimize coefficients.
5. **Prediction & Testing:** Making predictions on the test set and comparing them against actual results.
6. **Model Evaluation:** Calculating the **Mean Absolute Error (MAE)** to quantify the model's accuracy and precision.

---

## 📊 Final Model Performance

| Metric | Value |
|------|------|
| MAE | ~4.21 |
| RMSE | ~5.39 |
| R² Score | ~0.88 |

The model explains approximately **88% of the variance** in student math scores.

---

## 🧪 Model Comparison & Selection

The following regression models were trained and evaluated:

- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Random Forest Regressor  

### ✅ Final Model Choice
**Lasso Regression** was selected due to:

- Strong generalization performance
- Built-in regularization
- Automatic feature selection
- High interpretability of coefficients

---

## 🔎 Feature Importance & Interpretation

Model coefficients were analyzed to interpret feature impact.

Key observations:

- Writing score and reading score are the strongest predictors
- Gender and lunch type have noticeable influence
- Parental education level contributes moderately
- The model remains interpretable and explainable

---

## 🌐 Deployment

The application is deployed on **two platforms**:

### 1️⃣ Streamlit Cloud
- Direct deployment using Streamlit
- Public live demo for real-time predictions

### 2️⃣ Hugging Face Spaces (Docker-based)
- Dockerized Streamlit application
- Demonstrates cross-platform deployment capability

During deployment, several real-world challenges were addressed:
- Python and library version mismatches
- Dependency installation failures
- Windows-to-Linux environment differences

---

## 🛠️ Tech Stack & Tools

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  
- Docker (for Hugging Face deployment)

---
## 📂 Project Structure

A detailed look at the repository's organization:

```text
Student-Score-Prediction-ML/
├── .devcontainer/                 # Development container configuration
├── .ipynb_checkpoints/           # Jupyter notebook checkpoints
├── Data/                         # Dataset directory
├── README.md                     # Main project documentation
├── Dockerfile                    # Docker configuration for deployment
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
├── student_score_model.pkl       # Trained model (pickle file)
└── student_score_prediction.ipynb # Main Jupyter notebook with full ML pipeline
```
---
## 💻 Installation & Usage

Follow these steps to set up the project locally on your machine:

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/Alamin-refat/Student-Score-Prediction-ML.git](https://github.com/Alamin-refat/Student-Score-Prediction-ML.git)
cd Student-Score-Prediction-ML
```
### 2. Create a Virtual Environment (Recommended)
This keeps the project dependencies isolated and prevents conflicts:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Required Libraries
Install all necessary dependencies listed in the requirements file to ensure the environment is ready:
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit Dashboard
Launch the web application locally to interact with the churn prediction model:
```bash
streamlit run app.py
```
---

## 🧠 Key Learnings

- Built a complete ML pipeline from data analysis to deployment
- Gained hands-on experience with model optimization and evaluation
- Resolved real-world dependency and environment issues
- Deployed the same ML application across multiple platforms

---

## 📬 Contact

**Author:** Alamin Refat  
**GitHub:** https://github.com/Alamin-refat  
**LinkedIn:** https://www.linkedin.com/in/alamin-refat-414b99262/  
**Email:** alaminrefat2017@gmail.com  


Feel free to connect for feedback, collaboration, or discussion.