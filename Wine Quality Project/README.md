# Wine Quality Machine Learning Project

This is a machine learning project using supervised and unsupervised learning. Clustering is unsupervised learning for a categorical target.. That means we do not have the labels to learn from. We aim to learn both the labels for each point and some way of characterizing the classes at the same time. Classification is supervised learning for a categorical target. Each python notebook has markdown explain the machine learning processes.

![alt text](https://github.com/stubbsdiondra/PortfolioProjects/blob/main/Wine%20Quality%20Project/Untitled%20design.png)

## About the Dataset

This dataset is the result of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines. More about this [dataset](https://archive.ics.uci.edu/ml/datasets/wine).

#### Dataset Features
1. Alcohol
2. Malic acid
3. Ash
4. Alcalinity of ash  
5. Magnesium
6. Total phenols
7. Flavanoids
8. Nonflavanoid phenols
9. Proanthocyanins
10. Color intensity
11. Hue
12. OD280/OD315 of diluted wines
13. Proline

## Classification Task
The task is to predict the quality of the wine from the measurements. I am going to attempt building an automatic wine classifier that, for measurements of a new wine returns the predicted quality. 

The dataset has columns for quality, alcohol,	malic acid, ash, alcalinity, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color intensity, hue, OD280_OD315, and proline. The target variable (chosen classifier) will be the quality of the wine.

## Clustering 

Clustering is a random algorithm where we aim to learn the labels for each point while characterizing the classes at the same time. It is different from regression and classification in that it is unsupervised learning and there isn't a target variable.  As opposed to regression and classification, we can do clustering on data without splitting the data in test or train splits. Because of this, we can evaluate how good clusters are based on the actual data it learn from rather than test or train data.

### Objective

What is the quality of each wine sample? The task is to predict the quality of the wine in this dataset without having to split the data in test/train models. I want to be able to do this by using the data I already have.
