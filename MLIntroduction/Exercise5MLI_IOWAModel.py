import pandas as pd
from sklearn.tree import DecisionTreeRegressor

iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)

print(home_data.columns)
y = home_data.SalePrice

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath',    'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]

iowa_model = DecisionTreeRegressor(random_state=1)

iowa_model.fit(X, y)

predictions = iowa_model.predict(X)
print(predictions)