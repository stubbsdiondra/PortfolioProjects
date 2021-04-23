#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING NUMPY & DICTIONARIES
# 2 APRIL 2021
#
# PROGRAM TITLE: AFRICA HAPPINES SURVEY ANALYSIS PROGRAM
#
#
# PROGRAM DESCRIPTION: A Python program that reads and cleans the Happiness in Africa
#                      Google Forms Survey responses to output data visualizations and 
#                      statistics with this cleaned data. This modularized program breaks
#                      all tasks required for this program into 8 functions to avoid code 
#                      duplication and to easily reuse code when checking values in the 
#                      CSV file and computing data statistics (i.e, mean, median and
#                      standard deviation)

# GENERAL SOLUTION: This program breaks down the tasks required for this program into 8 functions
#
#                   check_age --> This function checks if the age contains only digits (i.e., 21years becomes 21)
#                                 AND checks if the age is between 0 and 150
#
#                   check_linear_scale --> This function checks if rating contains only digits and if the rating 
#                                 is between the scale of 1 to 5
#
#                   check_multiple_choice --> This function checks if the choice for the multiple choice question 
#                                 is not empty and is one of the provided choices for the question 
#
#                   read_csv --> This function opens/reads the survey responses CSV file and checks/cleans invalid 
#                                  data entries in each row of the CSV file
#                                Checks that the age, linear scale and multiple choice responses are valid
#                                  by calling the helper functions defined above
#                                Outputs error messages if the entries cannot be cleaned and what values have
#                                  been skipped
#                                Appends valid/cleaned entries for linear scale responses to lists
#                                Updates accumulator variables counting number of responses for each choice
#                                  in a multiple choice question
#
#                   plt_linear_rating --> This function plots a histogram of the ratings for the linear scale question 
#                                where respondents rate the statement: The more freedom there is to make life choices 
#                                the more people are happy
#
#                   plt_counts --> This function plots a pie chart of the counts for each choice in the multiple choice
#                                  question
#
#                   compute --> This function computes a data statistic using the numpy module (i.e, mean, median, 
#                               standard deviation) with the ratings for linear scale question
#
#                   main --> This function setups the program and manages to call to functions defined above for 
#                            specified processing, calculations, visualizations and output

# PSEUDOCODE: Output that the data from the CSV file is being read and cleaned
#             Output error messages and that the data value has been skipped for invalid respondent input
#             Output that the data from the CSV file has been cleaned
#             Output histogram showing the ratings of which respondents rated the statement: The more freedom 
#               there is to make life choices the more people are happy
#             Output computed data statistics on the linear rating scale question
#               computed mean, median and standard deviation
#             Output pie graph displaying survey responses from users who chose which African country is the happiest

# import the matplotlib.pylot module with the alias plt
import matplotlib.pyplot as plt

# import the csv package
import csv

# import the numpy package with alias np
import numpy as np 


