#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Importing the Necessary Data
google_csv=pd.read_csv("D:\Ajmal\Project\Google 2012-20.csv")
yahoo_csv=pd.read_csv("D:\Ajmal\Project\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("D:\Ajmal\Project\wNetflix 2012-20.csv")

#Imported Data (Run these Codes only to check if working or not)
print(google_csv)
print(yahoo_csv)
print(netflix_csv)

#numpy.genfromtxt ~ 
#Function of the Code: The set of functions that convert the data of a column to a value.

google_data=np.genfromtxt("D:\Ajmal\Project\Google 2012-20.csv",delimiter=",",names=["x", "y"])
yahoo_data=np.genfromtxt("D:\Ajmal\Project\Yahoo 2012-20.csv",delimiter=",",names=["x", "y"])
netflix_data=np.genfromtxt("D:\Ajmal\Project\wNetflix 2012-20.csv",delimiter=",",names=["x", "y"])

#Creating Patches to Use in Legends
#Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
google_patch=mpatches.Patch(color="blue",label="Google")
nflx_patch=mpatches.Patch(color="green",label="Netflix")
yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

#Plotting the Data
plt.plot(google_data['x'],google_data['y'],yahoo_data['x'],yahoo_data['y'],netflix_data['x'],netflix_data['y'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
plt.show()


#Styling Commands (Works only on Bar Graphs)
#plt.rcParams.update(plt.rcParamsDefault)
#plt.style.use('grayscale')
#

#Additional Commands that were used previously in this File
#Only kept for Further Reference
#yahoo_csv=pd.read_csv("D:\Ajmal\Project\Yahoo 2012-20.csv")
#print(yahoo_csv)
#yahoo_data=np.genfromtxt("D:\Ajmal\Project\Google 2012-20.csv",delimiter=",",names=["x", "y"])
#plt.plot(yahoo_data['x'],yahoo_data['y'])
#plt.show()
