import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

reviews.points.describe()

reviews.taster_name.describe()

reviews.points.mean()

reviews.taster_name.unique()

reviews.taster_name.value_counts()