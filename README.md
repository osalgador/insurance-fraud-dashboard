# Insurance Fraud Detection Dashboard

## Overview
This project analyzes **insurance claim data** to identify patterns associated with **fraudulent claims**. Using **Python for data cleaning and exploratory analysis** and **Power BI for visualization**, the dashboard provides insights into claim behavior, fraud rates, and risk indicators.

The goal of this project is to demonstrate **data analysis and actuarial insights in the insurance industry**.

---

#  Objectives

- Analyze insurance claims data
- Identify patterns related to **fraudulent claims**
- Explore relationships between:
  - claim severity
  - incident type
  - customer age
  - geographic location
- Build an **interactive Power BI dashboard**

---

#  Project Structure
insurance-fraud-dashboard
│
├── data
│ └── insurance_claims.csv
│
├── scripts
│ └── lifeinsurance.py
│
├── dashboard
│ └── insurance_fraud_dashboard.pbix
│
├── images
│ └── dashboard_preview.png
│
└── README.md
---


---

#  Data Preparation

The dataset was cleaned using **Python (Pandas)**.

Main preprocessing steps:

- Handling missing values
- Converting categorical variables
- Transforming binary variables:
  - `property_damage`
  - `police_report_available`
  - `fraud_reported`
- Creating new analytical variables:
  - **Fraud Label**
  - **Age Groups**
  - **Claim Severity Categories**

---

#  Exploratory Data Analysis

Exploratory analysis was performed using **Python and visualization libraries** to better understand the dataset.

The analysis included:

- Customer age distribution
- Fraud case distribution
- Incident severity analysis
- Claim amount vs fraud status
- Claims by state
- Incident type frequency

---

#  Dashboard Features

The **Power BI dashboard** provides interactive insights into insurance claims and fraud detection.

## Key Performance Indicators (KPIs)

- Total Claims
- Fraud Cases
- Fraud Rate
- Total Claim Amount
- Average Claim Amount

---

## Main Visualizations

- Fraud vs Non-Fraud distribution
- Claims by Age Group
- Fraud by Incident Severity
- Claims by Incident Type
- Claims by State
- Claim Amount by Fraud Status

---

## Interactive Filters

The dashboard includes slicers for:

- Incident Type
- State
- Incident Severity

These filters allow users to explore fraud patterns across different segments of the data.

---

#  Key Insights

From the analysis we can observe:

- Approximately **24.7% of claims show fraud indicators**
- Fraudulent claims tend to have **higher average claim amounts**
- The most common incident types are:
  - Single vehicle collisions
  - Multi-vehicle collisions
- Most claims occur among customers aged **31–50**

---

#  Tools & Technologies

This project was built using:

- **Python**
- Pandas
- Matplotlib
- Seaborn
- **Power BI**
- Git
- GitHub

---

#  Dashboard Preview

<img width="1379" height="776" alt="image" src="https://github.com/user-attachments/assets/dfeb8609-d4d1-4366-a20a-e76221733b44" />


---

#  Future Improvements

Possible extensions of this project include:

- Building a **machine learning model to predict fraud probability**
- Implementing **feature engineering for risk scoring**
- Adding **time-series analysis of claims**
- Deploying the dashboard using **Power BI Service**

---

#  Author

**Oscar Salgado**

Projects focused on **insurance analytics, fraud detection, and actuarial data analysis**.

GitHub:  
https://github.com/osalgador

---

#  Project Purpose

This project was developed as part of a **data analytics and actuarial portfolio**, demonstrating skills in:

- Data cleaning
- Exploratory data analysis
- Data visualization
- Insurance risk analysis
- Fraud detection analytics
