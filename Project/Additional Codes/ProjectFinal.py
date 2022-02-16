#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import sys

inputrange=[1,2,3,4,5,6,7]
yes=['YES','Y','Yes','yes']
no=['NO','N','No','no']
print('Welcome to GraphSoft')
user_statement=print("Please choose one of the following \n1. View the CSVs \n2.Show a graph of the Whole Data \n3.Plot a graph between a specified Range of Years \n4. Plot the original graph and a user-specified graph \n5.Plot a graph between a specified Range of Years and Import as CSV \n6.The graph followed by a detailed analysis of it. \n7.Exit the Program")

user_input=int(input('Choose 1,2,3,4,5 or 6: '))

while isinstance(user_input,int)==True:

    if user_input==1:
        print('The available CSVs are \n1. Google CSV \n2. Yahoo CSV \n3. Netflix CSV \n4. All 3 CSVs')
        user_in=int(input('Which option would you like to Choose? (choose a value between 1 and 4): '))
        if user_in==1:
              google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
              print(google_csv)
              print('Thank you for using GraphSoft')
              break
        if user_in==2:
              yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
              print(yahoo_csv)
              print('Thank you for using GraphSoft')
              break
        if user_in==3:
              netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")
              print(netflix_csv)
              print('Thank you for using GraphSoft')
              break
        if user_in==4:
              google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
              yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
              netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")
              print('Printing Google CSV')
              print(google_csv)
              print('Printing Yahoo CSV')
              print(yahoo_csv)
              print('Printing Netflix CSV')
              print(netflix_csv)
              print('Thank you for using GraphSoft')
              break

    
    elif user_input==2:
        print('Displaying graph of the whole data')
        #Importing the Required Libraries and Modules
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.patches as mpatches

        #Importing the Necessary Data
        google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
        yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
        netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

        #Plotting Graph Based on Original Data
        plt.title('Overall Graph')
        plt.plot(google_csv['Year'],google_csv['Revenue'],color="blue",label="Google")
        plt.plot(yahoo_csv['Year'],yahoo_csv['Revenue'],color="orange",label="Yahoo")
        plt.plot(netflix_csv['Year'],netflix_csv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.legend()
        plt.ylabel("Revenue")        
        plt.show()

        print('Thank you for using GraphSoft')
        break
        
    elif user_input==2:

        #Importing the Required Libraries and Modules
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.patches as mpatches

        #Importing the Necessary Data
        google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
        yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
        netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")
       
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

        #Creating Patches to Use in Legends
        #Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
        google_patch=mpatches.Patch(color="blue",label="Google")
        nflx_patch=mpatches.Patch(color="green",label="Netflix")
        yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

        #Plotting Graph Based on User Request
        #plt.subplot(2,1,2)
        plt.title('Graph Based on User Request')
        print('Displaying a Graph between ',Start_Year,'and ',End_Year)
        plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],color="blue",label="Google")
        plt.plot(mod_ycsv['Year'],mod_ycsv['Revenue'],color="orange",label="Yahoo")
        plt.plot(mod_ncsv['Year'],mod_ncsv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.ylabel("Revenue")
        plt.legend()
        plt.show()
        
        print('Thank you for using GraphSoft')
        break

    elif user_input==3:

        #Importing the Required Libraries and Modules
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.patches as mpatches

        #Importing the Necessary Data
        google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
        yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
        netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

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

        #Plotting Graph Based on Original Data
        plt.suptitle('Revenue over Years Graph')
        plt.subplots_adjust(hspace=0.4, wspace=0.4)
        plt.subplot(2,1,1)
        plt.title('Overall Graph')
        plt.plot(google_csv['Year'],google_csv['Revenue'],color="blue",label="Google")
        plt.plot(yahoo_csv['Year'],yahoo_csv['Revenue'],color="orange",label="Yahoo")
        plt.plot(netflix_csv['Year'],netflix_csv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.ylabel("Revenue")
        plt.legend()

        #Plotting Graph Based on User Request
        plt.subplot(2,1,2)
        plt.title('Graph Based on User Request')
        print('Displaying the full graph and a Graph between ',Start_Year,'and ',End_Year)
        plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],color="blue",label="Google")
        plt.plot(mod_ycsv['Year'],mod_ycsv['Revenue'],color="orange",label="Yahoo")
        plt.plot(mod_ncsv['Year'],mod_ncsv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.ylabel("Revenue")
        plt.legend()
        plt.show()
        
        print('Thank you for using GraphSoft')
        break

    elif user_input==4:

        #Importing the Required Libraries and Modules
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.patches as mpatches

        #Importing the Necessary Data
        google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
        yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
        netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

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


        #Plotting Graph Based on User Request
        plt.title('Graph Based on User Request')
        print('Displaying a Graph between ',Start_Year,'and ',End_Year)
        plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],color="blue",label="Google")
        plt.plot(mod_ycsv['Year'],mod_ycsv['Revenue'],color="orange",label="Yahoo")
        plt.plot(mod_ncsv['Year'],mod_ncsv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.ylabel("Revenue")
        plt.legend()
        plt.show()
        
        yes=['YES','Y','Yes','yes']
        no=['NO','N','No','no']
        
        input2=input('Would you like to proceed to Export? (Y/N): ')
        if input2 in yes:
            #Expoting the Data
            mod_gcsv.to_csv (r'Exported Data\User Request Data Google.csv', index = False, header=True)
            mod_ycsv.to_csv (r'Exported Data\User Request Data Yahoo.csv', index = False, header=True)
            mod_ncsv.to_csv (r'Exported Data\User Request Data Netflix.csv', index = False, header=True)
            print('The file has been exported to a folder called "Exported Data" in the same directory')
            break
        elif input2 in no:
            print('Export Cancelled')

        print('Thank you for using GraphSoft')
        
    elif user_input==5:

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
        plt.plot(google_csv['Year'],google_csv['Revenue'],color="blue",label="Google")
        plt.plot(yahoo_csv['Year'],yahoo_csv['Revenue'],color="orange",label="Yahoo")
        plt.plot(netflix_csv['Year'],netflix_csv['Revenue'],color="green",label="Netflix")
        plt.xlabel("Years")
        plt.ylabel("Revenue")
        plt.legend()   
        plt.show()
        
        print('Thank you for using GraphSoft')
        break

    elif user_input==6:
        print('Thank you for using GraphSoft')
        exit()
        break
    
    elif user_input not in inputrange:
        print('Sorry, please specify a number between 1 to 6')
        break
