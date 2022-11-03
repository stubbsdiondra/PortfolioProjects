#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING CONDITIONALS
# 5 MARCH 2021

# PROGRAM TITLE: HAPPINESS IN AFRICA SURVEY PROGRAM

# PROGRAM DESCRIPTION: A Python program that queries the user to input responses to the survey 
#                      questions from my Google Form survey. The program records the users 
#                      responses and uses conditional statements to check and clean their inputs. 
#                      After cleaning the user input, the program then outputs clean data in a CSV 
#                      format. 

# GENERAL SOLUTION: Import the datetime library to use the method to get the current date and time.
#                   Ask the user for input according to my survey questions.
#                   Use conditional statements to check user input for age, linear scale, multiple 
#                   choice and data driven yes/no questions.
#                   Output the cleaned responses of the user, separated by commas, using a print 
#                   statement with string formatting that combines strings and variables. 

# PSEUDOCODE: Import datetime library.
#             Define variable for current data and time.
#             Define variables and ask for user input to my survey questions.
#             Use if/elif/else statements to check for valid used input and clean 
#             invalid user input if possible.
#             If the user enters valid input to ALL survey questions:
#               print a line with the cleaned data values separated by commas
#               for each response that the user gave to the questions: current data in mm/dd/yyyy 
#               and current time in hh:mm:ss, user’s response to question one, user’s response to 
#               question two, user’s response to question three, etc.
#             If the user enters invalid input to ANY survey questions:
#               output an error message stating unable to output the user’s responses because one 
#               or more of the user’s inputs are invalid.

#######################################################################################################################
################################################### SOLUTION ##########################################################
#######################################################################################################################

# import the datetime library to use functions to get current data and time
from datetime import datetime

# define a variable to get the current date and time
today = datetime.now()

# output message that this is a survey program and topic
print("\t\t\t\t\t\tSurvey Program")
print("\t\t\t\t\tWhat is the Happiness State of Africa?")
print("----------------------------------------------------------------------------------------------------------------")

print("")
print("")

#ask first survery question about age and assign user input to variable
age_input = input("How old are you? ")

#######################################################################################################################
#                                               VALID AGE CHECK
#######################################################################################################################
# define flag variable of boolean type to track if user enters invalid input
#   set to be True and if any user input is invalid, then set to False
valid = True

# check if user's input is less than 2 characters long
#    if true, then reassign variable of boolean type to state that a rule 
#    has been violated
if (len(age_input) < 2):
    valid = False
    
# define variable for the first two characters of the user's input
#    this should represent the user's entered age 
age = age_input[0:2]

# check if any characters in age are NOT digits
#    if true, then reassign variable of boolean type to state that
#    a rule has been violated
if age.isdigit()  == False:
    valid = False
    
# check if user's input is more than two characters long AND if the 
#    third character is a digit (i.e., something like 723) 
#    if true, then reassign variable of boolean type to state that a 
#    rule has been violated
if (len(age_input) > 2) and age_input[2].isdigit():
    valid = False 

    
# if variable of boolean type determines that no rules were violated,
#    then print the cleaned data value 
#    otherwise, print that it is invalid
if (valid):
    print("The age value is " + age + ".")
else:
    print("The age value is invalid.")

#######################################################################################################################
#                                              END VALID AGE CHECK
#######################################################################################################################

print("")
print("")

# ask second survery question about which African country had the highest happiness 
#   rank in 2020 and assign user input to variable

print("Which African country do you think had the highest happiness rank in 2020?")

print("")

print("Please enter one of the options listed below.")
print("Israel")
print("Mauritius")
print("South Sudan")
print("Ethiopia")

print("")
print("")

happiest_country = input("Your response: ")

#######################################################################################################################
#                                             MULTIPLE CHOICE CHECK
#######################################################################################################################

# if the user enters a valid choice for this multiple choice question,
#    the output that this is a valid choice and us this input in the final output
#    otherwise, output that the user input an invalid choice
if happiest_country == "Israel" or happiest_country == "israel":
    print("Your response is " + happiest_country + ".")
elif happiest_country == "Mauritius" or happiest_country == "mauritius":
    print("Your response is " + happiest_country + ".")
elif happiest_country == "South Sudan" or happiest_country == "south sudan":
    print("Your response is " + happiest_country + ".")
elif happiest_country == "ethiopia" or happiest_country == "ethiopia":
    print("Your response is " + happiest_country + ".")
else:
    print("This is not a valid choice.")
    valid = False 

