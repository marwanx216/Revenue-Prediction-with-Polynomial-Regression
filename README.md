# 📊 Revenue Prediction with Polynomial Regression  

## 📌 Overview  
This project applies **polynomial regression** to predict daily revenue using feature selection based on correlation analysis. The objective is to analyze the impact of different polynomial degrees on model performance and optimize predictive accuracy.

## 🛠 Features  
✔ Feature selection based on correlation  
✔ Polynomial regression (1st to 5th degree)  
✔ Train-test split for model evaluation  
✔ MSE analysis to detect overfitting  
✔ Correlation heatmap visualization  

## 🔬 Data  
The dataset (`assignment1dataset.csv`) contains various features related to business revenue. The target variable is **RevenuePerDay**.

## 📈 Results  
- Higher polynomial degrees improve training accuracy but can lead to **overfitting**.  
- Feature selection enhances model interpretability and efficiency.  
- Correlation analysis helps identify the most impactful predictors.

## 📂 Repository Structure  
📦 Revenue-Prediction-Polynomial-Regression
┣ 📜 assignment1dataset.csv # Dataset
┣ 📜 revenue_prediction.py # Main script
┣ 📜 README.md # Documentation
┣ 📜 requirements.txt # Required Python libraries

📊 Visualizations
1️⃣ Model Performance: MSE vs Polynomial Degree
Shows how model accuracy changes with different polynomial degrees.
![Figure_1](https://github.com/user-attachments/assets/74ea7d50-b523-4f31-922c-d7b5784a7a31)



2️⃣ Correlation Heatmap
Highlights the relationship between selected features and revenue.
![Figure_2](https://github.com/user-attachments/assets/ca669285-ae13-44a0-a257-b82d09ddca5e)

📌 Future Improvements
🚀 Test on a larger dataset
🚀 Try advanced regression models (Ridge, Lasso)
🚀 Deploy as a web app

🤝 Contributing
Feel free to fork this repository and suggest improvements!

📩 Contact
👤 Your Name
📧 [Your Email]
🔗 [LinkedIn Profile]
