# IBM Employee Churn Case Study

As a Senior Business Analyst as IBM, I was informed that the latest company report was released and the employee retention rate has dropped to 84%.

My job is to discover what the key drivers are for employees churning and predict IBM employees at risk of churning. My team has already suggested that a Decision Tree or Gaussian NB machine model is best for prediction, but my job is to fit another classifier and compare it to the ones my team drafted and use exploratory data analysis, visualizations and accuracy scores to make recommendations for IBM to increase employee retention and choose the best performing model.

Tools Used: SQL, Python and Power BI

Skills Used: JOINS, AGGREGATE FUNCTIONS, CREATING VIEWS, Machine Learning, Data Visualizations, Data Analysis

[Article Explaining this Project](https://medium.com/@stubbsdiondra/ibm-employee-churn-prediction-a116ff4e8274)

[Power BI Dashboard](https://drive.google.com/file/d/1aRn_qDrDLEyD2z_LO5tH-Aa83O8GZY3Z/view?usp=sharing)

![slide 1](https://github.com/stubbsdiondra/PortfolioProjects/blob/main/IBM%20Employee%20Churn%20Analysis/ibm_dashboard.png)

## Findings

### KPIs and Metrics

There are 1470 employees at IBM. 1233 of those employees have stayed with the company while 237 have churned. Of the 1470, 31% of employees are very satisfied with their jobs.

The attrition rate is 16.12%. Males are churning the most at IBM. Employees between the ages of 30 to 39 are churning the most. The second group is aged between 20 and 29. 

By department, the Research & Development department has the most churners. The Sales department is close behind it. Lab Technicians, Sales Executives and Research Scientists are roles experiencing the most churning. These roles are in the Research & Development and Sales departments. 

### Satisfaction on the Job

Each satisfaction rating is on a scale with 1 being low and 4 very high (1: Low, 2 :Medium, 3 :High, 4 :Very High). Employees are between Medium and High for satisfaction with environment, relationships, work life balance and their overall job. Job satisfaction is the highest among employees in the sales department and in the age group of <20. This shows that job satisfaction isn’t indicative of employee churn.

### Correlations & Other Relationships

There is a strong correlation between years at company and years with current manager and years at company and years in current role. The scatter plots show that the longer an employee stays at IBM, the longer they stay with the same manager in the same position. This is indicative that lack of promotion may be causing attrition. When we click on the group that has the most churning (30-39), the correlation is even stronger (~80%).

There isn’t much opportunity for growth or promotion, especially for those between the ages of 30 and 39. This same age group received the least training time. Males also received the least training time and these two groups experience the most attrition. This is indicative that lack of professional training may be a key driver of employee churn.

## Model Selection
I found that the Logistic Regression classifier is the best predicting the risk of employees churning when compared the the Decision Tree and Gaussian NB models that my team suggested. To improve accuracy I could try different models or use more training data.

## Recommendations

To increase satisfaction on the job, the company can begin with improving work to life balance. They can implement changes such as offering flexibility in work schedules, location or by allowing remote work. They can encourage work break and consider opportunities where employees can receive time off. Support for parents such as accommodating child care needs or parental leave benefits, may also improve work to life balance.

IBM can host events or create more team work opportunities to foster good relationships between employees. Smarts hires, best practices for conflict resolution and diversity training may improve environment satisfaction.

Our key drivers for churn seem to be lack of promotion and opportunities for training and growth. By implementing opportunities for professional training, growth, promotion or recognition, we may see improvement in employee retention. These efforts should be focused on groups such as males and those between ages 30 to 39. It may also be a smart move to develop great managers for the Research & Development and Sale departments since they are the ones experiencing the most attrition.

Overall, IBM should ensure that their employees are heard. Moving forward they should consider  an employee survey to gauge satisfaction with their jobs and the company, and to learn their thoughts, needs, and suggestions. They should conduct annual reports on attrition after implementing changes and continually monitor satisfaction among employees.
