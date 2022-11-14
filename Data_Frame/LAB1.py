
import pandas as pd

fuel = pd.read_csv('fuel.csv', low_memory= False)
fuel.head()

pd.options.display.max_columns=500
fuel.head(10)

fuel.tail()

fuel = pd.read_csv('./LAB1/fuel.csv', usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'])
fuel.head()

fuel = pd.read_csv('./LAB1/fuel.csv', usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'], index_col=['Vehicle ID'])
fuel.head()