#######################################################################################################################
#                                           END MULTIPLE CHOICE CHECK
#######################################################################################################################

print("")
print("")

# ask third survey question about whether freedom to make life choices raises or lowers happiness

print("Do you think freedom to make life choices raises or lowers happiness?")

print("")

print("Please choose from the options listed below.")
print("Raises")
print("Lowers")

print("")

life_choices = input("Your response: ")

#######################################################################################################################
#                                             MULTIPLE CHOICE CHECK
#######################################################################################################################
# if the user enters a valid choice for this multiple choice question,
#    the output that this is a valid choice and us this input in the final output
#    otherwise, output that the user input an invalid choice
if life_choices == "Raises" or life_choices == "raises":
    print("You think freedom to make life choices " + life_choices + " happiness.")
elif life_choices == "Lowers" or life_choices == "lowers":
    print("You think freedom to make life choices " + life_choices + " happiness.")
else:
    print("This is not a valid choice.")
    valid = False
    
#######################################################################################################################
#                                             END MULTIPLE CHOICE CHECK
#######################################################################################################################

print("")
print("")

#ask fourth survey question about if more freedom to make life choices makes people happier

print("The more freedom there is to make life choices, the more people are happy.")

print("")

print("1       2       3       4       5")
print("Strongly Disagree          Strongly Agree")

print("")

happier = input("Your response: ")

#######################################################################################################################
#                                             LINEAR SCALE CHECK
#######################################################################################################################

# if the user inputted only digits, then convert thier input to an integer
#    otherwise, output that the user did not input a valid number and 
#    exit the program
# if the user entered a valid input between 1 and 5 on the linear scale,
#    the output that this is a valid choice and use the input in the final output
#    otherwise, output that the user input an invalid choice
if happier.isdigit():
    happier = int(happier)
    if happier >= 1 and happier <= 5:
        print("The choice " + str(happier) + " is valid.")
    else:
        print("This is not a valid choice.")
        valid = False
else:
    print("This is not a valid choice.")
    valid = False

#######################################################################################################################
#                                           END LINEAR SCALE CHECK
#######################################################################################################################

print("")
print("")

# ask fifth survey question about which countries have higher happiness ranks

print("What countries have higher happiness ranks? Poor or wealthy countries?")

print("")

print("Please choose from options listed below.")
print("Poor countries")
print("Wealthy countries")

print("")

ranks = input("Your response: ")

#######################################################################################################################
#                                             MULTIPLE CHOICE CHECK
#######################################################################################################################

# if the user enters a valid choice for this multiple choice question,
#    the output that this is a valid choice and us this input in the final output
#    otherwise, output that the user input an invalid choice
if ranks == "Poor countries" or ranks == "poor countries":
    print("You believe that " + ranks + " receive higher happiness ranks.")
elif ranks == "Wealthy countries" or ranks == "wealthy countries":
    print("You believe that " + ranks + " receive higher happiness ranks.")
else:
    print("This is not a valid choice.")
    valid = False
#######################################################################################################################
#                                           END MULTIPLE CHOICE CHECK
#######################################################################################################################

print("")
print("")

# ask sixth survey question about if social support has an affect on the overall happiness of a country

print("Do you think social support has an affect on the overall happiness of a country?")

print("")

print("Please answer Yes or No.")

social_support = input("Your response: ")

#######################################################################################################################
#                                             MULTIPLE CHOICE CHECK
#######################################################################################################################

# if the user enters a valid choice for this multiple choice question,
#    the output that this is a valid choice and us this input in the final output
#    otherwise, output that the user input an invalid choice
if social_support == "Yes" or social_support == "yes":
    print("You believe that social support has an affect on the overall happiness of a country.")
elif social_support == "No" or social_support == "no":
    print("You believe that social support does not have an affect on the overall happiness of a country.")
else: 
    print("This is not a valid answer.")
    valid = False
#######################################################################################################################
#                                           END MULTIPLE CHOICE CHECK
#######################################################################################################################

print("")
print("")

# output the cleaned user input in a CSV format with the timestamp mm/dd/yyy hh:mm:ss
# as first field and then followed by user responses to questions
if (valid):
    print("Your survey responses: ")
    print('%02d/%02d/%04d %02d:%02d:%02d, %s, %s, %s, %s, %s, %s' % (today.month, today.day, today.year, today.hour, today.minute, today.second, age, happiest_country, life_choices, str(happier), ranks, social_support))
else:
    print("Unable to output your responses because one or more of your responses are invalid. Try again.")

