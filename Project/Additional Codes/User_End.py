#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import sys

inputrange=[1,2,3,4,5,6]
yes=['YES','Y','Yes','yes']
no=['NO','N','No','no']
print('Welcome to GraphSoft')
user_statement=print("Please choose one of the following \n1.Show a graph of the Whole Data \n2.Plot a graph between a specified Range of Years \n3. Plot the original graph and a user-specified graph \n4.Plot a graph between a specified Range of Years and Import as CSV \n5.The graph followed by a detailed analysis of it. \n6.Exit the Program")

user_input=int(input('Choose 1,2,3,4,5 or 6: '))

while isinstance(user_input,int)==True:
    
    if user_input==1:
        print('Displaying graph of the whole data')
        import Part1
        print('Thank you for using GraphSoft')
        break
        
    elif user_input==2:
        import Part2
        print('Thank you for using GraphSoft')
        break

    elif user_input==3:
        import Part3
        print('Thank you for using GraphSoft')
        break

    elif user_input==4:
        import Part4
        print('Thank you for using GraphSoft')
        print('The file has been exported to a folder called "Exported Data" in the same directory')
        break

    elif user_input==5:
        import Part5
        print('Thank you for using GraphSoft')
        break

    elif user_input==6:
        print('Thank you for using GraphSoft')
        exit()
        break
    
    elif user_input not in inputrange:
        print('Sorry, please specify a number between 1 to 6')
        break
