# Data Analysis and Modeling Toolkit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def load_data():
    """Load and prepare the dataset"""
    return pd.read_csv("assignment1dataset.csv")


def select_features(df, target='RevenuePerDay', threshold=0.5):
    """Identify important features based on correlation"""
    corr_matrix = df.corr()
    target_corr = corr_matrix[[target]].sort_values(target, ascending=False)
    features = target_corr.index[abs(target_corr[target]) > threshold].tolist()
    features.remove(target)
    return features


def generate_polynomials(X, degree):
    """Create polynomial and interaction features"""
    X_poly = X.copy()
    for d in range(2, degree + 1):
        for col in X.columns:
            X_poly[f'{col}²'] = X[col] ** 2 if d == 2 else X[col] ** d
        for i, col1 in enumerate(X.columns):
            for col2 in X.columns[i + 1:]:
                X_poly[f'{col1}×{col2}'] = X[col1] * X[col2]
    return X_poly


def main():
    # Load and prepare data
    df = load_data()
    features = select_features(df)
    print(f"Selected features: {features}")

    # Split data
    X = df[features]
    y = df['RevenuePerDay']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model evaluation
    degrees = range(1, 6)
    train_errors = []
    test_errors = []

    for degree in degrees:
        X_train_poly = generate_polynomials(X_train, degree)
        X_test_poly = generate_polynomials(X_test, degree)

        model = LinearRegression()
        model.fit(X_train_poly, y_train)

        train_errors.append(mean_squared_error(y_train, model.predict(X_train_poly)))
        test_errors.append(mean_squared_error(y_test, model.predict(X_test_poly)))

    # Create figure with two subplots
    plt.figure(figsize=(14, 6))

    # First subplot: MSE vs Degree
    plt.subplot(1, 2, 1)
    plt.plot(degrees, train_errors, 'bo-', label='Training MSE')
    plt.plot(degrees, test_errors, 'ro-', label='Testing MSE')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('Mean Squared Error')
    plt.title('Model Performance by Polynomial Degree')
    plt.legend()
    plt.grid(True)

    # Second subplot: Correlation heatmap
    plt.subplot(1, 2, 2)
    corr_data = df[features + ['RevenuePerDay']].corr()[['RevenuePerDay']]
    sns.heatmap(corr_data, annot=True, cmap='coolwarm', vmin=-1, vmax=1,
                linewidths=0.5, cbar_kws={'label': 'Correlation'})
    plt.title('Feature Correlation with RevenuePerDay')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()