# function name: check_age
# argument(s): one string representing the age of the respondent
# description: checks if the age contains only digits AND checks if the age is between 0 and 150
# return: one boolean if the age is valid
#             True if the age is valid
#             False if the age is invalid
def check_age(some_age):
    
    # flag variable set to True assuming age is valid before checks
    valid = True
    
    # check if the age (passed as the argument) contains only digits
    #       OR the first two characters of the age (passed as the argument)
    #       contain only digits
    #
    # examples that PASS this check: 26years old, 200 yrs
    # examples that FAIL this check: twenty-three, too old, twenty-two
    if some_age.isdigit() or some_age[0:2].isdigit():
        
         # check if the length of age (passed as the argument) is greater than 2
        #       AND the third character of the age (passed as the argument) is
        #       a digit
        #
        # examples that PASS this check: 200 yrs
        # examples that FAIL this check: 26years old, 25
        if len(some_age) > 2 and some_age[2].isdigit():
            
            # get the first three characters of the age (passed as the argument)
            #     using string slicing, convert to an integer and store in a 
            #     NEW variable holding the cleanes value
            #
            # example CLEANED with this statement: 200 yrs becomes 200
            age = int(age[0:3])

        # otherwise (i.e., the length of age is NOT greater than 2 AND the third
        #            character of the age is NOT a digit)
        #
        # examples that PASS this check: 26years old, 25, ... etc.
        else:
            # get the first two characters of the age (passed as the argument)
            #     using string slicing, convert to an integer and store in a
            #     NEW variable holding the cleaned value
            #
            # example CLEANED with this statement: 26years old becomes 26
            age = int(some_age[0:2])
            
            
        # check if the age (NEW variable created in previous check) is outside the 
        #       range of 1 to 150 for human lifespan
        #
        # examples that PASS this check: 200
        # examples that FAIL this check: 26, 25, ... etc. 
        if age < 0 or age > 150:
            
            # update the flag variable to be set to False since the cleaned age
            #     (NEW variable created in previous check) is invalid and outside
            #     of range
            valid = False
    # otherwise (i.e., age (passed as the argument) does NOT contain only digits)
    #
    # examples that PASS this check: twenty-three, too old, twenty-two
    else: 
        # update the flag variable to be set to False since the age
        #     (passed as the argument) is invalid and not an integer
        valid = False
    
    # return the flag variable that is either True or False depending on if the
    #    age of the respondent is valid after all above checks
    return valid


# function name: check_linear_scale
# argument(s): one string representing the rating given for a linear sclae question
# description: checks if rating contains only digits and if the rating is between
#              the scale of 1 to 5
# return: one boolean (i.e., either True or False) if the rating is valid
#             True if the rating is valid
#             False if the rating is invalid
def check_linear_scale(linear_question):
    
    # flag variable set to true assuming ratin is valid before checks
    valid = True
    
     # check if the rating (passed as the argument) only contains digits
     #  convert to an integer and store in a NEW variable holding the integer value 
    if linear_question.isdigit():
        
        linear = int(linear_question)
        
        # check if the rating (NEW variable created in previous line) is between
        #       1 and 5 for this linear rating scale question
        if linear < 1 or linear > 5:
            
            # update the flag variable to be set to False since the rating
            #     (NEW variable created in previous line) is invalid and outside
            #     the range of 1 and 5
            valid = False
            
     # otherwise (i.e, the rating (passed as the argument) does NOT only contain digits)
    else:
        
        # update the flag variable to be set to False since the rating
        #     (passed as the argument) is invalid and not an integer
        valid = False
    
    # return the flag variable that is either True or False depending on if the
    #    rating for the linear scale question is valid after all above checks
    return valid      
    
# function name: check_multiple_choice
# argument(s): one string representing the choice given for a multiple choice question
# description: checks if the choice for the multiple choice question is not empty and
#              is one of the provided choices for the question
# return: one boolean (i.e., either True or False) if the choice is valid
#             True if the choice is valid
#             False if the choice is invalid
def check_multiple_choice(multiple_choice):
    
    # flag variable set to True assuming choice is valid before checks
    valid = True
    
    # check is the choice (passed as the argument) for the multiple choice questions is NOT empty
    if multiple_choice != "" or multiple_choice != None: 
        
        # check if the choice (passed as the argument) for the multiple choice questions is NOT 
        #       equal to any of the provided choices for the multiple choice question
        if multiple_choice != "Israel" and multiple_choice != "Mauritius" and multiple_choice != "South Sudan" and multiple_choice != "Ethiopia": # ???
            
            # update the flag variable to be set to False since the choice 
            #        (passed as the argument) is invalid and not one of the provided
            #        choices for the multiple choice question
            valid = False
            
     # otherwise (i.e, the choice (passed as the argument) is empty)
    else:
        
        # update the flag variable to be set to False since the choice
        #        (passed as the argument) is invalid and cannot be empty
        valid = False
        
    # return the flag variable that is either True or False depending on if the
    #    choice for the multiple choice question is valid after all above checks
    return valid 
            
            
