#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING LOOPS
# 10 MARCH 2021

# PROGRAM TITLE: Africa Happiness Data & Simple Facts Program

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
#                   The fifth choice outputs that the program has ended and exits the loop

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


# define string variable that is empty to hold user's input
choice = ''

# output title of program and where data was collected
print("Africa Happiness Data & Simple Facts Program")
print("Data collected from 2015 and 2020 World Happiness Report\n\n")

# loop until the user chooses the choice to quit the program
while choice != 5:
    print("Choose one of the following numbered options to view data and statistics about happiness in Africa.")
    print("1. Overall Happiness of Africa: 2015 vs 2020")
    print("2. Happiest & Saddest country in Africa for 2020")
    print("3. Happiness score of Mauritius vs Finland for 2020")
    print("4. Top 5 Happiest & Saddest countries in Africa for 2020")
    print("5. Quit")
    
    # get the choice for the user's input and store in variable
    choice = input("Choice: ")
    
    print("")
    #check if user's input only contains digits
    if choice.isdigit():
        
        #convert variable storing user input into an integer
        choice = int(choice)
        
        # check if the user chose the first option
        if choice == 1:
            # define float variables storing Africa's happiness scores for 2015 and 2020
            africa_happiness2015 = 4.30
            africa_happiness2020 = 4.43
            
            # output happiness scores of Africa from 2015 and 2020 and if they have increased or decreased
            print("Overall happiness score of Africa in 2015:", africa_happiness2015)
            print("Overall happiness score of Africa in 2020:", africa_happiness2020) 
            print("The overall happiness score of Africa has increased since 2015.")
            
            print("")
            print("")
        
        # check if the user chose the second option
        elif choice == 2:
            # define float variables storing the happiness scores of Mauritius and South Sudan from 2020
            mauritius = 6.10
            south_sudan = 2.82
            
            # output the happiest and saddest country in Africa for 2020
            print("The Happiest African Country in 2020 was Mauritius with a score of", mauritius)
            print("The Saddest African Country in 2020 was South Sudan with a score of", south_sudan)
            
            print("")
            print("")
       
        # check if the user chose the third option
        elif choice == 3:
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
        
        # check if the user chose the third option
        elif choice == 4: 
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
        
        # check if the user choice the fifth option
        elif choice == 5: 
            # output that the program has ended
            print("Program Ended.")
            
        # otherwise, the user has chosen an invalid option (outside range of 1 to 5)    
        else:
            print("Invalid entry: Choice outside of range. Please choose one of the numbered options (1-5) in the list")
            print("")
            
    # otherwise, the user has not entered input containing only digits
    else:
        print("Invalid Entry: Choice should only contain digits. Please choose one of the numbered options (1-5) in the list")
        print("")


# In[ ]:



