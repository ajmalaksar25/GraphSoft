#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Defining a Dictionary for the Years specified in DataFrames
id_dict={2012:0,2013:1,2014:2,2015:3,2016:4,2017:5,2018:6,2019:7}

#Importing the Necessary Data
google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

#Creating Patches to Use in Legends
#Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
google_patch=mpatches.Patch(color="blue",label="Google")
nflx_patch=mpatches.Patch(color="green",label="Netflix")
yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

print("When we take a closer look at the graph, we can see that google has only been rising in its overall revenue throughout these years. \nIt had its major leap from the year 2016. \nThe fall of Yahoo was also said to be due to constant development of Google as a worldwide search engine causing more traffic. \nThis helped the company's growth by a huge factor. \nWhen yahoo was sold, it directly gave Google a monopoly in the market.")
print('In the case of Yahoo, we can see a sequential downfall. \nThis is because of the fact that the company did not have any development over the years and did not have a clear vision for its future. \nThis led to the company being acquired by an American Company called Verizon. \nA few divisions which were not purchased by Yahoo was renamed to Altaba Inc who later on ended up selling their stakes in NASDAQ and further filing a Certificate of Dissolution in the US State of Delaware. \nIt is their lack of vision and development that led to the downfall of this once great company.')
print('Netflix originally started as DVD selling company which followed a Pay-Per-Rental model. \nThis meant that people would pay a small amount for renting the DVD and pay a postage charge. \nThe further started moving to online streaming and rentals. \nThis was a large hit to companies like BlockBuster who were the leaders of this market. \nThey once tried enquiring Blockbuster about a partnership in 2010 where the CEO of Blockbuster laughed at the founder of Netflix. \nThey took it a competition and then expanded to online streaming allowing them to have access to a wider audience which promoted the comppany so well. \nThe low prices for watching as many movies attracted millions which helped the company to earn Millions from the years after 2016.')

#Plotting Graph Based on Original Data
plt.title('Overall Graph')
plt.plot(google_csv['Year'],google_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
plt.show()
