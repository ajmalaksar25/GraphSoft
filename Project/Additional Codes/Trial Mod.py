#display the whole graph
#display between a selected range
#analysis of data

#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Importing the Necessary Data
google_csv=pd.read_csv("D:\Ajmal\Project\Revenue\Google 2012-20.csv")
yahoo_csv=pd.read_csv("D:\Ajmal\Project\Revenue\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("D:\Ajmal\Project\Revenue\wNetflix 2012-20.csv")

#Imported Data (Run these Codes only to check if working or not)
print(google_csv)
print(yahoo_csv)
print(netflix_csv)

#Defining a Dictionary for the Years specified in DataFrames
id_dict={2012:0,2013:1,2014:2,2015:3,2016:4,2017:5,2018:6,2019:7}

#Getting Input from User
Start_Year=int(input("Choose an Year (between 2012-2019): "))
End_Year=int(input("Choose an Year (between 2012-2019): "))

#Applying the Input Command on the Dictionary
x_start=int(id_dict[Start_Year])
x_end=int(id_dict[End_Year])+1

#Creating New DataFrames based on User input
mod_gcsv=google_csv[x_start:x_end]
mod_ycsv=yahoo_csv[x_start:x_end]
mod_ncsv=netflix_csv[x_start:x_end]

#numpy.genfromtxt ~ 
#Function of the Code: The set of functions that convert the data of a column to a value.
google_data=np.genfromtxt("D:\Ajmal\Project\Revenue\Google 2012-20.csv",delimiter=",",names=["x", "y"])
yahoo_data=np.genfromtxt("D:\Ajmal\Project\Revenue\Yahoo 2012-20.csv",delimiter=",",names=["x", "y"])
netflix_data=np.genfromtxt("D:\Ajmal\Project\Revenue\wNetflix 2012-20.csv",delimiter=",",names=["x", "y"])

#Creating Patches to Use in Legends
#Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
google_patch=mpatches.Patch(color="blue",label="Google")
nflx_patch=mpatches.Patch(color="green",label="Netflix")
yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

#Plotting the Data
#plt.plot(google_data['x'],google_data['y'],yahoo_data['x'],yahoo_data['y'],netflix_data['x'],netflix_data['y'])
#plt.xlabel("Years")
#plt.ylabel("Revenue")
#plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
#plt.show()

#Plotting Graph Based on Original Data
plt.suptitle('Revenue over Years Graph')
plt.subplot(2,1,1)
plt.title('Overall Graph')
plt.plot(google_csv['Year'],google_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])

#Plotting Graph Based on User Request
plt.subplot(2,1,2)
plt.title('Graph Based on User Request')
plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],mod_ycsv['Year'],mod_ycsv['Revenue'],mod_ncsv['Year'],mod_ncsv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
#additional line
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.show()

#Expoting the Data
mod_gcsv.to_csv (r'D:\Ajmal\Project\Exported Data\User Request Data Google.csv', index = False, header=True)
mod_ycsv.to_csv (r'D:\Ajmal\Project\Exported Data\User Request Data Yahoo.csv', index = False, header=True)
mod_ncsv.to_csv (r'D:\Ajmal\Project\Exported Data\User Request Data Netflix.csv', index = False, header=True)

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
