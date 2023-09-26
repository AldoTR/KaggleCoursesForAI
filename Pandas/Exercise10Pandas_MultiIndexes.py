import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed

mi = countries_reviewed.index
type(mi)

countries_reviewed.reset_index()

countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

countries_reviewed.sort_values(by='len', ascending=False)

countries_reviewed.sort_index()

countries_reviewed.sort_values(by=['country', 'len'])