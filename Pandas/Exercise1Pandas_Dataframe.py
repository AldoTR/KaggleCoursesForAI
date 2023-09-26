import pandas as pd

dataframe1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print('\n')
print(dataframe1)

dataframe2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print('\n')
print(dataframe2)

dataframe3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print('\n')
print(dataframe3)

fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
print(fruits)

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                 index = ['2017 Sales', '2018 Sales'])
print(fruit_sales)
