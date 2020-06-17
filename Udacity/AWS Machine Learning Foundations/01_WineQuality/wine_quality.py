import pandas as pd
# wine quality dataset taken from the UCI Machine Learning Repository:
# https://archive.ics.uci.edu/ml/datasets/wine+quality
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()


def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low'


for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')
