import pandas as pd
import numpy as np
import re
import os


def load_data(path):
    df = pd.read_csv(path, index_col="show_id")
    df['country'].fillna('Missing',inplace=True)
    df['rating'] = df['rating'].apply(lambda x : x if "min" not in str(x) else None)
    df['rating'].fillna('Missing',inplace=True)
    df['director'].fillna('Missing',inplace=True)
    df['cast'].fillna('Missing',inplace=True)
    df["date_added"] = pd.to_datetime(df['date_added'])
    df["year_added"] = df["date_added"].dt.year
    df['season_count'] = df['duration'].apply(lambda x : str(x).split(" ")[0] if "Season" in str(x) else None)
    df['movie_duration'] = df['duration'].apply(lambda x : str(x).split(" ")[0] if "Season" not in str(x) else None)
    df['season_count'] = df['season_count'].apply(pd.to_numeric, errors='coerce')
    df['movie_duration'] = df['movie_duration'].apply(pd.to_numeric, errors='coerce')
    return df