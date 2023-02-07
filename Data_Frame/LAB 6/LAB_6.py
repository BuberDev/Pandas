import pandas as pd
import numpy as np

fuel = pd.read_csv('fuel.csv', low_memory=False, usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'],
                                                       index_col='Vehicle ID')

fuel.head()

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

fuel.head()

fuel.fillna(-1).head()

replaceRules = {'Class': '---',
               'Fuel Type': '---',
               'Combined MPG (FT1)': '-1'}

fuel.fillna(replaceRules).head()

avgMPG = fuel['Combined MPG (FT1)' ].mean()
avgMPG

fuel['Class'].fillna('?', inplace=True)
fuel['Fuel Type'].fillna('?', inplace=True)
fuel['Combined MPG (FT1)'].fillna(avgMPG, inplace=True)
fuel.head()

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN
fuel.head()

fuel['Combined MPG (FT1)'].fillna(method='ffill', inplace=True)
fuel.head()
