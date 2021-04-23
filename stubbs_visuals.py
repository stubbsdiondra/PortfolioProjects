#!/usr/bin/env python
# coding: utf-8

# In[45]:


# Diondra Stubbs
# CSC 201 - SPRING 2021
# PROGRAMMING WITH DATA USING LISTS
# 26 MARCH 2021
#
# PROGRAM TITLE: African Happiness Visuals Program
#
# PROGRAM DESCRIPTION: A Python program that creates four different types of visualizations 
#                      based on the data from the 2015, 2016, 2017, 2018, 2019 and 2020 World 
#                      Happiness Report. Additionally, this program also computes basic 
#                      calculations such as minimum, maximum and average on this same data.
#
# GENERAL SOLUTION: This is a modularized Python program that breaks all tasks required for 
#                   this program into several functions in order to easily reuse code and 
#                   avoid code duplication. It uses the following functions:
#
#                   scatter_visual: This function creates and outputs a scatter chart based on
#                                   the lists of x and y coordinates it receives as arguments.
#
#                   line_visual: This function creates and outputs a line chart based on the 
#                                lists of x and y coordinates it receives as arguments.
#
#                   bar_visual: This function creates and outputs a bar chart based on the 
#                               lists of x-coordinates of each bar’s left edge and heights 
#                               of each bar along the y-axis it receives as arguments.
#
#                   pie_visual: This function creates and outputs a pie chart based on the 
#                               lists of values and slice labels it receives as an argument.
#
#                   minimum_val: This function finds the minimum value in a list that 
#                                it receives as an argument.
#
#                   maximum_val: This function finds the maximum value in a list.
#
#                   average_val: This function finds the average value of a list that it receives 
#                                as an argument.
#
#                   main: This function setups the program and manages calls to functions defined 
#                         for creating the visualization and computing simple calculations.
#
#
# PSEUDOCODE: Output scatter plot showing the social support values of Mauritius from 2015 to 2020.
#             Output the minimum, maximum and average social support value between 2015 and 2020.
#             Output line chart showing the overall happiness scores of Africa from 2015 to 2020.
#             Output the minimum, maximum and average happiness scores between 2015 and 2020.
#             Output bar graph showing the happiness scores of Mauritius from 2015 to 2020.
#             Output the minimum, maximum and average happiness scores between 2015 and 2020.
#             Output pie graph displaying survey responses from users who chose which African 
#                country is the happiest.
#             Output the minimum, maximum and average response from the survey question.


# import the matplotlib library
import matplotlib.pyplot as plt

# function name: scatter_visual
# arguments: 2 integer lists where one contains the x-coordinates and the other contains the y-coordinates
# return: none
# description: creates and outputs a scatter chart based on the lists of x and y coordinates it received as arguments

def scatter_visual(x_coords, y_coords):
    
    # plot the given lists of x and y coordinates as a scatter chart
    x_coords = [0, 1, 2, 3, 4, 5]
    y_coords = [0.98, 0.76, 1.21, 1.39, 1.40, 0.91]
    
    plt.scatter(x_coords, y_coords)
    
    # give appropiate title, x-axis and y-axis labels, and grid layout
    plt.title("Mauritius Social Support Overtime")
    plt.xlabel("Year")
    plt.ylabel("Social Support")
    
    # customize the x tick marks along the x-axis and y-axis
    plt.xticks([0, 1, 2, 3, 4, 5], ['2015', '2016', '2017', '2018', '2019', '2020'])
    
    # show the scatter chart
    plt.show()
    

# function name: line_visual
# arguments: 2 integer lists where one contains the x-coordinates and the other contains the y-coordinates
# return: none
# description:creates and outputs a line chart based in the lists of x and y coordinates it received as arguments

def line_visual(x_coords, y_coords):
    
    # plot the given lists of x and y coordinates as a line chart using marker
    x_coords = [0, 1, 2, 3, 4, 5]
    y_coords = [4.30, 4.27, 4.24, 4.33, 4.31, 4.43]
    
    plt.plot(x_coords, y_coords)
    
    # give appropiate title, x-axis and y-axis labels, and grid layout
    plt.title("Africa Happiness Scores from 2015 to 2020")
    plt.xlabel("Year")
    plt.ylabel("Happiness Scores")
    
    # customize the x tick marks along the x-axis and y-axis
    plt.xticks([0, 1, 2, 3, 4, 5], ['2015', '2016', '2017', '2018', '2019', '2020'])
    
    # show the line chart 
    plt.show()
    

# function name: bar_visual
# arguments: 2 integer lists where one contains the x-coordinates of each bar's left edge and heights of each bar along y-axis it receives as arguments
# return: none
# description: creates and outputs a bar chart based on the lists of x-coordinates of each bar’s left edge and heights of each bar along y-axis it receives as arguments

def bar_visual(left_edges, heights):
    
    # plot the years and happiness scores as a bar chart
    left_edges = [0, 1, 2, 3, 4, 5]
    heights = [5.48, 5.65, 5.63, 5.89, 5.89, 6.10]
    
    plt.bar(left_edges, heights, color={'r','m','g','k','b','c'})
    
    # give appropriate title and x-axis and y-axis labels
    plt.title("Mauritius Happiness Scores from 2015 to 2020")
    plt.xlabel("Year")
    plt.ylabel("Happiness Scores")
    
    # customize the x tick marks along the x-axis and y-axis
    plt.xticks([0, 1, 2, 3, 4, 5], ['2015', '2016', '2017', '2018', '2019', '2020'])
    
    # show the bar chart
    plt.show()
    

