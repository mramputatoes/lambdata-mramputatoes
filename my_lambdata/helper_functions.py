import pandas
import numpy
import random


class CleanData:
    def __init__(self):
        return

    def null_count(self, df):
        return df.isnull().sum().sum()


    def train_test_split(self, df, frac):
        msk = np.random.rand(len(df)) < frac
        train = df[msk]
        test = df[~msk]
        return train, test