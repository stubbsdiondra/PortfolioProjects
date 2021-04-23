#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING FUNCTIONS
# 19 MARCH 2021

# PROGRAM TITLE: African Happiness Data & Facts Program 

# PROGRAM DESCRIPTION: A Python program that provides the user with a list of choices 
#                      pertaining to African happiness data from the World Happiness 
#                      Report. The list of choices in the program will relate data 
#                      and simple facts using happiness score data from the World 
#                      Happiness Report.

# GENERAL SOLUTION: This program consists of the use of a loop that gives users numbered
#                   options from 1 to 5 to choose from. It will not terminate or exit until
#                   the fifth option is chosen. This program will check if user input is 
#                   valid and will display error messages otherwise. It will check that the 
#                   user only inputs digits.
#
#                   The first choice outputs the overall happiness scores of Africa in 2015 and 2020. 
#                      It also outputs whether the happiness score has increased or decreased overtime.
#                   The second choice outputs the happiest and saddest countries in African according 
#                      to the 2020 World Happiness Report.
#                   The third choice outputs happiness scores of Mauritius and Finland in 2020. 
#                      It also outputs the difference between their scores.
#                   The fourth choice outputs the top 5 happiest and saddest countries in Africa in 2020.
#                   The fifth choice outputs that the program has ended and exits the loop.
#
#                   This is a modularized Python program that breaks all tasks required for this program 
#                   into several functions to avoid code duplication and easily reuse code when checking 
#                   the user’s input and making sure to output the appropriate information for the option 
#                   that the user chooses. It uses the following functions:
#
#                   main -> sets up the program and manages calls to other functions defined to handle to five options
#                   it repeats the five options until the user chooses the option to quit
#
#                   title_msg -> outputs the title of the program and where the data was collected from
#
#                   get_choice -> outputs the list of five choices for the main ment and calls the check_choice 
#                   function passing it 1 as the minimum and 5 as the maximum to obtain a valid input from the user
#
#                   check_choice -> asks the user for their choice and then checks that the user’s input is a valid
#                   digit between the minimum and maximum arguments passed to it
#                   it keeps asking for input until the user enters valid input
#
#                   option1 -> output the overal happiness score of Africa for 2015 and 2020, stating if it has
#                   increased or decreased over time
#
#                   option2 -> output the happiest and saddest country in Africa for 2020
#
#                   option3 -> output the happiness score of Mauritius and Finland and compute/output difference
#
#                   option4 -> output top 5 happiest and saddest countries in Africa for 2020


# DATA COLLECTION: WORLD HAPPINESS REPORT 2015 & WORLD HAPPINESS REPORT 2020
#                  https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv

# PSEUDOCODE: 
#      Output the title of program and where the data was collected from
#      Repeat the following as lomg as the user hasn't chose the option to quit (5)
#      Output list of choice (1 = Overall Happiness Score, 2 = Happiest Country in 
#        Africa, 3 = Happiness of Mauritius vs. Finland, 4 = Top 5 Happiest & Saddest, 
#        5 = Quit)
#     
#      get choice from the user
#      if the user's input only contains digits then check which choice they made and output 
#         the appropriate data and simple facts for that choice
#         choice 1 --> Output the overal happiness score of Africa for 2015 and 2020, stating if it has increased
#                      or decreased over time
#         choice 2 --> Output the happiest and saddest country in Africa for 2020
#         choice 3 --> Output the happiness score of Mauritius and Finland and comput/output difference
#         choice 4 --> Output top 5 happiest and saddest countries in Africa for 2020
#         choice 5 --> Output program had ended and terminate loop and program
#      otherwise, disply and error message and allow the user to try again


# function name: title_msg
# arguments: none
# return: none
# descrption: outputs the title of the program and where the data was collected from
def title_msg():
    
    # output title of program and where data was collected
    print("Africa Happiness Data & Simple Facts Program")
    print("Data collected from 2015 and 2020 World Happiness Report\n\n")

# function name: check_choice
# arguments: 2 integer values representing the minimum and maximum numbered options in the menu              
# return: the valid input 
# description: asks the user for their choice and then checks that the user's input is a valid digit
#              between the minimum and maximum arguments passed to it
#              it keeps asking for input intil the user enters valid input
#              between the passed minimum and maximum argument(s)

def check_choice(minimum,maximum):
    
    # define string variable that is empty to hold user's input
    choice = ''
    
    # loop until the user's input is no longer empty
    while choice == '':
        
        # ask the user to input their choice and store it into a variable
        choice = input("Choice: ")
        
        print("")
        
        # check if the user's input does not only contain digits
        if choice.isdigit() == False:
            
            #output an error message stating that the user did not enter input with only digits
            print("Invalid Entry: Choice should only contain digits. Please choose one of the numbered options (1-5) in the list")
            print("")
            
    
        # otherwise
        else:
            
            # coverts the user's input to an integer
            choice = int(choice)
            
            # check if the user's input is less than the minimum or greater than the maximum
            if choice < minimum or choice > maximum:
                
                # output an error message stating that the user did not enter input between 1 and 5
                print("Invalid entry: Choice outside of range. Please choose one of the numbered options ", minimum, "-", maximum, "in the list")

    return choice
                

