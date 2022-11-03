#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Diondra Stubbs
# AFRICA HAPPINESS FURTHER DATA ANALYSIS
# 23 APRIL 2021

###########################################################################################################
# START OF IMPORTS AND SETTINGS
###########################################################################################################

# import libraries needed for this program
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
###########################################################################################################
# END OF IMPORTS AND SETTINGS
###########################################################################################################

# reading in the 2020 World Happiness Report for countries in Africa
af_path = "africa_happinessreport.csv"
df = pd.read_csv(af_path)

# only need some of the columns of this data set
df = df[['Country name', 'Happiness Scores', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']]

# printing on the DataFrame created on the data set
df


# In[13]:


# function name: correlation_matrix
# argument(s): 1 Pandas DataFrame with csv data
# return: none
# description: creates a correlation matrix between the happiness scores, social support, healthy life expectancy,
#              freedom to make life choices, generosity and perceptions of corruption of countries in Africa
def correlation_matrix(df):
    plt.figure()
    sns.heatmap(df.corr(), center=0, annot=True, vmin=-1, vmax=1, cmap="RdBu_r")
    plt.savefig("correlations.png")
    
correlation_matrix(df)


# In[14]:


# Let's look into some regression analysis 

# First we prepare the data to use a model
reg_data = df.drop(["Country name"], axis=1)
y = reg_data["Happiness Scores"]
X = reg_data.drop(["Happiness Scores"], axis=1)

for feature in X.columns.values.tolist():
    X = reg_data.drop(["Happiness Scores"], axis=1)
    X = X[feature]
    X = X.values.reshape(-1,1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    plt.title("Regressions of " + feature)
    plt.scatter(X, y)

    degrees = [1,2,3,4]
    for degree in degrees:
        poly_features = PolynomialFeatures(degree=degree)

        # transforms the existing features to higher degree features.
        X_train_poly = poly_features.fit_transform(X_train)

        # fit the transformed features to Linear Regression
        poly_model = LinearRegression()
        poly_model.fit(X_train_poly, y_train)

        # predicting on test data-set
        y_test_predict = poly_model.predict(poly_features.fit_transform(X_test))

        # Plotting the regression

        new_x, new_y = zip(*sorted(zip(X_test, y_test_predict)))
        plt.plot(new_x, new_y, label="Degree = " + str(degree))

    plt.xlabel(feature)
    plt.ylabel("Happiness Scores")
    plt.legend()
    plt.show()
    plt.close()
    
# the outputted plots show how adjusted the regressions are with the data