# function name: pie_visual
# arguments: 2 lists where one contains integer values for the slice sizes and the other contains 
#             the labels of the slices
# return: none
# description: creates and outputs a pie chart based on the lists of values and slice labels it 
#                receives as an argument

def pie_visual(happiest_country, slice_labels):
    
    # plot the list of percentages and labels as a pie chart
    happiest_country = [12, 12, 24, 52]
    
    slice_labels = ['Mauritius', 'South Sudan', 'Ethiopia', 'Israel']
    
    # plot the legend in the upper right corner to show the labels/colors of each slice in the pie chart
    plt.pie(happiest_country, labels = slice_labels, colors={'k', 'm', 'r', 'c'})
    
    # give appropriate title 
    plt.title('Which African Country is the Happiest?')
    
    # show the pie chart
    plt.show()
    
    
# function name: minimum_val
# arguments - 1 list containing integer values
# return - 1 integer that is the minimum value in the list that it receives as an argument
# description: : finds the minimum value in a list that it receives as an argument

def minimum_val(some_list):
    
    minimum = some_list[0]
    
    for i in some_list:
        
        if i < minimum:
            minimum = i
            
    return minimum


# function name: maximum_val
# arguments - 1 list containing integer values
# return - 1 integer that is the maximum value in the list that it receives as an argument
# description: : finds the maximum value in a list that it receives as an argument

def maximum_val(some_list):
    
    maximum = some_list[0]
    
    for i in some_list:
        
        if i > maximum:
            maximum = i
    
    return maximum


# function name: average_val
# arguments - 1 list containing integer values
# return - 1 integer (or float) that is the average of the list
# description: : finds the average value of a list that it receives as an argument

def average_val(some_list):
    
    total = 0
    
    for value in some_list:
        total += value
        
    average = total / len(some_list)
    
    return average
    
    
# function name: main
# arguments: none
# return: none
# description: sets ups the program and manages calls to functions defined for creating the visualization and computing simple data statistics

def main():
    
    # create a list of years and social support
    x_coords = [0, 1, 2, 3, 4, 5]
    y_coords = [0.98, 0.76, 1.21, 1.39, 1.40, 0.91]
    
    # plots these lists as a scatter chart using scatter_visual function
    scatter_visual(x_coords, y_coords)
    
    social_support = [0.98, 0.76, 1.21, 1.39, 1.40, 0.91]
    
    # calculate and output the minimum, maximum and average of social support
    min1 = minimum_val(social_support)
    print("Minimum Social Support of Mauritius from 2015 to 2020:", min1)
    
    max1 = maximum_val(social_support)
    print("Maximum Social Support of Mauritius from 2015 to 2020:", max1)
    
    avg1 = average_val(social_support)
    print("Average Social Support Score of Mauritius from 2015 to 2020:", avg1)
    
    # create a list of years and happiness scores of Africa
    x_coords = [0, 1, 2, 3, 4, 5]
    y_coords = [4.30, 4.27, 4.24, 4.33, 4.31, 4.43]
    
    
    # plot these lists as a line chart using line_visual function
    line_visual(x_coords, y_coords)
    african_happiness = [4.30, 4.27, 4.24, 4.33, 4.31, 4.43]
    
    # calculate and output the minimum, maximum and average of happiness scores of  Africa between 2015 and 2020
    min2 = minimum_val(african_happiness)
    print("Minimum African Happiness Score between 2015 and 2020:", min2)
    
    max2 = maximum_val(african_happiness)
    print("Maximum African Happiness Score between 2015 and 2020:", max2)
    
    avg2 = average_val(african_happiness)
    print("Average African Happiness Score between 2015 and 2020:", avg2)
    
    
    # create a list of years and happiness scores of Mauritius
    left_edges = [0, 1, 2, 3, 4, 5]
    heights = [5.48, 5.65, 5.63, 5.89, 5.89, 6.10]
    
    # plot these lists as a bar chart using bar_visual function
    bar_visual(left_edges, heights)
    mauritius_happiness = [5.48, 5.65, 5.63, 5.89, 5.89, 6.10]
    
    # calculate and output the minimum, maximum and average of happiness scores 
    min3 = minimum_val(mauritius_happiness)
    print("Minimum Mauritius Happiness Score between 2015 and 2020:", min3)
    
    max3 = maximum_val(mauritius_happiness)
    print("Maximum Mauritius Happiness Score between 2015 and 2020:", max3)
    
    avg3 = average_val(mauritius_happiness)
    print("Average Happiness Score of Mauritius between 2015 and 2020:", avg3)
    
    
    # create a list of percentages for the user responses to statements provided in survey question about the happiest country in africa
    happiest_country = [12, 12, 24, 52]
    
    # create labels for respective slices in the pie chart
    slice_labels = ['Mauritius', 'South Sudan', 'Ethiopia', 'Israel']
    
    # plot these lists as a pie chart using pie_visual function
    pie_visual(happiest_country, slice_labels)
    happiest_country = [12, 12, 24, 52]
    
    # calculate and output the minimum, maximum and average of user responses
    min4 = minimum_val(happiest_country)
    print("Minimum Response:", min4)
    
    max4 = maximum_val(happiest_country)
    print("Maximum Response:", max4)
    
    avg4 = average_val(happiest_country)
    print("Average Response:", avg4)
    
    
# call the main function to run the program
main()


# In[ ]:




