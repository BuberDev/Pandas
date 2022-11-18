import pandas as pd

fuel = pd.read_csv('fuel.csv', low_memory=False, usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'])
fuel.head()

fuel.info()

fuel.dtypes

fuel.dtypes.value_counts()

fuel['Make'].value_counts().head(10)

fuel.index

fuel.columns

fuel.values

fuel.axes

fuel.shape

fuel.count()

len(fuel)
