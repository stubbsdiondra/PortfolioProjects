#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# CLEANING, SUMMARIZING & VISUALIZING DATAFRAMES
# 16 APRIL 2021
#
# PROGRAM TITLE: 
#
# PROGRAM DESCRIPTION: A modularized Python program that reads all the records from the 2020 World Happiness Report
#                      data set found online into a Pandas DataFrame, visually inspects and cleans the DataFrame 
#                      for common data errors, and creates summary tables and visualizations from the cleaned 
#                      DataFrame.
#
# GENERAL SOLUTION: This program breaks down the tasks required for this program into several functions including:

#                   read_as_dataframe: This function converts data in a CSV file to a Pandas DataFrame
#                   
#                   visually_inspect: visually inspects the DataFrames to diagnose it for common data errors
#
#                   cleaning: clean the data errors in the Pandas DataFrame indentified in visual inspection
#
#                   get_continent_subset: creates filtered subset(s) on the cleaned DataFrame to help narrow it 
#                                         down and perform computations on particular information that will serve 
#                                         as supporting evidence to some of the questions posed about this topic 
#
#                   africa_pivot: creates a pivot table containing happiness scores for each country in just Africa
#
#                   africa_pivot_line_chart: creates a line chart with a trendline for the happiness scores vs healthy
#                                            life expectancy in Africa
#
#                   african_countries_pivot: creates a pivot table containing happiness scores for each country in 
#                                            Africa
#
#                   african_countries_pivot_bar_chart: creates a bar chart for the happinesss scores by country for 
#                                                      Africa
#
#                   africa_social_pivot: creates a pivot table containing social support and happiness scores for each 
#                                        country in just Africa
#
#                   africa_social_scatter_chart: creates a scatter chart with a trendline for the social support of 
#                                                African countries by happiness score
#
#                   african_social_pivot2: creates a pivot table containing social support scores for each country 
#                                          in Africa
#
#                   african_social_bar_chart: creates a bar chart for the social support scores by country for Africa
#
#                   main: sets up the program and manages calls to functions defined for reading the CSV file into 
#                         a Pandas DataFrame, visually inspects and cleans the DataFrame of common data errors, 
#                         and creates summary tables and visualizations from the cleaned DataFrame and its filtered 
#                         subsets.
#
#
# PSEUDOCODE: Import pandas, matplotlib, numpy and scipy.stats libraries for this program to work
#             Read the CSV file into a Pandas DataFrame
#             Output the frequency of values in each column of the Pandas DataFrame to identify 
#                duplicate values, NaN values or incorrectly formatted numbers.
#             Clean the data frame by dropping any NaN (missing) values and duplicated rows
#             Output description of the data frame to make sure each column is read in as the right type 
#               (i.e. - float, object, etc)
#             Output value counts on the cleaned data frame to make sure the common data errors have been fixed 
#             Output cleaned filtered subset for countries only in Africa
#             Output pivot table for Africa's Happiness scores in 2020
#             Plot a line chart showing the relationship between Healthy Life Expectancy and Happiness Scores for Africa
#             Output pivot tables for Africa's Happiness scores by country
#             Output bar chart showing each country's happiness score in 2020
#             Output pivot table for Africa's Happiness scores by social support
#             Output a scatter chart showing the relationship between Africa's social support and happiness scores in 2020
#             Output pivot table for Africa's social support scores in 2020
#             Output bar chart showing each country's social support score in 2002

# import libraries needed for this program
import pandas as pd, matplotlib.pyplot as plt, numpy as np
from scipy.stats import linregress

# function name: read_as_dataframe
# argument(s): 1 string representing the name of the CSV file
# return: 1 Pandas DataFrame
# description: converts data in a CSV file to a Pandas DataFrame
def read_as_dataframe(file):
    
    # read CSV file into pandas dataframe
    df = pd.read_csv(file)
    
    # return pandas dataframe containing data from csv file
    return df 


# function name: visually_inspect
# argument(s): 1 Pandas DataFrame
# return: None
# description: visually inspects the DataFrames to diagnose it for common data errors
def visually_inspect(df):
    
    # output the # or rows/columns and data types of each column in dataframe
    print(df.info())
    print('\n\n')
    
    # output the frequency of each value in the Country Name column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Country Name'].value_counts(dropna = False))
    print('\n\n')
        
    # output the frequency of each value in the Regional Indicator  column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Regional Indicator'].value_counts(dropna = False))
    print('\n\n')
    
    # output the frequency of each value in the Happiness Scores column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Happiness Scores'].value_counts(dropna = False))
    print('\n\n')
    
    # output the frequency of each value in the Social Support column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Social Support'].value_counts(dropna = False))
    print('\n\n')
    
    # output the frequency of each value in the Healthy Life Expectancy column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Healthy Life Expectancy'].value_counts(dropna = False))
    print('\n\n')
    
    # output the frequency of each value in the Freedom to Make Life Choices column to identify 
    #    duplicate or NaN values or strings or incorrectly formatted numbers
    print(df['Freedom to Make Life Choices'].value_counts(dropna = False))
    print('\n\n')
    
    # output columns with numerical type to see which columns are not being 
    #        recognized as numerical
    print(df.describe())
    print('\n\n')
    
    
