#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Diondra Stubbs
# CSC 201 - Spring 2021
# INTRODUCTION TO PYTHON & PROGRAMMING WITH DATA
# 26 FEBRUARY 2021

# PROGRAM TITLE: AFRICA HAPPINESS & SOCIAL SUPPORT APPROXIMATION PROGRAM

# PROGRAM DESCRIPTION: A Python program that approximates the average overall happiness scores 
#                      of the continent Africa from 2015 to 2020 and the average social support 
#                      factor in Africa between 2015 and 2020. 

# GENERAL SOLUTION: This program consists of the use of several variables such as integer and float,
#                   representing and storing data collected from the annual World Happiness Reports 
#                   from 2015 to 2020. These variables are used to compute the averages of happiness 
#                   scores and social support factors in Africa from 2015 to 2020. The calculations 
#                   to compute these averages, include the use of arithmetic operators such as 
#                   addition (+) and division (/). They also include variable operators. As a result, 
#                   this program outputs these averages using a print statement. The print statement 
#                   involves string formatting and concatenation to combine integers, floats and 
#                   strings in it’s output.

                   
#PSEUDOCODE:

# define integer variable to hold and compute the number of years between 2015 and 2020
# define float variables to hold the average happiness scores of Africa from years between 2015 and 2020
# define float variable to compute the average happiness scores of Africa from 2015 to 2020
# define float variables to hold the average social support factors of Africa from years between 2000 and 2015
# define float variable to compute the average social support factors of Africa from 2015 to 2020
# print average happiness scores and social support factors of Africa from 2015 to 2020


#######################################################################################################################
#                                                      SOLUTION
#######################################################################################################################
# On Thursday, February 25, 2021 at 8:00PM
# Africa Happiness Score Data
#    2015        4.30
#    2016        4.27
#    2017        4.24
#    2018        4.33
#    2019        4.31
#    2020        4.43
# https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv
#
# Africa Social Support Data
#    2015        0.81
#    2016        0.57
#    2017        0.96
#    2018        0.97
#    2019        0.91
#    2020        0.69
# https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv


# integer variable computes and holds the total number of years from 2015 to 2020
total_years = (2020 - 2015) + 1

# float variables storing average overall happiness scores of Africa from 2015 to 2020
happiness_avg_2015 = 4.30
happiness_avg_2016 = 4.27
happiness_avg_2017 = 4.24
happiness_avg_2018 = 4.33
happiness_avg_2019 = 4.31
happiness_avg_2020 = 4.43

# float variable stores the average happiness score of Africa from to 2015 to 2020
happiness_avg = (happiness_avg_2015 + happiness_avg_2016 + happiness_avg_2017 + happiness_avg_2018 + happiness_avg_2019 + happiness_avg_2020) / total_years

# float variables storing average overall social support factors of Africa from 2015 to 2020.
social_support_avg_2015 = 0.81
social_support_avg_2016 = 0.57
social_support_avg_2017 = 0.96
social_support_avg_2018 = 0.97
social_support_avg_2019 = 0.91
social_support_avg_2020 = 0.69

# float variable stores the average social support factor of Africa from to 2015 to 2020
social_support_avg = (social_support_avg_2015 + social_support_avg_2016 + social_support_avg_2017 + social_support_avg_2018 + social_support_avg_2019 + social_support_avg_2020) / total_years


#outputs the average happiness score and social support factor of Africa from 2015 to 2020
print("Happiness Score and Social Support Data Collected from the 2015, 2016, 2017, 2018, 2019 and 2020 World Happiness Reports")
print("----------------------------------------------------------------------------------------------------------------------------")
print("In Africa, the average happiness score over the period of " + str(total_years) + " years, from 2015 to 2020, was %0.2f." % happiness_avg)
print("In Africa, the average social support factor over the period of " + str(total_years) + " years, from 2015 to 2020, was %0.2f." % social_support_avg)


# In[ ]:



