# Insurance Fraud Detection Dashboard
---
## Dashboard preview
![Dashboard Preview](images/Fraud_Dashboard.png)

---
## Project Overview

This project analyzes **insurance claim data** to identify patterns associated with **fraudulent claims**.  
Using **Python for data cleaning and exploratory data analysis (EDA)** and **Power BI for visualization**, the project highlights fraud indicators, claim distributions, and potential risk patterns across multiple variables.

The objective of this project is to demonstrate practical skills in:

- Data cleaning and preprocessing
- Exploratory data analysis
- Fraud pattern identification
- Business intelligence dashboard development

This project is part of a **data analytics and actuarial portfolio focused on insurance risk analysis**.

---

# Project Objectives

The main objectives of this analysis are:

- Analyze insurance claim data
- Identify patterns associated with **fraudulent claims**
- Explore relationships between:
  - claim severity
  - incident type
  - customer age
  - geographic location
- Develop an **interactive Power BI dashboard** for data-driven insights

---

# Dashboard Features

The Power BI dashboard provides a comprehensive overview of claim activity and fraud indicators.

### Key Performance Indicators (KPIs)

- **Total Claims:** 1000
- **Fraud Cases:** 247
- **Fraud Rate:** 24.7%
- **Total Claim Amount:** 53M+
- **Average Claim Amount:** 52.7K+

---

### Main Visualizations

The dashboard includes several analytical views:

• **Fraud vs Non-Fraud Distribution**  
Shows the proportion of fraudulent vs legitimate claims.

• **Claims by Age Group**  
Analyzes claim frequency across customer age groups.

• **Fraud vs Non-Fraud by Incident Severity**  
Examines how fraud cases are distributed across different levels of claim severity.

• **Claims by Incident Type**  
Shows which types of incidents generate the largest claim amounts.

• **Fraud vs Non-Fraud by State**  
Highlights geographic distribution of fraud cases and claim activity across states.

• **Claim Amount by Fraud Status**  
Compares the number of claims between fraudulent and legitimate cases.



# Data Preparation

Data preprocessing and cleaning were performed using **Python and Pandas**.

Key steps included:

- Handling missing values
- Cleaning categorical variables
- Converting binary indicators:
  - `property_damage`
  - `police_report_available`
  - `fraud_reported`
- Creating analytical features:
  - **Fraud Label**
  - **Age Groups**
- Preparing the dataset for visualization in Power BI

---

# Exploratory Data Analysis

Exploratory analysis was conducted to understand the structure and behavior of the data.

The analysis included:

- Customer age distribution
- Fraud case distribution
- Incident severity analysis
- Claim amount vs fraud status
- Claims by geographic location
- Incident type frequency

These insights guided the design of the Power BI dashboard.

---

# Key Insights

The analysis reveals several interesting patterns:

• Approximately **24.7% of claims show fraud indicators**.

• Fraudulent claims appear more frequently in **major damage incidents** compared to minor damage claims.

• The most common incident types are:

- Single vehicle collisions
- Multi-vehicle collisions

• Most claims occur among customers aged **31–50 years old**.

• Fraud distribution varies across states, suggesting **possible regional risk patterns**.
---

# Machine Learning: Fraud Prediction Model

To extend the analysis beyond visualization, a machine learning model was developed to **predict the probability of fraudulent claims**.

---

## Model Approach

The problem was framed as a **binary classification task**, where:

- **0 → Non-Fraud**
- **1 → Fraud**

The dataset was preprocessed using:

- One-hot encoding for categorical variables
- Feature engineering (age groups, damage indicators)
- Train-test split (80/20)

---

## Logistic Regression Model (Final Model)

Logistic Regression was selected as the primary model due to its interpretability and strong performance.

### Model Performance

- **Accuracy:** 76%
- **ROC-AUC:** 0.726
- **Fraud Recall:** 65%
- **Fraud Precision:** 55%

### Interpretation

- The model successfully detects **65% of fraudulent claims**, significantly improving detection compared to baseline approaches.
- ROC-AUC of **0.726** indicates good discrimination between fraud and non-fraud cases.
- The model maintains a good balance between precision and recall, which is critical in fraud detection scenarios.

---

## Random Forest Model

A Random Forest model was also evaluated to compare performance.

### Model Performance

- **Accuracy:** 70%
- **ROC-AUC:** 0.726
- **Fraud Recall:** 27%
- **Fraud Precision:** 44%

### Interpretation

Although Random Forest achieved a similar ROC-AUC score, it failed to effectively detect fraudulent cases, capturing only **27% of fraud instances**.

---

## Model Comparison

| Metric | Logistic Regression | Random Forest |
|--------|------------------|--------------|
| Accuracy | 76% | 70% |
| ROC-AUC | 0.726 | 0.726 |
| Fraud Recall | **65%** | 27% |
| Fraud Precision | 55% | 44% |

---

## Final Model Selection

Logistic Regression was selected as the final model due to its superior ability to detect fraudulent claims.

In fraud detection, **recall is more important than accuracy**, as failing to detect fraud leads to direct financial loss.

---

## Key Model Insights

The model identified several important drivers of fraud:

- **Severe accidents** significantly increase fraud probability
- **Higher claim amounts and total damage** are strong fraud indicators
- **Policy-related variables** (deductibles, limits) influence fraud behavior
- **Incident characteristics** (type and severity) are key predictors

These findings align with real-world insurance risk patterns, where fraud is often associated with **high-value and high-severity claims**.

---
---

# Tools & Technologies

This project was developed using the following tools:

- **Python**
- Pandas
- Matplotlib
- Seaborn
- **Power BI**
- Git
- GitHub

---

# Project Structure
 ```
insurance-fraud-dashboard
│
├── data
│ ├── insurance_claims.csv
│ └── insurance_fraud_dashboard.csv
│
├── scripts
│ ├── fraud_model.py
│ └── lifeinsurance.py
│
├── dashboard
│ └── Analysis_fraud.pbix
│
├── images
│ └── Fraud_Dashboard.png
│
└── README.md
```
 

---

#  Future Improvements

Possible extensions of this project include:

- Creating **fraud risk scoring models**
- Adding **time-series claim analysis**
- Deploying the dashboard through **Power BI Service**

---

#  Author

**Oscar Salgado**

Projects focused on **data analysis, insurance analytics, fraud detection, and actuarial insights**.

GitHub:  
https://github.com/osalgador

---

#  Project Purpose

This project was developed as part of a **data analytics and actuarial portfolio**, demonstrating practical skills in:

- Data cleaning
- Exploratory data analysis
- Fraud detection analysis
- Data visualization
- Insurance risk analysis
