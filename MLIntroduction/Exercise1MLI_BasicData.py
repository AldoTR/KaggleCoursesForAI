import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
print (melbourne_data.columns)
print(melbourne_data.describe())
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
print('Prediction target')
print(y)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude ']

print('Features')
print(Y.head)
print(X.head)