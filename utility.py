import pandas as pd


def get_category_counts(df):
    return df.value_counts()


def get_category_index(counts):
    return counts.index


def merge_data(df_1, df_2, df_3, on, suffix_one, suffix_two, suffix_three):
    df_merged = pd.merge(
        df_1,
        df_2,
        df_3,
        on=on,
        how="outer",
        suffixes=(suffix_one, suffix_two, suffix_three),
    )
    return df_merged


def merge_data_two(df_1, df_2, on, suffix_one, suffix_two):
    df_merged = pd.merge(
        df_1, df_2, on=on, how="outer", suffixes=(suffix_one, suffix_two)
    )
    return df_merged
