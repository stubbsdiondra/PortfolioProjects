/*
Diondra Stubbs 
IBM EMPLOYEE DATA EXPLORATION

SKILLS USED: JOINS, AGGREGATE FUNCTIONS, CREATING VIEWS

DATA
I worked with a fictional data set created by IBM data scientists. It contains data about employees and various factors influencing attrition from the company.
There are four tables containing information about the departments at IBM, what department each employee works, what their job role is and other information such as age, gender, etc.

OBJECTIVE 
Imagine you are a Senior Data Analyst for IBM. The latest company performance report has been realeased and it looks like the employee retention rate has reduced to 84%.
Your assignment is to discover what the key drivers are for employees at IBM. You are expected to perform SQL queries to explore the data and make a suggestion as to what may 
be causing employees to leave the company.

*/

USE portfolioproject;

/* 									                     	DATA PREP

First I want to look at all the tables and correct and column names that aren't being read in correctly. 
There should be 1470 rows in the employees, dept_emp and titles tables since there are 147 employees 
*/
SELECT 
    *
FROM
    employees;

ALTER TABLE employees RENAME COLUMN ï»¿EmployeeNumber TO EmployeeNumber;

SELECT 
    *
FROM
    dept_emp;
    
ALTER TABLE dept_emp RENAME COLUMN ï»¿emp_no TO emp_no;

SELECT 
    *
FROM
    titles;
    
ALTER TABLE titles RENAME COLUMN ï»¿emp_no TO emp_no;



/* 
								                       DATA EXPLORATION  
*/


/* How many employees have left? How many stayed?*/

SELECT 
    *
FROM
    employees;

SELECT 
    Attrition, COUNT(Attrition)
FROM
    employees
GROUP BY Attrition; # 237 employees have left or churned while 1233 have stayed


/* What is the attrition rate? */
SELECT
(SELECT 
    COUNT(Attrition)
FROM
    employees
WHERE
    Attrition = 'Yes') /
(SELECT 
    COUNT(EmployeeNumber)
FROM
    employees)*100 AS attrition_rate; # the attrition rate is 16.12%


/* What is the employee profile for a employee that churned and stayed? */

CREATE OR REPLACE VIEW employee_profile AS
	SELECT 
		Age,
		Gender,
		Attrition,
		DistanceFromHome,
		JobRole,
		MaritalStatus
	FROM
		employees;
        
SELECT 
    (SELECT 
            COUNT(Gender)
        FROM
            employee_profile
        WHERE
            Attrition = 'Yes' AND Gender = 'Female') / (SELECT 
            COUNT(Attrition)
        FROM
            employee_profile
        WHERE
            Attrition = 'Yes') * 100 AS females_attrition; # 36.7% of employees who churned are women
            
SELECT 
    (SELECT 
            COUNT(Gender)
        FROM
            employee_profile
        WHERE
            Attrition = 'No' AND Gender = 'Female') / (SELECT 
            COUNT(Attrition)
        FROM
            employee_profile
        WHERE
            Attrition = 'No') * 100 AS females_stayed; # 40.6% of employees who stayed are women
            
SELECT 
    (SELECT 
            COUNT(Gender)
        FROM
            employee_profile
        WHERE
            Attrition = 'Yes' AND Gender = 'Male') / (SELECT 
            COUNT(Attrition)
        FROM
            employee_profile
        WHERE
            Attrition = 'Yes') * 100 AS males_attrition;  #63.3% of employees who churned are men
            
SELECT 
    (SELECT 
            COUNT(Gender)
        FROM
            employee_profile
        WHERE
            Attrition = 'No' AND Gender = 'Male') / (SELECT 
            COUNT(Attrition)
        FROM
            employee_profile
        WHERE
            Attrition = 'No') * 100 AS males_stayed; # 59.4% of employees who stayed are men
            
SELECT 
    AVG(Age)
FROM
    employee_profile
WHERE
    Attrition = 'Yes'; # The average age is 33 for those who have churned

SELECT 
    MAX(Age)
FROM
    employee_profile
WHERE
    Attrition = 'Yes'; #58
    
SELECT 
    MIN(Age)
FROM
    employee_profile
WHERE
    Attrition = 'Yes'; #18