# function name: cleaning
# argument(s): 1 Pandas DataFrame with csv data
# return: 1 cleaned Pandas DataFrame
# description: clean the data errors in the Pandas DataFrame indentified in visual inspection
def cleaning(df):
    
    # drop any NaN (missing) values from the DataFrame
    df.dropna(inplace = True)
    
    # drop duplicates
    df.drop_duplicates(inplace = True)
    
    
    # reset the index numbers of the DataFrame after these changes
    #       have been applied
    df.reset_index(drop = True, inplace = True)
    
    # return the cleaned df
    return df
    
    
# function name: get_continent_subset
# arugment(s):1 Pandas DataFrame that has been cleaned (i.e., the cleaned DataFrame without data errors)
# return: 1 subset of the Pandas DataFrame 
# description: creates filtered subset(s) on the cleaned DataFrame to help narrow it down and perform 
#              computations on particular information that will serve as supporting evidence to some of 
#              the questions posed about this topic
def get_continent_subset(df, continent):
    
    country_filter = df['Regional Indicator'] == continent
    
    africa_sub = df[country_filter]
    
    return africa_sub
    
    
# function name: africa_pivot
# argument(s): 1 filtered subset of a DataFrame containing only data on Africa
# return: 1 pivot table containing happiness scores by country for Africa
# description: creates a pivot table containing happiness scores for each country in just Africa
def africa_pivot(africa_sub):
    
    # create a pivot table calcuating the median of the happiness scores
    #        of each country in Africa in the subset containing all data 
    #        on Africa
    africa_pivot = africa_sub.groupby("Happiness Scores", as_index = False).median()
    
    # reset the index
    africa_pivot.reset_index(inplace = True)
    
    # return the pivot table
    return africa_pivot


# function name: africa_pivot_line_chart
# argument(s): 2 columns from a given pivot table as x and y values to plot
# return: None
# description: creates a line chart with a trendline for the happiness scores vs healthy life expectancy in Africa
def africa_pivot_line_chart(x, y):
    
    # create a line chart using passed x and y values from a pivot table
    plt.plot(x, y)
    
    # give chart appropiate title, x and y labels, legend
    plt.title("Africa: Healthy Life Expectancy vs. Happiness Scores")
    plt.xlabel("Healthy Life Expectancy")
    plt.ylabel("Happiness Scores")
    
    #show the chart
    plt.show()
    

# function name: african_countries_pivot
# argument(s): 1 filtered subset of a DataFram containg data only on Africa
# return: 1 pivot table containing happiness scores by country for Africa
# description: creates a pivot table containing happiness scores for each country in Africa
def african_countries_pivot(africa_sub):
    
    # create a pivot table calculating the median of happiness scores of each country
    africa_countries_pivot = africa_sub.pivot_table(values = "Happiness Scores", index = "Country Name", aggfunc = np.min, margins = False)
        
    # reset the index of pivot table
    africa_countries_pivot.reset_index(inplace = True)
    
    # return the pivot table
    return africa_countries_pivot  


# function name: african_countries_pivot_bar_chart
# argument(s): 1 pivot table with happiness scores of countries in Africa
# return: None
# description: creates a bar chart for the happiness scores by country for Africa
def african_countries_pivot_bar_chart(african_countries2_pivot):
    
    # create a bar chart using passed pivot table
    african_countries2_pivot.plot(kind = "bar")
    
    # adjust x ticks to show country names
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], ["Algeria", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Egypt", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Senegal", "Sierra Leone", "South Africa", "South Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"])
    
    # give chart appropiate title, x and y labels, legend
    plt.title("African Countries Happiness Scores")
    plt.xlabel("Countries")
    plt.ylabel("Happiness Scores")
    plt.legend(bbox_to_anchor = (1.5, 1), loc = "upper right")
    
    # show the chart
    plt.show()
    

# function name: africa_social_pivot 
# argument(s): 1 filtered subset of a DataFrame containing only data on Africa
# return: 1 pivot table containing happiness scores by country for Africa
# description: creates a pivot table containing social support and happiness scores for each country in just Africa
def africa_social_pivot(africa_sub):
    
    # create a pivot table calcuating the median of the happiness scores
    #        of each country in Africa in the subset containing all data 
    #        on Africa
    africa_social_piv = africa_sub.pivot_table(values = "Social Support", index = "Happiness Scores", aggfunc = np.min, margins = False)
    
    # reset the index
    africa_social_piv.reset_index(inplace = True)
    
    # return the pivot table
    return africa_social_piv


# function name: africa_social_scatter_chart
# argument(s): 2 columns from a given pivot table as x and y values to plot
# return: None
# description: creates a scatter chart with a trendline for the social support of African countries by happiness score
def africa_social_scatter_chart(x, y):
    
    # create a trendline using built-in scipy function linregress using passed x and y values
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    
    # create a line chart using passed x and y values from a pivot table
    plt.scatter(x, y)
   
    # plot the trendline on this scatter chart with label 
    plt.plot(x, intercept + slope*x, 'r', label = 'fitted line')
    
    # give chart appropiate title, x and y labels, legend
    plt.title("Africa: Social Support vs. Happiness Scores")
    plt.xlabel("Social Support")
    plt.ylabel("Happiness Scores")
    
    #show the chart
    plt.show()