# function name: read_csv
# argument(s): one string representing the file name of the survey responses CSV file
# description: opens/reads the survey responses CSV file and checks/cleans invalid data
#              entries in each row of the CSV file
#              checks that the age, linear scale and multiple choice responses are valid
#              by calling the helper functions defined above
#              outputs error messages if the entries cannot be cleaned and what values have
#              been skipped
#              appends valid/cleaned entries for linear scale responses to lists
#              updates accumulator variables counting number of responses for each choice
#                  in a multiple choice question
# return: 1 lists containing valid/cleaned responses for linear scale question
#         AND 4 integers containing counts for 4 choices in the multiple choice question              
def read_csv(filename):
    
    # create empty list to store linear scale question in CSV file
    ratings = []
    
    # create variable(s) to store count of multiple choice otpions and set equal to 0
    mul_choice1 = 0
    mul_choice2 = 0
    mul_choice3 = 0
    mul_choice4 = 0

    # open the survey responses CSV file to read it
    with open(filename) as csv_infile:

        # reader is the Python object to read the CSV file
        reader = csv.DictReader(csv_infile)
        
        # output that the survey responses CSV file is read and cleaned
        print("Reading and cleaning survey.csv.....\n")

        # this for loop takes each row of the CSV file and calls it "row"
        for row in reader:
            
            # check if the age in the row is valid by:
            #       CALLING check_age function
            #       AND
            #       PASSING the age in the row
            if check_age(row["How old are you?"]):
                
                # check if the response for the linear scale question in the row is valid by:
                #       CALLING check_linear_scale function
                #       AND
                #       PASSING the response for the first linear scale question in the row
                if check_linear_scale(row["The more freedom there is to make life choices the more people are happy (with 1 being strongly disagree, 2 being disagree, 3 neutral, 4 agree, 5 strongly agree)."]):
                    
                    # append valid integer digit between 1 and 5 to list storing values 
                    #        for first linear scale question
                    ratings.append(int(row["The more freedom there is to make life choices the more people are happy (with 1 being strongly disagree, 2 being disagree, 3 neutral, 4 agree, 5 strongly agree)."]))
                    
                # otherwise (i.e., response for the first linear scale question in the row is invalid)
                else:
                    
                    # output error message with line number and invalid data entry and skip bad data value
                    print("Error on line", reader.line_num, row["The more freedom there is to make life choices the more people are happy (with 1 being strongly disagree, 2 being disagree, 3 neutral, 4 agree, 5 strongly agree)."], "is not a valid response. Bad data value skipped")
            
             # check if the choice for the multiple choice question in the row is valid by:
                #       CALLING check_multiple_choice function
                #       AND
                #       PASSING the choice for the multiple choice question in the row
                if check_multiple_choice(row["Which African country do you think had the highest happiness rank in 2020?"]) == True:
                    
                    # count the number of responses for each of the valid choices in this multiple choice question
                    #       and add to the 4 variables storing the counts for each of these choices
                    mul_choice1 += row["Which African country do you think had the highest happiness rank in 2020?"].count("Israel")
                    mul_choice2 += row["Which African country do you think had the highest happiness rank in 2020?"].count("Mauritius")
                    mul_choice3 += row["Which African country do you think had the highest happiness rank in 2020?"].count("South Sudan")
                    mul_choice4 += row["Which African country do you think had the highest happiness rank in 2020?"].count("Ethiopia")
                    
                    
                # otherwise (i.e., choice for the multiple choice question in the row is invalid)
                else:
                    
                    # output error message with line number and invalid data entry and skip bad data value
                    print("Error on line", reader.line_num, ":", row["Which African country do you think had the highest happiness rank in 2020?"], "Empty or invalid choice. Bad data value skipped.")
                    
            # otherwise (i.e., the age in the row is invalid)    
            else:
                
                # output error message with line number and invalid data entry and skip bad data value
                print("Error on line", reader.line_num, ":", row["How old are you?"], "-->", "Not an integer or outside of range between 0 and 150. Bad data value skipped.")
                
    
    # output that the CSV file has been cleaned
    print("\nsurvey.csv has been cleaned!\n\n\n")
    
    # return list containing valid/cleaned responses for linear scale question
    #         AND 4 integers containing counts for 4 choices in the multiple choice question
    return ratings, mul_choice1, mul_choice2, mul_choice3, mul_choice4          


