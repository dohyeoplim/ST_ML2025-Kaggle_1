import pandas as pd
import numpy as np

def get_date_features_df(df):
    """
    'date'(월-일 형식)에서 월, 일, day_of_year, sine/cosine 칼럼을 추출합니다.
    """
    # 월, 일
    month = df['date'].str.split('-').str[0].astype(int)
    day = df['date'].str.split('-').str[1].astype(int)

    # day_of_year(윤년 고려 안함)
    day_of_year = month * 30 + day

    date_features = pd.DataFrame({
        'month': month,
        'day': day,
        'day_of_year': day_of_year,
        'month_sin': np.sin(2 * np.pi * month / 12),
        'month_cos': np.cos(2 * np.pi * month / 12),
        'day_sin': np.sin(2 * np.pi * day_of_year / 365),
        'day_cos': np.cos(2 * np.pi * day_of_year / 365)
    }, index=df.index)

    return date_features

def get_time_segments_df(df, feature_prefixes, segments=None):
    if segments is None:
        segments = {
            'night':    [0, 1, 2, 3, 4, 5],
            'morning':  [6, 7, 8, 9, 10, 11],
            'afternoon':[12, 13, 14, 15, 16, 17],
            'evening':  [18, 19, 20, 21, 22, 23]
        }
    seg_feature_dfs = []
    for feature in feature_prefixes:
        for seg_name, hours in segments.items():
            seg_cols = [f"{feature}_{h}" for h in hours if f"{feature}_{h}" in df.columns]
            if not seg_cols:
                continue
            seg_stats = pd.DataFrame({
                f"{feature}_{seg_name}_mean": df[seg_cols].mean(axis=1),
                # f"{feature}_{seg_name}_std": df[seg_cols].std(axis=1)
            }, index=df.index)
            seg_feature_dfs.append(seg_stats)
    if seg_feature_dfs:
        segments_features = pd.concat(seg_feature_dfs, axis=1)
    else:
        segments_features = pd.DataFrame(index=df.index)
    return segments_features

def get_engineered_df(df, feature_groups):
    date_features = get_date_features_df(df)
    time_seg_features = get_time_segments_df(df, feature_groups)

    engineered_df = pd.concat([df, date_features, time_seg_features], axis=1)

    return engineered_df
