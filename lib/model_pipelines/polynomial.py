import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from lib.evaluation.cross_validation import k_fold_cv

def polynomial_model(processed_df, degree=2):
    poly_model = Pipeline([
        ('scaler', StandardScaler()),
        ('poly_features', PolynomialFeatures(degree=degree, include_bias=False)),
        ('linreg', LinearRegression())
    ])

    exclude_cols = ['id', 'station', 'station_name', 'date', 'target']

    X = processed_df.drop(columns=exclude_cols, errors='ignore')
    y = processed_df['target']

    metrics = k_fold_cv(poly_model, X, y, k=5, shuffle=True, random_state=42)

    print(metrics)