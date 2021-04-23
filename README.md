# The Happiness of Africa
## What is the general state of happiness in Africa? 

This project analyzes the 2020 World Happiness Report to draw conclusions about the general well being of Africa. It uses a data set consisting of over 150 countries and their happiness scores, freedom to make life choices, social support, healthy life expectancy, regional indicator, perceptions of corruption and generosity. This analysis was done to answer the following data-driven questions: 'Which African country ranked the happiest in 2020?' and 'Which variable predicts or explains a country's happiness score?'


# Background

Every year, a World Happiness Report is published to state the subjective well-being (SWB) in each country across the globe. The World Happiness Report is a publication of the United Nations Sustainable Development Solutions Network and it is a result of data from the Gallup World Poll. Over 150 countries participate in the study, annually. The World Happiness Report for 2020 ranks cities around the world by their SWB and digs even deeper into how social, urban and natural environments affect our happiness. 

Happiness Scores or SWB are national average responses to questions of life evaluation. They are important because they remind policy makers and people in power that happiness is based on social capital, not just financial. Happiness is often considered an essential and useful way to guide public policies and measure their effectiveness.

Africa is the world’s second largest and second most populous continent on the globe. It has 54 countries making it the continent with the most countries. Africa has approximately 30% of the earth’s mineral resources. It also has the largest reserves of precious metals with over 40% of the gold reserves, 60% on cobalt and 90% of platinum. However, Africa is the world’s poorest and most underdeveloped continent. One begins to wonder, if the fact that Africa is almost 100% colonized, factors into that. Given that Africa is the poorest and most underdeveloped country, what is the SWB of Africa? Which country in Africa is the happiest? The saddest? Will the continent's state of colonization and development affect their overall happiness?


# World Happiness Report 2020

The dataset used is generated from the 'World Happiness Report 2020'. This dataset contains the Happiness Score for over 150 countries for the year of 2020. The data gathered from the Gallup World Poll gives a national average of Happiness scores for countries all over the world. It is a annual landmark survey of the state of global happiness.

This dataset is from the data repository "Kaggle". On Kaggle's dataset page, I searched for Africa Happiness after filtering the search to CSV file type. I wasn't able to find any datasets that could answer my questions that didn't include other countries from different continents. I decided to use a Global Happiness Report to answer the questions I have. The dataset I am using was publish by Micheal Londeen and it was created on March 24, 2020. His main source is the World Happiness Report for 2020.


# Defining the variables in the data set
 
Country Name: The name of the country
 
Regional Indicator: The location of the country (continent or region)
 
Happiness Score: The survey measure of SWB is from the Gallup World Poll (GWP) covering years from 2005 to 2019. The national average response to the question of life evaluations. 
 
Healthy Life Expectancy: Healthy life expectancies at birth, based on the data extracted from the World Health Organization’s (WHO) Global Health Observatory data repository.

Social Support: The national average of the binary responses (either 0 or 1) to the GWP question “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”

Freedom to Make Life Choices:  The national average of responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”

Perception of Corruption: The national average of the survey responses to two questions in the GWP: “Is corruption widespread throughout the government or not” and “Is corruption widespread within businesses or not?”

Generosity: The residual of regressing national average of response to the GWP question “Have you donated money to a charity in the past month?” on GDP per capita. 

More information can be found @ https://sites.google.com/uri.edu/stubbs-africa-happiness-2020/home
