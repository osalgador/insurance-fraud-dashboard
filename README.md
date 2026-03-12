Insurance Fraud Detection Dashboard
Overview

This project analyzes insurance claim data to identify patterns associated with fraudulent claims.
Using Python for data cleaning and exploratory analysis and Power BI for visualization, the dashboard provides insights into claim behavior, fraud rates, and risk indicators.

The goal of this project is to demonstrate data analysis and actuarial insights in the insurance industry.

Objectives

Analyze insurance claims data

Identify patterns related to fraudulent claims

Explore relationships between:

claim severity

incident type

customer age

geographic location

Visualize key metrics using an interactive Power BI dashboard

Project Structure
insurance-fraud-dashboard
│
├── data
│   └── insurance_claims.csv
│
├── scripts
│   └── lifeinsurance.py
│
├── dashboard
│   └── insurance_fraud_dashboard.pbix
│
├── images
│   └── dashboard_preview.png
│
└── README.md

Data Preparation

The dataset was cleaned using Python (Pandas).

Main preprocessing steps:

Handling missing values

Converting categorical variables

Transforming binary variables:

property_damage

police_report_available

fraud_reported

Creating new analytical variables:

Fraud Label

Age Groups

Claim Severity Categories

Exploratory Data Analysis

Several visualizations were generated using Python to understand the data distribution:

Customer age distribution

Fraud cases distribution

Incident severity analysis

Claim amount vs fraud status

Claims by state

Incident type frequency

Dashboard Features

The Power BI dashboard includes:

Key Performance Indicators (KPIs)

Total Claims

Fraud Cases

Fraud Rate

Total Claim Amount

Average Claim Amount

Main Visualizations

Fraud vs Non-Fraud distribution

Claims by Age Group

Fraud by Incident Severity

Claims by Incident Type

Claims by State

Claim Amount by Fraud Status

Interactive Filters

Users can filter the dashboard by:

Incident Type

State

Incident Severity

Key Insights

Approximately 24.7% of claims show fraud indicators

Fraudulent claims tend to have higher average claim amounts

The most common incidents are:

Single vehicle collisions

Multi-vehicle collisions

The majority of claims occur among customers aged 31–50

Tools & Technologies

Python

Pandas

Matplotlib / Seaborn

Power BI

Git

GitHub

Dashboard Preview
<img width="1383" height="777" alt="image" src="https://github.com/user-attachments/assets/9dee0b80-b7d4-4731-a67a-7b4b11a24137" />
Future Improvements

Build a machine learning model to predict fraud probability

Implement feature engineering for risk scoring

Add time-series analysis for claim trends

Author

Oscar Salgado

Data analysis projects focused on insurance risk, fraud detection, and actuarial insights.

GitHub:
https://github.com/osalgador

Project Purpose

This project was developed as part of a data analytics and actuarial portfolio, demonstrating skills in:

Data cleaning

Exploratory data analysis

Data visualization

Risk analysis in insurance datasets

