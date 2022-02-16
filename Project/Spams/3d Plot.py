from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")
z=1
google_csv=pd.read_csv("Spams\Google 2012-20.csv")
print(google_csv)
google_data=np.genfromtxt("Spams\Google 2012-20.csv",delimiter=",",names=["x", "y"])
plt.plot3d(google_data['x'],google_data['y'],z)
plt.show()


plt.show()
