import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

netflixcsv=pd.read_csv("D:\Ajmal\Project\Additional\Hours Netflix.csv")
print(netflixcsv)
netflixdata=np.genfromtxt("D:\Ajmal\Project\Additional\Hours Netflix.csv",delimiter=",",names=["x", "y"])
plt.bar(netflixdata['x'],netflixdata['y'])
#plt.plot(netflixdata['x'],netflixdata['y'])
#netflixpatch=mpatches.Patch(color="orange",label="Yahoo")
plt.xlabel("Years")
plt.ylabel("Hours")
#plt.legend(handles=[netflixpatch])
plt.show()