# function name: get_choice
# arguments: none
# return: the valid input
# descrption: outputs the list of five choices for the main menu and calls the check_choice function
#             passing it 1 as the minimum and 5 as the maximum to obtain a valid input from the user
def get_choice():
    
    #output the list of options the user can choose from
    print("Choose one of the following numbered options to view data and statistics about happiness in Africa.")
    print("1. Overall Happiness of Africa: 2015 vs 2020")
    print("2. Happiest & Saddest country in Africa for 2020")
    print("3. Happiness score of Mauritius vs Finland for 2020")
    print("4. Top 5 Happiest & Saddest countries in Africa for 2020")
    print("5. Quit")
    
    print("")
    
    # call the check_choice function passing it 1 as the minimum and 5 as the maximum
    #      store the returned value in a variable
    choice = check_choice(1,5)
    
    # return the user's valid input that was stored in the variable above
    return choice
    

# function name: option4
# arguments: none
# return: none
# description: outputs the top 5 happiest and saddest countries in Africa for 2020
def option4():
    # output the top 5 happiest & saddest African countries for 2020
    print("The Top 5 Happiest Countries in Africa for 2020:")
    print("Mauritius")
    print("Libya")
    print("Ivory Coast")
    print("Benin")
    print("Congo(Brazzaville)")
    print("")
    print("The Top 5 Saddest Countries in Africa for 2020:")
    print("Tanzania")
    print("Central Africa Republic")
    print("Rwanda")
    print("Zimbabwe")
    print("South Sudan")
    
    print("")
    print("")

# function name: option3
# arguments: none
# return: none
# description: outputs the happiness score of Mauritius and Finland in 2020 and compute/output the difference
def option3():
    
    # define float variables storing the happiness scores of Mauritius and Finland
    mauritius = 6.10
    finland = 7.81

    # compute the difference between the happiness scores of Finland and Mauritius
    difference = (finland - mauritius)

    #output the happiness score of Mauritius and Finland in 2020 and compute/output the difference
    print("2020 Mauritius Happiness Score:", mauritius)
    print("2020 Finland Happiness Score:", finland)
    print("In 2020, Finland ranked happier than Mauritius with a difference of", difference)
    
    print("")
    print("")
    
# function name: option2
# arguments: none
# return: none
# description: outputs the happiest and saddest country in Africa for 2020
def option2():
    
    # define float variables storing the happiness scores of Mauritius and South Sudan from 2020
    mauritius = 6.10
    south_sudan = 2.82

    # output the happiest and saddest country in Africa for 2020
    print("The Happiest African Country in 2020 was Mauritius with a score of", mauritius)
    print("The Saddest African Country in 2020 was South Sudan with a score of", south_sudan)
    
    print("")
    print("")
    
# function name: option1
# arguments: none
# return: none
# description: outputs happiness scores of Africa from 2015 and 2020 and if they have increased or decreased
def option1():
    
    # define float variables storing Africa's happiness scores for 2015 and 2020
    africa_happiness2015 = 4.30
    africa_happiness2020 = 4.43

    # output happiness scores of Africa from 2015 and 2020 and if they have increased or decreased
    print("Overall happiness score of Africa in 2015:", africa_happiness2015)
    print("Overall happiness score of Africa in 2020:", africa_happiness2020) 
    print("The overall happiness score of Africa has increased since 2015.")
    
    print("")
    print("")

# function name: main
# arguments: none
# return: none
# description: sets up the program and manages calls to other functions defined to handle the five options
#              it repeats the five options until user chooses the option to quit
def main():
    
    # define string variable that is empty to hold user's input
    choice = ''
    
    # call title_msg function to output the title of the program and where the data was collected from
    title_msg()
    
    # loop until the user chooses the choice to quit the program
    while choice != 5:
        
        # call the get_choice function to get the choice from the user and store in variable
        choice = get_choice()
        
        # check if the user chose the first option
        if choice == 1:
            
            # call option1 function to output appropiate data and calculations for this option
            option1()
        
        # check if the user chose the second option
        elif choice == 2:
           
            # call option2 function to output appropiate data and calculations for this option
            option2()
            
        # check if the user chose the third option
        elif choice == 3:
            
            # call option3 function to output appropiate data and calculations for this option
            option3()
        
        # check if the user chose the fourth option
        elif choice == 4:
            
            # call option4 function to output appropiate data and calculations for this option
            option4()
        
        # check if the user chose the fifth option
        elif choice == 5:
            
            # output that the program has ended
            print("Program Ended.")
    
    
# call the main function to run the program

main()


# In[ ]:




