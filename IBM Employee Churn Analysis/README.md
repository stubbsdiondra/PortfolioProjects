# IBM Employee Churn Case Study

As a Senior Business Analyst as IBM, I was informed that the latest company report was released and the employee retention rate has dropped to 84%.

My job is to discover what the key drivers are for employees churning and predict IBM employees at risk of churning. My team has already suggested that a Decision Tree or Gaussian NB machine model is best for prediction, but my job is to fit another classifier and compare it to the ones my team drafted and use exploratory data analysis, visualizations and accuracy scores to make recommendations for IBM to increase employee retention and choose the best performing model.

Tools Used: SQL, Python and Power BI

Skills Used: JOINS, AGGREGATE FUNCTIONS, CREATING VIEWS, Machine Learning, Data Visualizations, Data Analysis

[Article Explaining this Project](https://medium.com/@stubbsdiondra/ibm-employee-churn-prediction-a116ff4e8274)

[Power BI Dashboard](https://drive.google.com/file/d/1aRn_qDrDLEyD2z_LO5tH-Aa83O8GZY3Z/view?usp=sharing)

![slide 1](https://github.com/stubbsdiondra/PortfolioProjects/blob/main/IBM%20Employee%20Churn%20Analysis/photos/1.png)

## Findings
- Employees between the ages of 18-23 and 48+ are the least satisfied on the job.
- The most attritions are taking place among middle aged employees (26-35). This group also experiences some of the highest amount of years since last promotion
- 83.9% (1233) of IBM's employees have stayed, while 16.1% (237) have left.
- The Research & Development and Sales departments experience the most churning
- YearsInCurrentRole is highly correlated with YearsAtCompany and YearsWithCurrManager and moderatly correlated with YearsSinceLastPromotion. This insinuates that many employees remain in their current role under the same manager overtime and there isn't much opportunity for promotion.  Lack of promotions may be a crucial factor to attritions.

## Recommendations
- implement professional-development opportunities, inclusion and diversity and access to key benefits to increase young employee job satisfaction.
- implement things like lighter workload, additional leave, and semi-retirement for to increase older employee job satisfaction.
- Implement more opportunities for promotion.

## Model Selection
I found that the Logistic Regression classifier is the best predicting the risk of employees churning when compared the the Decision Tree and Gaussian NB models that my team suggested. To improve accuracy I could try different models or use more training data.

[View Slideshow](https://www.canva.com/design/DAFT9KPwKI0/a-CALd4j7ZY3-ATtlsWWTA/view?utm_content=DAFT9KPwKI0&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
