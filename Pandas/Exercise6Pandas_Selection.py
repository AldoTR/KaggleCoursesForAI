import pandas as pd

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
wine_reviews_country = wine_reviews.loc[0, 'country']
print(wine_reviews_country)

wine_reviews2 = wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
print(wine_reviews2)

wine_reviews3 = wine_reviews.set_index("title")
print(wine_reviews3)

wines_italy = wine_reviews.country = "Italy"
print(wines_italy)

wines_all_italy = wine_reviews.loc[wine_reviews.country == "Italy"]
print(wines_all_italy)

wine_italy_points = wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90), ['country', 'points']]
print(wine_italy_points)

wine_italy_or_points = wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90), ['country', 'points']]
print(wine_italy_points)

wines_in_country = wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France']), ['country', 'points', 'critic']]
print(wines_in_country)

wines_in_country['points'] = 0
print(wines_in_country)

wines_in_country['points'] = range(len(wines_in_country), 0, -1)
print(wines_in_country)

wines_in_country['points'] = range(0, len(wines_in_country), 1)
print(wines_in_country)
