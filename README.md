# Telco-Customer-Churn

## Motivation:

Customer retention is important to any growing company because it measures how successful they are at satisfying existing customers.

Moreover, it is also well known that:
*  Retain customers is more cost-effective than acquiring new ones,
* Retained customers tend to spend more and buy more often,
* Retained customers are more willing to refer your products to friends and family.

The aim of this study is to analyze relevant customer data in order to develop focused customer retention programs.

Concretely, we'd like to answer the following questions:

Is the percentage of churn the same across all services?
Is there a way to improve the retention ratio within a particular service?
Is there some kind of client more likely to churn?

## Installation

We have used python 3.8 for this project, and a detailed list of packages and their version is available within conda_environment.txt file.

## Project Structure

* **Telco Customer Churn.ipynb:** Jupyter Notebook containing a well-documented version of the analysis. We strongly suggest going through it in order to have a better understanding of all conclusions.

* **./utilities/functions.py:** Python script containing all the necessary helper functions used during the analysis

* **./data/telcocustomerchurn.csv:** The data used for the analysis, we provide a deeper explanation about the data down below.
* **conda_environment.txt:** txt file containing all the necessary packages and versions to run the project.

## Data:

For this analysis, we'll be exploring the Telco Customer Churn DataSet, where each row represents a customer, each column contains customer’s attributes, such as:


* Customer account information, e.g. how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.

* Demographic info about customers, e.g. gender, age range, and if they have partners and dependents

* Services that each customer has signed up for e.g. phone, multiple lines, etc.

## Results

In this section, we will show some of the key findings:

1. Customer who has recently signup for the Fiber Optics service have the highest churn probability

![image](https://user-images.githubusercontent.com/28582065/93122124-403e3e80-f6c6-11ea-9f6e-447f8f11ddb2.png)

2. Service add-ons such as Streaming Entertainment or Online Security are helpful resources to retain unhappy Fiber Optic customers.

![image](https://user-images.githubusercontent.com/28582065/93122372-a4610280-f6c6-11ea-9d91-a53f8262fc33.png)

3. There are some socio-demographic characteristics that customers with the lowest churn probability share in common.

![target_pop](https://user-images.githubusercontent.com/28582065/93122710-4b459e80-f6c7-11ea-8cbf-6373490d478f.png)
