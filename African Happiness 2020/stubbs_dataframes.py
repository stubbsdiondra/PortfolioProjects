#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING DATAFRAMES
# 9 APRIL 2021
#
# PROGRAM TITLE: Happiness Report DataFrames Program
#
# PROGRAM DESCRIPTION: A modularized Python program that reads the 2020 World Happiness Report 
#                      data set found online into a Pandas DataFrame. It creates filtered subsets 
#                      of the Pandas DataFrame containing all records in the original dataset to 
#                      only focus on particular continents such as Africa, Europe and Asia. This 
#                      program will output calculations on these continents by performing data 
#                      statistic calculations such as mean, median, maximum and minimum. This will 
#                      potentially help answer the question of "Which African country scored the 
#                      happiest in 2020?"  
#
# GENERAL SOLUTION: This program breaks down the tasks required for this program into several functions including:



#
#                   compute: This function computes ONE data statistics on the filtered subset of the Pandas 
#                            DataFrame
#
#                   output_stats: This function outputs the filtered subset AND the calculated data statistic 
#                                 on the subset
#
#                   main: This function set ups the program and manages calls to functions defined for specified 
#                         processing, calculations and output
#
# PSEUDOCODE: Output info about dataset to see the data type in each column
#
#             Output the head of the dataset to make sure CSV data is being read into a pandas dataframe correctly
#
#             Output filtered subsets to get data on Africa, Europe and Asia
#
#             Output computed data statistics on happiness scores of each continent 
#
#
# import the pandas library to read dataset found online into dataframe
import pandas as pd

# function name: read_as_dataframe
# argument(s): 1 string representing the name of the CSV file
# return: 1 Pandas DataFrame
# description: converts data in a CSV file to a Pandas DataFrame
def read_as_dataframe(file):
    
    # read CSV file into pandas dataframe
    df = pd.read_csv(file)
    
    # return pandas dataframe containing data from csv file
    return df 
    

# function name: get_subset
# argument(s): 1 Pandas DataFrame containing data from CSV file
# return: 1 subset of the Pandas DataFrame
# description: creates a filtered subset of the Pandas DataFrame
def get_subset(df, continent):
    
    country_filter = df['Regional Indicator'] == continent
    
    africa_sub = df[country_filter]
    
    return africa_sub


# function name: compute
# argument(s):  1 filtered subset of the Pandas DataFrame and 1 string representing the 
#               column name in the DataFrame you want to compute the data statistic on
# return: 1 computed data statistic on the given column name in the filtered subset of 
#         the Pandas DataFrame
# description: computes ONE data statistics on the filtered subset of the Pandas DataFrame
def compute(africa_sub, happiness):
    
    # compute the mean, median, max and min of African happiness scores
    mean_score = africa_sub[happiness].mean()
    median_score = africa_sub[happiness].median()
    min_score = africa_sub[happiness].min()
    max_score = africa_sub[happiness].max()

    # return the computed data statistics
    return mean_score, median_score, min_score, max_score

# function name: output_stats
# argument(s): 1 filtered subset of the DataFrame AND the calculated data statistic on the subset
# return: None
# description: outputs the filtered subset AND the calculated data statistic on the subset.
def output_stats(title, continent, subset, mean, median, minimum, maximum):
    
    # output the title of each continent AND its corresponding subset
    print(title)
    print(subset)
    
    #output the data stats for each continent
    print("\nThe overall Happiness Score in 2020 was", mean)
    print("The median of happiness scores was", median)
    print("The minimum happiness score in", continent, "was", minimum)
    print("The maximum happiness score in", continent, "was", maximum)
    
    

# function name: main
# argument(s): none
# return: none
# description: set ups the program and manages calls to functions defined for specified processing, 
#              calculations and output.
def main():
    
    # CSV file path and name
    filename = "stubbs_africahappiness.csv"
    
    # read in CSV file as a pandas dataframe
    df = read_as_dataframe(filename)
    
    df.info()
    
    # make sure CSV data is being read into a pandas dataframe correctly
    print('')
    print('')
    print(df.head()) 
    
    africa_subset = get_subset(df, "Africa")
    europe_subset = get_subset(df, "Europe")
    asia_subset = get_subset(df, "Asia")
    
    mean_afr, median_afr, minimum_afr, maximum_afr = compute(africa_subset, "Happiness Scores")
    mean_eur, median_eur, minimum_eur, maximum_eur = compute(europe_subset, "Happiness Scores")
    mean_asia, median_asia, minimum_asia, maximum_asia = compute(asia_subset, "Happiness Scores")
    
    output_stats("\n\n\t\t\t2020 Africa Statistics\n", "Africa", africa_subset, mean_afr, median_afr, minimum_afr, maximum_afr)
    output_stats("\n\n\t\t\t2020 Europe Statistics\n", "Europe", europe_subset, mean_eur, median_eur, minimum_eur, maximum_eur)
    output_stats("\n\n\t\t\t2020 Asia Statistics\n", "Asia", asia_subset, mean_asia, median_asia, minimum_asia, maximum_asia)
    
# call the main function to run the program
main()


# In[ ]:



