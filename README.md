# E-commerce Customer Segmentation & RFM Analysis

**Live Demo Application: https://e-commerce-customer-segmentation-rfm-analysis-ks2p8vpsrkxcvvfu.streamlit.app/**

**Tech Stack:** Python, Pandas, Streamlit

### 🎯 Business Problem
Marketing teams often struggle with generic campaigns that waste budget on disengaged customers while neglecting high-value customers. 

**The Goal:** Build an automated segmentation tool using **RFM (Recency, Frequency, Monetary)** analysis to identify customer cohorts and tailor marketing strategies for maximum ROI.

### 💡 Solution
Analyzed over 400k transaction rows to find the most valuable customers.
* **Data Source:** https://archive.ics.uci.edu/dataset/502/online+retail+ii
* **Key Techniques:** Data cleaning, Feature Engineering, Visualization.
* **Visualization:** Used Streamlit to visualize the results in an interactive web application.

### 📊 Key Findings
* Customers were segmented into groups by using the RFM score (1-5):
    * Most Valuable Customers (Best Recency and Frequency)
    * Potential Loyal Customers (Good Recency, Medium Frequency)
    * New Customers (Best Recency, Low Frequency)
    * Promising Customers (Good Recency, Low Frequency)
    * Loyal Customers (Medium Recency, Best Frequency)
    * Need Attention (Medium Recency and Frequency)
    * At Risk (Poor Recency, Best Frequency)
    * Inactive (Worst Recency and Frequency)

### Dashboard Screeshots

**1. KPI view**
![KPI Dashboard](/images/image.png)

**2. Segment Analysis**
![Charts](/images/image-1.png)

