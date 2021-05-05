import pandas as pd
import numpy as np
import plotly_express as py

coffes = pd.read_csv('./coffe.csv')
coffel = np.array(coffes['Coffee in ml'])
sleepl = np.array(coffes['sleep in hours'])
c = np.corrcoef(coffel , sleepl)
print(c)

fig = py.scatter(coffes)
fig.show()

mark = pd.read_csv('./mrk.csv')
marks = np.array(mark['Marks In Percentage'])
days = np.array(mark['Days Present'])
c1 = np.corrcoef(marks , days)
print(c1)

fig1 = py.scatter(mark)
fig1.show()
