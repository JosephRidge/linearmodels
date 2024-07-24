import pandas as pd


def read_data(path):
    return pd.read_csv(path)


def data_head(df):
    return df.head()


def data_shape(df):
    return df.shape


def check_null(df):
    return df.isnull().mean() * 100


def drop_rows(df):
    return df.dropna()


def get_info(df):
    return df.info()


def get_summary(df):
    return df.describe()
