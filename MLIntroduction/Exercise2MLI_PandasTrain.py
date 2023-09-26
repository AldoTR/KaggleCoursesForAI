import pandas as pd

# save filepath to variable for easier access
iowa_file_path = 'train.csv'
# read the data and store data in DataFrame titled melbourne_data
home_data = pd.read_csv(iowa_file_path) 
# print a summary of the data in Melbourne data
print(home_data.describe())