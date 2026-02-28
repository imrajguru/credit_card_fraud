# 💳 Credit Card Fraud Detection System

A Machine Learning-based web application built using **Streamlit** that detects fraudulent credit card transactions in real time.

---

## 🚀 Project Overview

This project aims to identify fraudulent credit card transactions using supervised machine learning techniques.

The application provides a simple and interactive **Streamlit UI** where users can input transaction details and receive instant predictions on whether the transaction is:

- ✅ Legitimate  
- 🚨 Fraudulent  

The model is trained on transaction data and uses preprocessing and feature scaling before prediction.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle / Joblib

---

## 📂 Project Structure

credit_card_fraud/
│
├── app.py  
├── requirements.txt  
├── models/  
│   └── fraud_detection_model.pkl  
├── dataset/  
│   └── fraudTest.csv  
├── .gitignore  
└── README.md  

---

## ⚠️ Dataset Information

Due to GitHub's file size limitations (100MB max), the dataset and trained model are **not included in this repository**.

You can download the dataset from:

Kaggle Credit Card Fraud Detection Dataset  
(Add your Kaggle dataset link here)

After downloading:

1. Create a folder named `dataset/`
2. Place `fraudTest.csv` inside it
3. Train the model (if required)
4. Run the application

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/imrajguru/credit_card_fraud.git
cd credit_card_fraud

```

## Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the Streamlit App
```
streamlit run app.py
```
The application will open in your browser.

##🧠 Model Details

Algorithm Used: (Mention your algorithm here — e.g., Random Forest / Logistic Regression)

Data Scaling: StandardScaler

Evaluation Metrics:

Accuracy

Precision

Recall

F1-Score

##🎯 Internship Submission Note

This project was developed as part of an internship assignment to demonstrate practical implementation of:

Data preprocessing

Machine learning model building

Fraud detection system design

Web deployment using Streamlit

Large files are excluded due to GitHub restrictions.
This follows industry best practices where datasets are not uploaded to version control systems.
