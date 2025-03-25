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

bash
Copy
Edit

## 🖥 Installation & Usage  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/Revenue-Prediction-Polynomial-Regression.git
cd Revenue-Prediction-Polynomial-Regression
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Model
bash
Copy
Edit
python revenue_prediction.py
📊 Visualizations
1️⃣ Model Performance: MSE vs Polynomial Degree

Shows how model accuracy changes with different polynomial degrees.
2️⃣ Correlation Heatmap

Highlights the relationship between selected features and revenue.

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
