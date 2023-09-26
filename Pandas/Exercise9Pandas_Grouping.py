import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

reviews.groupby('points').points.count()

reviews.groupby('points').price.min()

reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

reviews.groupby(['country']).price.agg([len, min, max])

