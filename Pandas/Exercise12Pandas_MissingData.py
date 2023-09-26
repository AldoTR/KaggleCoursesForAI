import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

reviews[pd.isnull(reviews.country)]

reviews.region_2.fillna("Unknown")

reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")