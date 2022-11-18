# 2020 World Happiness Project

This project analyzes the 2020 World Happiness Report to draw conclusions about the general well being of 153 countries in the world. The analysis is performed in Python. Each python notebook has markdown explaining each part of my analysis. I also added the analysis I did in R which is explained in a [predicitve analytics](https://docs.google.com/document/d/1MWESB-buBUXKKyxrG-zl6VXcT7JvmyMm6VWXq4wVDiQ/edit?usp=sharing) case study I did.

![This is an image](https://github.com/stubbsdiondra/PortfolioProjects/blob/main/World%20Happiness%202020%20Project/happiness.png)

This is renovation of college programming project I did in 2021. Original can be found [here](https://github.com/stubbsdiondra/Subjective-Wellbeing-Africa-2020)

## About the Dataset

This dataset contains the Happiness Score for over 150 countries for the year of 2020. The data gathered from the Gallup World Poll gives a national average of Happiness scores for countries all over the world. It is an annual landmark survey of the state of global happiness.

This dataset is from the data repository "Kaggle". On Kaggle's dataset page, I searched for Africa Happiness after filtering the search to CSV file type. I wasn't able to find any datasets that could answer my questions that didn't include other countries from different continents. I decided to use a Global Happiness Report to answer the questions I have. The dataset I am using was publish by Micheal Londeen and it was created on March 24, 2020. His main source is the World Happiness Report for 2020.

More about this [dataset](https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2020.csv).

## Dataset Features

### Dataset Features

1. Country Name
2. Regional Indicator
3. Happiness score (Ladder Score)
5. Healthy Life Expectancy (HLE)
6. Social support
7. Freedom to make life choices
8. Generosity
9. Perceptions of Corruption

Explanation of the [features](https://happiness-report.s3.amazonaws.com/2020/WHR20_Ch2_Statistical_Appendix.pdf).

## The Project

This project does some basic data wrangling and exploratory data anlysis to answer the following questions:

EDA Questions
1. Which country has the highest score? Why?
2. How many observations are there?
3. Are there any null values? How does this dataset need to be cleaned?
4. Is there any correlation between the features?
5. Are the minimum and maximum happiness scores reasonable? Are there any outliers?
6. What is the mean happiness score?

It also does a regression analysis on the data to predict the happiness score given the other features in the dataset. The model is tested to see it performance. Some visualizations were also created in Tableau to draw insights.
