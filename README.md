# 🛒 Supermart Profit Prediction | Machine Learning Project

## 📑 Table of Contents

| No. | Section | No. | Section |
|:---:|---|:---:|---|
| 01 | [📌 Project Overview](#-project-overview) |  07 | [📊 Model Performance](#-model-performance) | 
| 02 | [🎯 Project Objectives](#-project-objectives) | 08 | [⚙️ Installation & Setup](#️-installation--setup)  |
| 03 | [✨ Key Features](#-key-features) | 09 | [📈 Example Prediction](#-example-prediction)|
| 04 | [🌐 Live Demo](#-live-demo) |10 | [💡 Business Value](#-business-value) |
| 05 | [🛠️ Technologies Used](#️-technologies-used) | 11 | [🚀 Future Improvements](#-future-improvements) |
| 06 | [🤖 Machine Learning Algorithm](#-machine-learning-algorithm) | 12 |[👩‍💻 About the Author](#-about-the-author) |


---

## 📌 Project Overview

Supermart Profit Prediction is a Machine Learning-based web application developed using Python, Scikit-learn, and Streamlit.

The project predicts estimated profit based on input features such as Sales Amount and Discount. It uses a Linear Regression model to analyze the relationship between sales-related features and profit.

An interactive Streamlit interface allows users to enter input values, upload a dataset, and generate profit predictions in real time.

## 🎯 Project Objectives

- Predict estimated profit using Machine Learning.
- Understand the relationship between sales, discounts, and profit.
- Build an interactive prediction application using Streamlit.
- Evaluate model performance using regression evaluation metrics.
- Provide a simple interface for business-oriented profit estimation.

## ✨ Key Features

- 📂 Dataset Upload Functionality
- 💰 Estimated Profit Prediction
- 📊 Interactive Input Features
- 🤖 Linear Regression Model
- 📈 Model Performance Evaluation
- 📉 Actual vs Predicted Visualization
- 🖥️ Interactive Streamlit Dashboard

## 🌐 Live Demo

🚀 **Try the Supermart Profit Prediction Application Live!**

Experience the interactive Machine Learning application and predict estimated Supermart profit using Sales Amount and Discount.

🔗 **[Click Here to Launch Live Application](https://supermart-profit-prediction-machine-learning-project-7xfe8mntv.streamlit.app/)**

**Platform:** Streamlit Community Cloud

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |  
| Pandas | Data Manipulation |
| NumPy | Numerical Computation | 
| Scikit-learn | Machine Learning | 
| Matplotlib | Data Visualization | 
| Seaborn | Statistical Visualization 
| Streamlit | Web Application |

## 🤖 Machine Learning Algorithm

**Linear Regression**

The Linear Regression algorithm is used to predict Supermart profit based on the selected input features.

### Input Features

- Sales Amount
- Discount

### Target Variable

- Profit



## 📊 Model Performance

The model was evaluated using training and testing datasets.

| Evaluation Metric | Result |
|---|---:|
| Training R² Score | 89.04% |
| Testing R² Score | 92.77% |
| Training MAE | 387.79 |
| Testing MAE | 661.33 |
| Cross-Validation MAE | 438.53 |
| Testing MSE | 854,041.82 |

**Note:** The model achieved a 92.77% R² score on the testing dataset.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Supermart-Profit-Prediction.git
```

### 2. Navigate to Project Directory

```bash
cd Supermart-Profit-Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit Application

```bash
streamlit run app.py
```

## 📈 Example Prediction

| Input Feature | Value |
|---|---:|
| Sales Amount | 230000 |
| Discount | 7.52 |
| Estimated Profit | 19,653.79 |

*Example output from the application.*

## 💡 Business Value

- Helps estimate potential profit from sales-related inputs.
- Provides insights into the relationship between discounts and profitability.
- Demonstrates how Machine Learning can support business decision-making.
- Offers an interactive approach to profit estimation.

## 🚀 Future Improvements

- Experiment with additional regression algorithms.
- Improve prediction performance through feature engineering.
- Add more business-related input features.
- Add interactive business analytics and reporting.

## 👤 About the Author

**Himanshi Sangani**

Aspiring Machine Learning Engineer | Python | SQL | Pandas | NumPy | Scikit-learn | Streamlit

---

⭐ If you find this project useful, don't forget to star the repository!