# function name: african_social_pivot2
# argument(s): 1 filtered subset of a DataFrame containg data only on Africa
# return: 1 pivot table containing happiness scores by country for Africa
# description: creates a pivot table containing social support scores for each country in Africa
def african_social_pivot2(africa_sub):
    
    # create a pivot table calculating the median of happiness scores of each country
    africa_social_pivot2 = africa_sub.pivot_table(values = "Social Support", index = "Country Name", aggfunc = np.min, margins = False)
        
    # reset the index of pivot table
    africa_social_pivot2.reset_index(inplace = True)
    
    # return the pivot table
    return africa_social_pivot2  


# function name: african_countries_pivot_bar_chart
# argument(s): 1 pivot table with happiness scores of countries in Africa
# return: None
# description: creates a bar chart for the social support scores by country for Africa
def african_social_bar_chart(african_social_pivot):
    
    # create a bar chart using passed pivot table
    african_social_pivot.plot(kind = "bar")
    
    # adjust x ticks to show country names
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], ["Algeria", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Egypt", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Senegal", "Sierra Leone", "South Africa", "South Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"])
    
    # give chart appropiate title, x and y labels, legend
    plt.title("African Countries Social Support")
    plt.xlabel("Countries")
    plt.ylabel("Social Support")
    plt.legend(bbox_to_anchor = (1.5, 1), loc = "upper right")
    
    # show the chart
    plt.show()

# function name: main 
# arugment(s): None
# return: None
# description: set ups the program and manages calls to functions defined for reading the CSV file into a Pandas 
#              DataFrame, visually inspects and cleans the DataFrame of common data errors, and creates summary 
#              tables and visualizations from the cleaned DataFrame and its filtered subsets.
def main():
    
    # CSV file path and name
    filename = "stubbs_africahappiness.csv"
    
    # read in CSV file as a pandas dataframe
    df = read_as_dataframe(filename)
    
    # visually inspect our dataframe for errors
    # original dataframe has 155 rows
    # several errors including:
    #         a. remove any NaN(missing) values in the dataframe especially in
    #            the Country Name, Regional Indicator, Social Support and Healthy
    #            Life Expectancy columns
    #         b. drop any duplicate rows in the dataframe
    visually_inspect(df)
    
    
    # call cleaning function to clean all columns with data errors described in previous comment above
    #      reassigned df to the cleaned dataframe
    cleaned_df = cleaning(df)
    
    
    # after cleaning the DataFrame, it now has 153 rows
    # resolved data errors include:
    #          a. removed any rows with NaN (missing) values in the DataFrame
    #          b. dropped any duplicate rows in the DataFrame
    #          c. reset the index after making all of these changes to the DataFrame
    visually_inspect(cleaned_df)
    
    
    africa_subset = get_continent_subset(cleaned_df, "Africa")
    print(africa_subset)
    
    
    # call the africa_pivot function to get pivot table for Africa
    africa_piv = africa_pivot(africa_subset)
    
    print("\nAFRICA: 2020 HAPPINESS SCORES PIVOT TABLE\n")
    # output this pivot table
    print(africa_piv)
    
    # call africa_pivot_line_chart function to plot the healthy life expectancy columns vs. happiness scores
    #      from this pivot table as a line chart
    africa_pivot_line_chart(africa_piv["Healthy Life Expectancy"], africa_piv["Happiness Scores"])
    
    # call the africa_happiness_pivot function to get the pivot table for African countries
    #      and their happiness scores
    pivot = african_countries_pivot(africa_subset)
    
    # output pivot table broken down by country
    print("COUNTRIES IN AFRICA: 2020 HAPPINESS SCORES\n")
    print(pivot)
    
    # call african_countries_pivot_bar_chart function to plot pivot table broken down by country as a bar chart
    african_countries_pivot_bar_chart(pivot)
    
    
    # call the africa_social_pivot function to get the pivot table for African countries and their social 
    #      support scores and happiness scores
    social_pivot = africa_social_pivot(africa_subset)
    
    # output pivot table broken down country
    print("AFRICA: 2020 SOCIAL SUPPORT PIVOT TABLE\n")
    print(social_pivot)
    
    # call the africa_social_scatter_chart function to plot the social support vs. happiness scores
    #      from this pivot table as a scatter chart
    africa_social_scatter_chart(social_pivot["Social Support"], social_pivot["Happiness Scores"])
    
    
    # call the african_social_pivot2 function to get the pivot table for African countries and thier 
    #      social support
    social_pivot2 = african_social_pivot2(africa_subset)
    
    # output pivot table broken down by country 
    print("COUNTRIES IN AFRICA: 2020 SOCIAL SUPPORT SCORES\n")
    print(social_pivot2)
    
    # call african_social_bar_chart function to plot pivot table broken down by country as a bar chart 
    african_social_bar_chart(social_pivot2)
    
    
# call the main function to run the program
main()


# In[ ]:



