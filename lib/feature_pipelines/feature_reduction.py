# import numpy as np

def reduce_feature_columns(df, base_features):
    # corr_threshold=0.95
    # numeric_df = df.select_dtypes(include=[np.number])
    # corr_matrix = numeric_df.corr().abs()
    # upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    # to_drop = [column for column in upper.columns if any(upper[column] > corr_threshold)]

    to_drop = []

    for feature in base_features:
        for hour in range(24):
            raw_col = f"{feature}_{hour}"
            if raw_col in df.columns:
                to_drop.append(raw_col)

    to_drop = list(set(to_drop))
    df_reduced = df.drop(columns=to_drop)

    return df_reduced, to_drop