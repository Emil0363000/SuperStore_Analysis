# SuperStore_Analysis

## Project Overview 

This project aims to build a complete data analysis and Business Intelligence workflow using Global Superstore dataset. The objective is to deliver a business insight and  answer questions such as: 
  - Which product generate profit or loss?
  - What is the impact of discount on profit?
  - Which market/country performs?
  - Which product categories are the most profitable?

Being able to answer these questions through data analysis can help to guide business decisions.

## Technical stack 

  - Raw dataset from Kaggle: https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset
  - ETL: Python & KNIME
  - Power Query
  - PowerBI

## Data pipeline 

Raw data -> Python -> KNIME -> Clean Dataset -> PowerBI -> Dashboard

## Python (Data exploration & cleaning)

The objective is to understand the data structure and quality using Pandas. 

  - Missing value (Postal code around 80%)
  - Outlier (extreme profit or shipping cost)
  - Data type (date initially in string format)

## KNIME (ETL) (Data cleaning & transformation)

The goal is to ensure data quality and enriched the dataset for analysis, producing a cleaned fact table and 5 dimensions tables (Customer, Product, Geography, Shipping mode and Date).

## Data modeling (PowerBI)

The model follows a star schema. This allows a performant and scalable data model. 

## DAX Measures 

The dax measures are stored in a dedicated table in PowerBI to improve usability and organization.

## Dashboard (PowerBI)

  - Page 1: Executive Overview
  - Page 2: Sales & Product analysis
  - Page 3: Geographic analysis
  - Page 4: Operations & Logistics
  - Page 5: Customer analysis

## Insight

  - High discount reduce profitability (once discounts reach around 25%, profit becomes close to zero or negative, particularly in the Technology and Furniture categories)
  - The Tables sub-category is highly unprofitable despite above average sales.
  - Revenue is distributed across many customers
  - Certain countries are significantly unprofitable
  - Some products generate revenue but destroy margin
  - There are spikes in both sales and profit during Q4 (especially November and December)
  - Top sales customers are not always the most profitable customers 
