import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from lib.evaluation.cross_validation import k_fold_cv

# import joblib

def linear_regression_model(processed_df):
    exclude_cols = ['id', 'station', 'station_name', 'date', 'target']

    X = processed_df.drop(columns=exclude_cols, errors='ignore')
    y = processed_df['target']

    # model pipeline
    linreg_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('lr', LinearRegression())
    ])

    metrics = k_fold_cv(linreg_pipeline, X, y)

    print(metrics)

    # joblib.dump(linreg_pipeline, 'linear_regression_model.joblib')
    # print("저장 완료")