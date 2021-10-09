import math

#Feet input: checks to see if feet is numeriic and checks to see if the input is valid
def program():

    def feetInput():
        global feet 
        feet = input("Enter feet amount")
        if feet.isnumeric():
            if int(feet) < 0:
                print("You cant be that height")           
                feetInput()
            elif int(feet) > 12:
                print("you cant be that tall")
               
                feetInput()
        
        else:
            print("enter an integer for feet")
            feetInput()
        float(int(feet))
        return feet


    #inches input: defines stringtype of inches
    def inchesInput():
        inches = input("enter inches")

    

          

        #result variable: checks to see if inches input is alphabetical, if it is then it prompts user to enter a number next time, then exits.
        res = inches.isalpha()
        if res is True:
            print("please enter a number")
            inchesInput()
        else:
        

            #floInches is a variable to convert all numerical inputs to a real number, just in case the user is 5 feet 4.5 inches, so a decimal number for inches input is valid
            floInches = float(inches)
            #Validates inches input
            if floInches > 12 or floInches == 0:
                print("Enter an amount from 0 to 12 inches!")
                inchesInput()
        return floInches



        #Variable names for all height calculations
    feet = feetInput()
    inches = inchesInput()
    totalInches = float((int(feet) * 12) + inches)
    centimeter = (totalInches * 2.54)
    centToMeter = (centimeter / 100)
    meterDisplay = round(centToMeter, 2)
    yardDisplay = round((totalInches / 36), 2)
    
    
   

    

        #this is an if statement to tell the user they are tall if over 96 inches

    if totalInches >= 96:
        print("Height: ", totalInches, "inches... you're very tall!")
    else:
        print("Height: ", totalInches, "inches")

    #All outputs for height in metric and standard
    print("Normal Height: ", feet, " feet, ", inches, "inches")
    print("Metric: ", meterDisplay, " meters")
    print("yards: ", yardDisplay)



def oncemore():
    again = input("would you like to do another? (y/n)")
    if again == "y":
        program()
    elif again == "n":
        print("ok, bye")
        exit()
    else:
        print("type 'y' or 'n'")
        oncemore()

program()
oncemore()



