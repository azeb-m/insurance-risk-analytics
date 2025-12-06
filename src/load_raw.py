import pandas as pd
import os

RAW_PATH = os.path.join("data", "raw", "MachineLearningRating_v3.txt")


def load_data():
    df = pd.read_csv(RAW_PATH, sep="|", engine="python")
    print("Loaded as pipe-delimited file")
    return df

if __name__ == "__main__":
    df = load_data()
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())
