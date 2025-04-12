import pandas as pd
import numpy as np

def convert_minus9999_to_nan(df):
    "-9999를 NaN으로 변환합니다."
    return df.replace(-9999, np.nan)

def interpolate_row(row):
    hours = np.array(range(len(row)))
    mask = row.notnull().values
    if mask.sum() >= 2:
        interp_vals = np.interp(hours, hours[mask], row[mask])
        return pd.Series(interp_vals, index=row.index)
    else:
        return row

def impute_hourly_features(df, feature_prefix):
    """
    주어진 feature_prefix에 대해 '_0'부터 '_23'까지의 컬럼을 각 row에 관해 linearly interpolate합니다.
    exception case 시 mean 이용
    """
    cols = [f'{feature_prefix}_{i}' for i in range(24) if f'{feature_prefix}_{i}' in df.columns]
    if not cols:
        return df

    df[cols] = df[cols].apply(interpolate_row, axis=1)

    for col in cols:
        if df[col].isnull().sum() > 0:
            df[col] = df.groupby('station')[col].transform(lambda x: x.fillna(x.mean()))
            df[col] = df[col].fillna(df[col].mean())
    return df

def handle_missing_values(df, feature_groups):
    df = convert_minus9999_to_nan(df)

    for feature in feature_groups:
        if feature == 'sunshine_duration':
            night_hours = [0, 1, 2, 3, 4, 5, 22, 23]
            for hour in night_hours:
                col = f'sunshine_duration_{hour}'
                # 밤 -> 0으로 대체
                if col in df.columns:
                    df[col] = df[col].fillna(0)
            # 낮 -> row interpolation
            df = impute_hourly_features(df, feature)
        else:
            df = impute_hourly_features(df, feature)

    return df
