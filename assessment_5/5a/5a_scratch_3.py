"""
courtesy of wilson. pandas approach
"""

import pandas as pd


def no_mr():
    df = pd.read_csv('abcnews.txt', header=None)
    df.columns = ['date', 'words']
    df['words'] = df['words'].str.split()
    word_df = df.explode(column='words')
    word_df['year'] = df['date'].astype(str).apply(lambda x: x[:4])
    count_by_year = word_df.pivot_table(index=['words', 'year'], values=['date'], aggfunc=len).reset_index()
    count_by_year.rename(columns={'date': 'count'}, inplace=True)
    max_idx = count_by_year.groupby('words')['count'].idxmax()
    result = count_by_year.loc[max_idx]
    print(result)


if __name__ == "__main__":

    no_mr()
