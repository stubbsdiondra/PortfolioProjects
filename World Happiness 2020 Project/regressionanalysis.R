# reading in the training set (75% of the data)

WHR = read.csv('WHR Training Set.csv', header = TRUE)

names(WHR)

SLR=lm(Happiness.Score~Logged.GDP.per.capita, data = WHR)
summary(SLR)

MLR=lm(Happiness.Score~Logged.GDP.per.capita + Social.support + Healthy.life.expectancy + Freedom.to.make.life.choices + Generosity + Perceptions.of.corruption, data = WHR)
summary(MLR)

MLR2=lm(Happiness.Score~Logged.GDP.per.capita + Social.support + Freedom.to.make.life.choices, data = WHR)
summary(MLR2)

summary(lm(Happiness.Score~Logged.GDP.per.capita, data = WHR))
summary(lm(Happiness.Score~Logged.GDP.per.capita + Social.support + Healthy.life.expectancy + Freedom.to.make.life.choices, data = WHR))

plot(x = WHR$Freedom.to.make.life.choices,
     y = WHR$Happiness.Score,
     xlab = "Freedom to make life choices",
     ylab = "Happiness score",
     main = "Happiness score vs. Freedom to make life choices")

abline(lm(WHR$Happiness.Score ~ WHR$Freedom.to.make.life.choices,
          data = WHR), col = "black")

plot(x = WHR$Logged.GDP.per.capita,
     y = WHR$Happiness.Score,
     xlab = "GDP",
     ylab = "Happiness score",
     main = "Happiness score vs. GDP")

abline(lm(WHR$Happiness.Score ~ WHR$Logged.GDP.per.capita,
          data = WHR), col = "black")

plot(x = WHR$Social.support,
     y = WHR$Happiness.Score,
     xlab = "SS",
     ylab = "Happiness score",
     main = "Happiness score vs. SS")

abline(lm(WHR$Happiness.Score ~ WHR$Social.support,
          data = WHR), col = "black")

poly_2 <- WHR$Logged.GDP.per.capita^2
poly_3 <- WHR$Logged.GDP.per.capita^3
poly_4 <- WHR$Logged.GDP.per.capita^4

WHR_new <- cbind(WHR,poly_2,poly_3,poly_4)
poly_reg=lm(Happiness.Score~Logged.GDP.per.capita+poly_2+poly_3+poly_4,data=WHR_new)
summary(poly_reg)


poly_reg2=lm(Happiness.Score~Logged.GDP.per.capita+poly_2,data=WHR_new)
summary(poly_reg2)
plot(poly_reg2)


poly_reg3=lm(Happiness.Score~Logged.GDP.per.capita+poly_2+poly_3,data=WHR_new)
summary(poly_reg3)
plot(poly_reg3)

WHR2=read.csv('WHR Test Set.csv', header=TRUE)
poly_2_test <- WHR2$Logged.GDP.per.capita^2
poly_3_test <- WHR2$Logged.GDP.per.capita^3
poly_4_test <- WHR2$Logged.GDP.per.capita^4

WHR2_new <- cbind(WHR2,poly_2_test,poly_3_test,poly_4_test)

poly_reg_test=lm(Happiness.Score~Logged.GDP.per.capita+poly_2_test+poly_3_test+poly_4_test,data=WHR2_new)
WHR2_new$prediction <- predict(poly_reg_test, WHR2_new, type = "Happiness.Score")
predict(poly_reg_test,newdata = WHR2_new)

predict(MLR,newdata = WHR2_new)

predict(MLR, newdata = WHR2_new, interval = "confidence")
predict(MLR, newdata = WHR_new, interval = "confidence")

VIF = 1/(1-0.7143)
VIF

hats <-as.data.frame(hatvalues(MLR))
hats[order(-hats['hatvalues(MLR)']),]
hats
