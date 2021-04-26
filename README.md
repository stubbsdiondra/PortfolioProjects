# THE HAPPINESS OF AFRICA
## What is the general state of happiness in Africa? 

This project analyzes the 2020 World Happiness Report to draw conclusions about the general well being of Africa. It uses several CSV files consisting of survey responses formed from a Google Form survey, data from the 2020 World Happiness Report and data on countries only in Africa from the 2020 World Happiness Report. The main data set used includes over 150 countries and their happiness scores, freedom to make life choices, social support, healthy life expectancy, regional indicator, perceptions of corruption and generosity. This analysis was done to answer the following data-driven questions: 'Which African country ranked the happiest in 2020?' and 'Which variable predicts or explains Africa's happiness score?'

This project includes several programs created in R and Python. (all created by Diondra Stubbs)

![431280](https://user-images.githubusercontent.com/83089796/116160255-b45ead00-a6bf-11eb-997b-6b3f2b5cb716.jpg)


## Background

The Gallup World Poll (GWP) is conducted annually to measure and track public attitudes concerning political, social and economic issues, including controversial and sensitive subjects. Annually, this poll tracks attitudes toward law and order, institutions and infrastructure, jobs, well-being and other topics for approximately 150 countries worldwide. The data gathered from the GWP is used to create an annual World Happiness Report (WHR). The World Happiness Report is conducted to review the science of understanding and measuring the subjective well-being and to use survey measures of life satisfaction to track the quality of lives in over 150 countries.

At first glance, it seems that world happiness isn't important or maybe it's just an emotional thing. However, several governments have started to look at happiness as a metric to measure success. Happiness Scores or  Subjective Well-being (SWB) are national average responses to questions of life evaluation. They are important because they remind policy makers and people in power that happiness is based on social capital, not just financial. Happiness is often considered an essential and useful way to guide public policies and measure their effectiveness. It is also important to note that happiness scores point out the importance of qualitative rather than quantitative. At times, quality is better than quantity. 

Africa is the world's second largest and second most populous continent in the world. It consists of 54 countries meaning that Africa has the most countries. Africa has approximately 30% of the earth's mineral resources and has the largest reserves of precious metals. Africa reserves over 40% of the gold reserves, 60% on cobalt and 90% of platinum. However, Africa unfortunately has the most developmental challenges. It is the world's poorest and most underdeveloped continent. Africa is also almost 100% colonized with the exceptions of Ethiopia and Liberia. Given this information, one can wonder what the SWB or state of happiness is in Africa? 

This site analyzes the 2020 World Happiness Report to draw conclusions to data-drive questions listed later on this page. The focus is specifically on countries in Africa. Even though there are 54 countries in Africa, only 43 participated in the 2020 WHR.

## The Why Behind this Analysis

Over 400 years ago, the tragic and disheartening event of slavery took place. People were kidnapped from the continent of Africa, forced into slavery in the American colonies and exploited to work as indentured servants. Families were ripped apart, history lost, heritages and customs uprooted and destroyed. Africa has a very sad history with the inclusion of slavery and colonialism. Before colonialism ruled, Africa had over 10,000 different states and autonomous groups with distinct languages and customs. After being uprooted from there home, much of that has been lost. This may include the removal of roots, traditions, and even identity. It is also crucial to point out that African's being removed from their home didn't allow them to truly develop and protect their home. 

This is very close to home because unfortunately, this is the reality of my ancestors. My great great grandparents were enslaved and I'm sure many more of my forefathers were. As a result, my family has lost their true history. It is disheartening to know that a part of my identity is lost in not being able to truly know where my ancestors are from and what customs, traditions and cultures we had. What language and practices did my ancestors speak and do? So many questions that I may never know the answer to. Based on the history and current state of Africa: What is the SWB of Africa? Has colonialism affected the happiness of Africa? Does Africa's sad history cause it to rank low in annual happiness reports? Which country in Africa is the happiest? The saddest? What factors or variables explain the happiness of Africa?


## World Happiness Report 2020

The dataset used is generated from the 'World Happiness Report 2020'. This dataset contains the Happiness Score for over 150 countries for the year of 2020. The data gathered from the Gallup World Poll gives a national average of Happiness scores for countries all over the world. It is a annual landmark survey of the state of global happiness.

This dataset is from the data repository "Kaggle". On Kaggle's dataset page, I searched for Africa Happiness after filtering the search to CSV file type. I wasn't able to find any datasets that could answer my questions that didn't include other countries from different continents. I decided to use a Global Happiness Report to answer the questions I have. The dataset I am using was publish by Micheal Londeen and it was created on March 24, 2020. His main source is the World Happiness Report for 2020.


## Defining the variables in the data set
 
Happiness score or subjective well-being (variable name ladder ): The survey measure of SWB is from the Feb 28, 2020 release of the Gallup World Poll
(GWP) covering years from 2005 to 2019. Unless stated otherwise, it is the national average response to the question of life evaluations. The English wording 
of the question is “Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. The top of the ladder represents the best possible life
for you and the bottom of the ladder represents the worst possible life for you. On which step of the ladder would you say you personally feel you stand at this
time?” This measure is also referred to as Cantril life ladder, or just life ladder in our analysis.

Healthy Life Expectancy (HLE). Healthy life expectancies at birth are based on the data extracted from the World Health Organization’s (WHO) Global
Health Observatory data repository. The data at the source are available for the years 2000, 2005, 2010, 2015 and 2016. To match this report’s sample period
(2005-2019), interpolation and extrapolation are used.

Social support (or having someone to count on in times of trouble) is the national average of the binary responses (either 0 or 1) to the GWP question “If you
were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”

Freedom to make life choices is the national average of responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what
you do with your life?”

Generosity is the residual of regressing national average of response to the GWP question “Have you donated money to a charity in the past month?” on GDP
per capita.

Corruption Perception: The measure is the national average of the survey responses to two questions in the GWP: “Is corruption widespread throughout
the government or not” and “Is corruption widespread within businesses or not?” The overall perception is just the average of the two 0-or-1 responses. In
case the perception of government corruption is missing, we use the perception of business corruption as the overall perception. The corruption perception at
the national level is just the average response of the overall perception at the individual level.

Source: https://happiness-report.s3.amazonaws.com/2020/WHR20_Ch2_Statistical_Appendix.pdf


## Description of the files and code

2020.csv --> Original cleaned data set from the 2020 World Happiness Report gathered from https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv

africa_happinessreport.csv --> Filtered set from the 2020.csv containing only countries in Africa

africa_happinessreport.xlsx --> Filtered set from the 2020.csv containing only countries in Africa in the form of an XLSX file

stubbs_africahappiness.csv --> africa_happinessreport.csv with some columns removed

survey.csv --> survey responses from a Google Forms survey I created for this topic https://docs.google.com/forms/d/e/1FAIpQLSdu7pYt7SNpZvzXds1kjhzsSuS-X_FyPvHdx2ViR7LyaTISUQ/viewform?usp=sf_link

africa_further_analysis.py --> reading in a CSV into a DataFrame. This program outputs the columns in the filtered set for countries only in Africa. It also creates a correlation matrix and views the regressions of each variable within the data set

africaahappiness_regressionanalysis.R --> R codes used to perform multiple linear regression

stubbs_africahappiness.csv --> 2020.csv with some columns removed

stubbs_africahappiness2020.py --> A Python program that approximates the average overall happiness scores of the continent Africa from 2015 to 2020 and the average social support factor in Africa between 2015 and 2020. 

stubbs_dataframes.py -->  A modularized Python program that reads the 2020 World Happiness Report data set found online into a Pandas DataFrame. It creates filtered subsets of the Pandas DataFrame containing all records in the original dataset to only focus on particular continents such as Africa, Europe and Asia. This program will output calculations on these continents by performing data statistic calculations such as mean, median, maximum and minimum. This will potentially help answer the question of "Which African country scored the happiest in 2020?"  

stubbs_dataset_analysis.py --> A modularized Python program that reads all the records from the 2020 World Happiness Report data set found online into a Pandas DataFrame, visually inspects and cleans the DataFrame for common data errors, and creates summary tables and visualizations from the cleaned 
DataFrame.

stubbs_functions.py --> A Python program that provides the user with a list of choices pertaining to African happiness data from the World Happiness Report. The list of choices in the program will relate data and simple facts using happiness score data from the World Happiness Report.

stubbs_stats.py -->  A Python program that provides the user with a list of choices pertaining to African happiness data from the World Happiness Report. The list of choices in the program will relate data and simple facts using happiness score data from the World Happiness Report.

stubbs_survey.py --> A Python program that queries the user to input responses to the survey questions from my Google Form survey. The program records the users responses and uses conditional statements to check and clean their inputs. After cleaning the user input, the program then outputs clean data in a CSV format. 

stubbs_survey_analysis.py --> A Python program that reads and cleans the Happiness in Africa Google Forms Survey responses to output data visualizations and statistics with this cleaned data. This modularized program breaks all tasks required for this program into 8 functions to avoid code duplication and to easily reuse code when checking values in the CSV file and computing data statistics (i.e, mean, median andstandard deviation)

stubbs_visuals.py --> A Python program that creates four different types of visualizations based on the data from the 2015, 2016, 2017, 2018, 2019 and 2020 World Happiness Report. Additionally, this program also computes basic calculations such as minimum, maximum and average on this same data.

stubbs_final.py --> A modularized Python program that provides the user with several options to choose from to showcase all of the data performed on the Google Forms survey and 2020 World Happiness Report data set. This program produces relevant data computations, pivot tables and visualizations that are relevant to the 2020 Africa Happiness topic and the posed data-driven questions on this topic. The user is able to choose between EIGHT options viewing the following: an overview of the topic and data set, data-driven questions and predictions, basic data statistics, simple data visualizations, survey analysis, data set analysis and findings and observations to the data-driven questions. The EIGHTH option allows the user to quit the program. 

## Findings & Observations

Question 1: Which country in Africa ranked the happiest in 2020?

Prediction: Happiness Scores are national average responses to questions of life evaluation. Getting this data is important because it helps remind policymakers and people in power that happiness is based on social capital, not just financial. These data results are an essential and useful way to guide public policies and measure their effectiveness. From the initial interaction with the original data set, Israel was named as a country that is in Africa. After deeper research, it was found that Israel is actually a part of Asia. The initial prediction was that Israel ranked the happiest in 2020 but the country in Africa that actually ranked the happiest in 2020 in Mauritius.

Observation(s): Mauritius scored as the happiest country in Africa for 2020. 'According to the 2020 World Happiness Report, Mauritius is listed as the happiest country in Africa with a happiness score of 6.1. A survey was created on this topic to determine which Africa country was the happiest based on respondent’s observations or opinions. The survey asked: Which African country do you think had the highest happiness rank in 2020?. The four options given were Israel, Mauritius, South Sudan, and Ethiopia. The option of Israel was a mistake on my part since I did not realize that Israel is actually in Asia. Taking this into count, I visually inspected and cleaned the data set in excel by researching where each country is located by continent. Based on these findings, I cleaned the data set in excel by properly stating the Continent of each country in the data set. 

Based on the survey responses, respondents believed that Israel was the happiest country but since it is not in Africa, most respondents believed that Ethiopia was the happiest African country in 2020.

                Country Name  Happiness Scores

                    Algeria              5.01

                      Benin              5.22

                   Botswana              3.48

               Burkina Faso              4.77

                   Burundi              3.78

                   Cameroon              5.08

    Central African Republic              3.48

                       Chad              4.42

                    Comoros              4.29

        Congo (Brazzaville)              5.19

          Congo (Kinshasa)              4.31

                     Egypt              4.15

                  Ethiopia              4.19

                     Gabon              4.83

                    Gambia              4.75

                     Ghana              5.15

                    Guinea              4.95

               Ivory Coast              5.23

                     Kenya              4.58

                   Lesotho              3.65

                   Liberia              4.56

                     Libya              5.49

                Madagascar              4.17

                    Malawi              3.54

                      Mali              4.73

                Mauritania              4.37

                 Mauritius              6.10

                   Morocco              5.09

                Mozambique              4.62

                   Namibia              4.57

                     Niger              4.91

                   Nigeria              4.72

                    Rwanda              3.31

                   Senegal              4.98

              Sierra Leone              3.93

              South Africa              4.81

               South Sudan              2.82

                 Swaziland              4.31

                  Tanzania              3.48

                      Togo              4.19

                   Tunisia              4.39

                    Uganda              4.43

                    Zambia              3.76

                  Zimbabwe              3.30

Above is outputted the summary table of African countries and their happiness score. The summary table was used to create a bar visual of each African country and their happiness score.

![Screenshot_1](https://user-images.githubusercontent.com/83089796/116130163-e6a8e400-a698-11eb-9549-be30651c42ca.png)

From the visualization above and the summary table, it is shown that Mauritius has the highest happiness score for 2020. In response to this first data-driven question, the observations above show that Mauritius ranked the happiest in 2020.


Question 2: Does a lower or higher social support score affect the overall happiness of a country? 

Prediction: By visually inspecting the original data set, the conclusion made was that higher-scoring countries (in happiness) had higher social support scores. This question was formed based on that observation. The prediction made was that higher social support scores result in higher happiness scores.

Observations: Observing the original CSV data set, it was concluded that Mauritius has the highest social support score. This led to the second data-driven question. Simply viewing the data in excel was not enough to draw a conclusion or response to this question, so a scatter chart was made to observe the relationship between social support and happiness scores. 

The chart made in Excel sheets created a scatter graphic and returned an R-squared value of 0.143. R-squared is a goodness-of-fit measure for linear regression models. I decided to use some of my skills from statistics and perform a bit of correlation analysis. Since R-squared is 0.143, approximately 14% of the variability in happiness scores is being explained by social support scores. From this, we can draw that the model doesn’t do a good job of explaining the variation of happiness scores in social support scores. 

![Screenshot_2](https://user-images.githubusercontent.com/83089796/116130247-017b5880-a699-11eb-8b45-96dc369a4aa5.png)

The scatter visual showing the relationship between social support and happiness scores is outputted above. We can’t be sure if social support scores give a country a higher or lower happiness score but together, all of the variables contribute to the happiness score.


Question 3: Does freedom to make life choices lower or raise the happiness score of a country?

Prediction: A comparison was made between the highest-ranking and lowest-ranking countries in Africa to make a prediction for this question. It was observed that South Sudan ranked the lowest and Mauritius ranked the highest in happiness. It was drawn that South Sudan had a lower score in freedom to make life choices while Mauritius scored higher. From this, the prediction that was made is that high happiness scores are a result of higher freedom to make life choices scores. The prediction is that more freedom to make life choices makes a country happy.

Observations: While it is easy to draw that Mauritius has a high value for freedom to make life choices and South Sudan has the lowest, it does not confirm whether this variable raises or lowers happiness. Another scatter visual was created in Excel sheets and it returns an R-squared value of 0.033. This implies that approximately 3% of the variability in happiness scores is being explained by the freedom to make life choices. This is very close to 0%, which represents a model that does not explain any of the variations in the response variable around its mean. From this, we can conclude that freedom to make life choices is not a good variable to explain happiness scores. However, it is possible that social support may be a better predictor of happiness scores.

![Screenshot_3](https://user-images.githubusercontent.com/83089796/116130343-1a840980-a699-11eb-9360-67debd4eabde.png)

The scatter visual showing the relationship between freedom to make life choices and happiness scores is outputted above.


Question 4: What is the relationship between happiness scores and healthy life expectancy?

Prediction: This question was formed based on the curiosity of if healthy life expectancy results from a country's happiness or if a country's happiness is evaluated in the fact that there is a healthy life expectancy. The healthy life expectancy column is based on Healthy life expectancies at birth, based on the data extracted from the World Health Organization’s (WHO) Global Health Observatory data repository. By comparing the healthy life expectancy scores between Mauritius and South Sudan, it was predicted that there is a positive relationship between happiness scores and healthy life expectancies. Higher happiness scores appear where there is a higher healthy life expectancy.

Observations: This data-driven question was asked to determine whether happiness causes healthy life expectancy or vice versa. To respond to this question, a line visual was made to observe the relationship between happiness scores and healthy life expectancy.

![Screenshot_4](https://user-images.githubusercontent.com/83089796/116130406-312a6080-a699-11eb-9813-0d676b6d3ba2.png)

The line chart showing the relationship between happiness scores and healthy life expectancy is outputted above. From this, we can conclude that the visual is very confusing. I would consider this to be an ineffective data visualization. This outputted line visual is not able to provide us with an answer to this data-driven question.

I took extra time to create a scatter visualization in excel to observe this relationship deeper. The returned R-squared value was 0.091. This means that only 9% of the variability in happiness scores is explained by healthy life expectancy. This leads me to conclude that it is better to consider all of the variables (columns) instead of drawing, which best predicts a country’s happiness score.

# Further Findings & Observations

To further the data analysis on this topic, some extra steps were taken to perform statistical analysis. Both Python and R were used to draw final conclusions. First, the original uncleaned data set was used in R programming language to run a multiple linear regression analysis. The results are as follows:

Together, social support, healthy life expectancy, perceptions of corruption, freedom to make life choices, and generosity explain 15% of the variability in happiness scores for African countries. These results are drawn from running a multiple linear regression on a model that only includes happiness scores, social support, healthy life expectancy, perceptions of corruption, freedom to make life choices, and generosity. The outputted adjusted R-squared value was 0.1512, therefore, giving us a 15% variability.

I decided to take it a step further and create more models between happiness scores and just one explanatory variable (social support, healthy life expectancy, perceptions of corruption, freedom to make life choices, or generosity). From this, it was found that social support has the highest adjusted R-squared value of 0.1223. This means that 12% of the variation in Happiness scores is being explained by social support. We can assume that social support is the best predictor of the results for Africa’s happiness scores.


To analyze further, a correlation matrix was created in Python between happiness scores, social support, healthy life expectancy, perceptions of corruption, freedom to make life choices, and generosity. Even though there weren’t any high correlations, the strongest correlation was between social support and happiness scores with a value of 0.38. This means that social support is more conditioning to the happiness score more than any other variable in the data set. Furthermore, happiness in Africa is related to people having relatives and/or friends that they can count on when they need help.


You can see the additional output from R and Python described in 'Furthering Observations and Findings' analysis in the codes above.

More information can be found here: https://sites.google.com/uri.edu/stubbs-africa-happiness-2020/home?authuser=0e

- Diondra Stubbs