# function name: plt_linear_rating
# arguments(s): one list containing integer ratings to the linear scale questions
# description: plots a histogram of the ratings for the linear scale question
# return: none
def plt_linear_rating(some_list):
    
    # plot a histogram using
    plt.hist(some_list, bins = 5)
    
    # give appropiate title and y label
    plt.title("Freedom to make life choices makes people happier")
    plt.ylabel("Rating (1 = Strong Disagree to 5 = Strongly Agree)")
    
    # give appropiate x and y ticks
    plt.xticks([1,2,3,4,5], ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
    
    
    # display the histogram graph
    plt.show()

    
# function name: plt_counts
# argument(s): 4 integer variables storing the counts for each choice in the 
#              multiple choice question
# description: plots a pie chart of the counts for each choice in the multiple choice question
# return: none     
def plt_counts(ct_opt1, ct_opt2, ct_opt3, ct_opt4):
    
    # create a list storing the values of all 4 variables with the counts for each choice 
    #        in the multiple choice question
    counts = [ct_opt1, ct_opt2, ct_opt3, ct_opt4]    
    
    # create a list of the string labels containing all the listed choice from the multiple
    #        choice question that is being plotted in this pie chart
    slice_labels = ['Israel', 'Mauritius', 'South Sudan', 'Ethiopia']
    
    # create a pie chart using the two lists created in the previous lines for
    #        the counts and labels
    plt.pie(counts, labels = slice_labels, autopct = "%.2f")
    
    # give appropriate title
    plt.title("Which African country had the highest happiness rank in 2020?")
    
    # plot the legend in the upper right corner
    plt.legend(bbox_to_anchor=(2,0.8), loc="upper right")
    
    # display the pie chart
    plt.show()
    
    
# function name: compute
# argument(s): 1 list containing ratings for linear scale question
# description: computes a data statistic using the numpy module (i.e, mean, median, standard deviation) with the ratings for linear scale question
# return: 3 float containing the computed data statistic on the list of ratings passed to it 
def compute(l_ratings):
    
    # create a variable storing the mean/average of ratings from the linear scale question
    average_ratings = np.mean(l_ratings)
    
    # create a variable storing the median of ratings from the linear scale question
    median_ratings = np.median(l_ratings)
    
    # create a variable storing the standard deviation of ratings from the linear scale question
    std_ratings = np.std(l_ratings)
    
    # return 3 float variables containg the computed data statistcs (mean, median, standard deviation)
    return average_ratings, median_ratings, std_ratings


# function name: main
# argument(s): none
# description: setups the program and manages calls to functions defined above for specified output 
# return: none    
def main():
    
    # create a variable to store the name of the survey responses CSV file as a string
    file = "survey.csv"
    
    # CALL read_csv function
    #      PASSING it the variable storing the name of CSV file
    #      STORING 5 RETURN VALUES in 5 different variables
    lratings, mchoice1, mchoice2, mchoice3, mchoice4 = read_csv(file)
    
    # CALL plt_linear_rating function
    #      PASSING it the variable storing ratings for the linear scale question
    #      STORING 1 RETURN value in 1 variable
    plt_linear_rating(lratings)
    
    # CALL compute function
    #      PASSING it the variable storing ratings for the linear scale question
    #      STORING 3 RETURN VALUES in 3 different variables
    average, median, std = compute(lratings)
    
    print("The computed average rating from the linear scale question is", format(average, '.02f'))
    print("The computed median rating from the linear scale question is", median)
    print("The computed standard deviation of ratings from the linear scale question is", format(std, '.02f'),"\n\n\n")
    
    # CALL plt_counts function
    #      PASSING it 4 variables storing the counts for the 3 choices in the multiple choice question
    #      (these are 4 of the 5 variables created in previous line with RETURN value from read_csv function)
    plt_counts(mchoice1, mchoice2, mchoice3, mchoice4)
    
    
# CALL the main function to run the program
main()


# In[ ]:




