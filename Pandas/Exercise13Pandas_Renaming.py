import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

reviews.rename(columns={'points': 'score'})

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')