SELECT 
    AVG(Age)
FROM
    employee_profile
WHERE
    Attrition = 'No';
    
SELECT 
    MAX(Age)
FROM
    employee_profile
WHERE
    Attrition = 'No'; # 60

SELECT 
    MIN(Age)
FROM
    employee_profile
WHERE
    Attrition = 'No'; # 18


SELECT 
    JobRole, COUNT(JobRole) AS count
FROM
    employee_profile
WHERE
    Attrition = 'yes'
GROUP BY JobRole
ORDER BY count DESC; # Lab Technician role has the most churning employees. 'Sales Executive', Research Scientist, 'Sales Representative' have the most churning. see what's happening in the departments of these roles


/* What departments do employees work in? */

SELECT 
    de.dept_no, de.emp_no, d.dept_name
FROM
    dept_emp de
        INNER JOIN
    departments d ON de.dept_no = d.dept_no
ORDER BY de.emp_no;

/* Now we can see each department name and number assigned to the IBM employees.
How many distinct departments are there in the company? */

CREATE OR REPLACE VIEW depts AS
SELECT 
    de.dept_no, de.emp_no, d.dept_name
FROM
    dept_emp de
        INNER JOIN
    departments d ON de.dept_no = d.dept_no
ORDER BY de.emp_no;

select * from depts;

SELECT DISTINCT
    dept_name
FROM
    depts; # there are 3 unique departments at IBM among these 1470 employees.

/* How many distinct job roles are there? */

SELECT 
    *
FROM
    titles;
    
SELECT DISTINCT
    titles
FROM
    titles; # there are 9 unique job roles

/* 
								                      PREDICTING WHY EMPLOYEES ARE CHURNING
*/


/* 
When thinking of reason why employes may leave their job, satisfaction comes into mind. I want to see if there is any
correlation between Job Satisfaction ratings and employee leaving their jobs. 

Employee satisfaction is a range variable (1-4) while Attrition is a nominal variable("Yes" or "No"). 
The Point-Biserial Correlation is useful for finding the relationship between numerical/range data and a 
dichotomous variable. The numerical variable is Job Satisfaction and the dichotomous variable is Attrition. 
I'm going to use Point-Biserial Correlation to find correlation between Attritiona and Job Satisfaction
*/

SELECT 
    Attrition, AVG(JobSatisfaction)
FROM
    employees
GROUP BY Attrition; # M1 = Yes, Mo=No

SELECT 
    STD(JobSatisfaction) AS std_jobsatisfaction
FROM
    employees;
    
SELECT 
    COUNT(*), Attrition
FROM
    employees
GROUP BY Attrition;

# While the satisfaction score is similar for both groups, we get a correlation of -0.10 between Job Satisfaction and Attrition. 
# There is virtually not correlation between employee retention and job satisfaction meaning that being satisified on the job or not
# is not a major factor towards employees churning


    
/* Next I would think to look at the correlation between employees years at the company and if they've been promoted.
The Pearson correlation coefficient  is a measure of linear correlation between two sets of data. It is the ratio between 
the covariance of two variables and the product of their standard deviations; thus, it is essentially a normalized measurement 
of the covariance, such that the result always has a value between −1 and 1. I will use Pearson's correlation to 
find the correlation between employee years in current position and years at the company?
*/
SELECT 
    @firstValue:=AVG(YearsAtCompany) as avg_years_at_company,
    @secondValue:=AVG(YearsInCurrentRole) as avg_years_on_job,
    @division:=(STDDEV_SAMP(YearsAtCompany) * STDDEV(YearsInCurrentRole)) as std
FROM
    employees;
    
SELECT 
    SUM((YearsAtCompany - @firstValue) * (YearsInCurrentRole - @secondValue)) / ((COUNT(YearsAtCompany) - 1) * @division) as Correlation
FROM
    employees;

# YearsInCurrentRole is highly correlated with YearsAtCompany and YearsWithCurrManager and moderatly correlated with YearsSinceLastPromotion. 
# This insinuates that many employees remain in their current role overtime and there isn't much opportunity for promotion.
# Can deduct and report to IBM stakeholders that lack of promotions may be a crucial factor to attritions.