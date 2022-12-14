# Air Quality Analysis Project

This project analyzes an air quality dataset that contains the responses of a gas multisensor device deployed on the field in an Italian city. Some exploratory data analysis, a regression analysis and model selection is performed in Python using Pandas, Numpy, Sesborn and Scikit-learn for this project. Each python notebook has markdown explaining each part of my analysis.

![This is an image](https://github.com/stubbsdiondra/PortfolioProjects/blob/main/Air%20Quality%20Analysis%20Project/pollution-italy.jpg)

## About the Dataset

This dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level,within an Italian city. Data were recorded from March 2004 to February 2005 (one year)representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. More about this [dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality)

### Dataset Features
Date (DD/MM/YYYY)
Time (HH.MM.SS)
CO(GT) - True hourly averaged concentration CO in mg/m^3 (reference analyzer)
PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)
NMHC(GT) - True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer)
C6H6(GT) - True hourly averaged Benzene concentration in microg/m^3 (reference analyzer)
PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)
NOx(GT) - True hourly averaged NOx concentration in ppb (reference analyzer)
PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)
NO2(GT) - True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)
PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)
PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)
T - Temperature in Â°C
RH - Relative Humidity (%)
AH - Absolute Humidity

## Regression Task

The task is to predict the Air Quality given the other measurements in the dataset.

The dataset has columns Date, Time, CO(GT), PT08.S1(CO), NMHC(GT), C6H6(GT), PT08.S2(NMHC), NOx(GT), PT08.S3(NOx), NO2(GT), PT08.S4(NO2), PT08.S5(O3), T, RH, and AH. The desired target variable is the temperature (T).

## Why Predict Air Quality

Being able to model, predict, and monitor air quality is becoming more and more relevant, especially in urban areas, due to the critical impact of air pollution on citizens’ health and the environment. Accurate forecasting helps people plan ahead, decreasing the effects on health and the costs associated.

## Findings

The R^2 (coefficient of determination) of the regression model is 0.9299834598762752. or ~93% meaning that ~93% of the data points fall on the regression line and ~93% of the independent/predictor variables in this model explain all the variation in y (Temperature).

The residuals show us that the residuals are spread out around the regression line but pretty close to it.

The coefficients tell us the relationship between the temperature and the other features. When the temperature increases by one C6H6 decreases by 0.41, PT08.S2(NMHC) increases by 0.009, NOx increases by 0.001, PT08.S3(NOx) increases by 0.001, NO2 decreases by 0.003, PT08.S4(NO2) increases by 0.005, RH decreases by 0.349 and AH increases by 14.39.

The MSE is 5.18. In other words, the average squared difference between the observed and predicted values is 5.18.

The predictors aren't perfect but it is a good fit, given that ~93% of the independent/predictor variables in this model explain all the variation in y and the amount of error in a model isn't extreme. Therefore, the model fits the data well.

This model would be pretty accurate at predicting air quality, allowing people to plan ahead, decreasing the effects on health and the costs associated.
