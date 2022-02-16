import pandas as pd
import matplotlib.pyplot
yes=['Y','Yes','yes']
no=['N','No','no']

input_1=str(input('Would you like to start? (Y/N): '))
#for x in range(0,1):
    #while input_1 in yes:
        #import User_End
      
        #input_2=str(input('Would you like to try again? (Y/N): '))
        #break
        #if input_2 in yes:
            #import User_End
        #elif input_2 in no:
            #break


    
        
#a=import User_End
#exec(a)

def yorn(question = "[y/n]", strict = True):
    """yorn([question][, strict]) -> user input

    Asks the question specified and if the user input is 'yes' or 'y',
    returns 'yes'.  If the user input is 'no' or 'n', it returns no.  If
    strict is False, many other answers will be acceptable."""
    question = question.strip(" ")
    x = input("%s " % question)
    x = x.lower()
    if (x == "yes") or (x == "y") or ((not strict) and ((x == "yep") or (x == "yeah") or (x == "of course") or (x == "sure") or (x == "definitely") or (x == "certainly") or (x == "uh huh") or (x == "okay") or (x == "ok"))): 
        return True 
    elif (x == "no") or (x == "n") or (not strict and x in ["nope", "uh uh", "no way", "definitely not", "certainly not", "nah", "of course not"]):
        return False
    else:
        return yorn(strict = strict)
again = True
while again:
    name = input("Whats your name?: ")
    age = input("How old are you?: ")
    if age.isdigit() and int(age) > 15:
        print("Congradulations you can drive!")
    elif age.isdigit() and int(age) < 16:
        print ("Sorry you can not drive yet :(")
    else:
        print("Enter a valid number")
    print ("it's been very nice getting to know you " + name)
    print ("")
    again = yorn("Would you like to try again? ", strict=False)
