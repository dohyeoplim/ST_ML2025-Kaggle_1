import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def k_fold_cv(model, X, y, k=5, shuffle=False, random_state=None):
    """
    K-Fold cross validation 수행

    :param model - model object
    :param X - feature DF
    :param y - target DF
    :param k - Fold 개수, 기본 5
    :param shuffle - split 전에 data를 shuffle할 지 여부, 기본 False
    :param random_state - shuffle 시의 random seed 값, 기본 None
    :return metrics - MAE, RMSE, R² 값을 담은 dict 반환
    """
    kf = KFold(n_splits=k, shuffle=shuffle, random_state=random_state)
    mae_list = []
    rmse_list = []
    r2_list = []

    for train_index, val_index in kf.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[val_index]
        y_train, y_val = y.iloc[train_index], y.iloc[val_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)

        mae_list.append(mean_absolute_error(y_val, y_pred))
        rmse_list.append(np.sqrt(mean_squared_error(y_val, y_pred)))
        r2_list.append(r2_score(y_val, y_pred))

    metrics = {
        'MAE': np.mean(mae_list),
        'RMSE': np.mean(rmse_list),
        'R2': np.mean(r2_list)
    }

    return metrics