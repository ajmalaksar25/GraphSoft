import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This next line makes our charts show up in the notebook
#matplotlib inline

table=pd.read_csv("D:\Ajmal\Project\Additional\Hours Netflix.csv")
fig,ax=plt.subplots()
ax.bar(table['Year'],table['Hours'])
plt.show()
