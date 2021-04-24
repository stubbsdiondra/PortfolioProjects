# THIS DATA and REGRESSION ANALYSIS IS ONLY DONE FOR COUNTRIES IN AFRICA
# Data is drawn from the 2020 World Happiness Report 
# https://www.kaggle.com/nicolevwoude/world-happiness-linear-regression-project

library(readxl)
data <- read_excel("africa_happinessreport.xlsx")
View(data)

# output the names of the columns
names(data)

# to determine which factors predict or best explain the Happiness Scores
## Happiness Scores will be the outcome variable and Social Support, Healthy Life Expectancy,
## Perceptions of Corruption, Generosity and Freedom to Make Life Choices as x or explanatory variables

# after creating and running a summary on this model, adjusted R-squared is 0.1512
## This tells us that approximately 15% of variation in Happiness Scores can be explained by 
## the model created 
## we can also see that the p-value is 0.04499. Since the p-value is less than 0.05 the data is not normally distributed
model <- lm(data$`Happiness Scores` ~ data$`Social support` + data$`Healthy life expectancy` + data$`Freedom to make life choices` + data$Generosity + data$`Perceptions of corruption`) 
summary(model)

# plot the model
plot(model)
## by plotting this model, we can see the relationship between happiness scores and the explanatory variables in the model is not linear


# Testing which variables are a better fit or which variables explain happiness scores

## Testing Social Support
model2 <- lm(data$`Happiness Scores` ~ data$`Social support`)
summary(model2)

# Testing Healthy Life Expectancy
model3 <- lm(data$`Happiness Scores` ~ data$`Healthy life expectancy`)
summary(model3)

# Testiing Freedom to make Life choices
model4 <- lm(data$`Happiness Scores` ~ data$`Freedom to make life choices`)
summary(model4)

# Testing Generosity
model5 <- lm(data$`Happiness Scores` ~ data$Generosity)
summary(model5)

# Testing Perceptions of Corruption
model6 <- lm(data$`Happiness Scores` ~ data$`Perceptions of corruption`)
summary(model6)

# By outputting all of the models above, we can conclude that Generosity is not significant since it explains -1.8% of
# variability in happiness scores. We can also say that Freedom to make life choices and perceptions of corruption are not significant
# because they only explain 1% and 3% of variability in happiness scores. By observing all of the models, we see that healthy life 
# expectancy and social support have the highest adjusted R-squared values. About 12% of variation in Happiness scores is explained by 
# social support and 6% by healthy life expectancy

# let's go one step further to test a model with just happiness scores and healthy life expectancy
mod <- lm(data$`Happiness Scores` ~ data$`Social support` + data$`Healthy life expectancy`)
summary(mod)
## from this model we can see that social support is the only significant explanatory variable. Together, healthly life expectancy and
## social support explain 13% of variation in happiness scores. Since social support is more significant, there is enough evidence to 
## assume that social support is a better fit. Therefore, it predicts happiness scores in Africa. 