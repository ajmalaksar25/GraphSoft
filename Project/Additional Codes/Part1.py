#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Importing the Necessary Data
google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

#Imported Data (Run these Codes only to check if working or not)
#print(google_csv)
#print(yahoo_csv)
#print(netflix_csv)

#Defining a Dictionary for the Years specified in DataFrames
id_dict={2012:0,2013:1,2014:2,2015:3,2016:4,2017:5,2018:6,2019:7}

#Creating Patches to Use in Legends
#Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
google_patch=mpatches.Patch(color="blue",label="Google")
nflx_patch=mpatches.Patch(color="green",label="Netflix")
yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

#Plotting Graph Based on Original Data
plt.title('Overall Graph')
plt.plot(google_csv['Year'],google_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
plt.show()
