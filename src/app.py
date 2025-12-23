import streamlit as st
import pandas as pd
import plotly.express as px

# Setting up the page configuration
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# Loading the data
@st.cache_data
def load_data():
    file_path = "data/processed/rfm_segments_cleaned.csv"
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.read_csv(f"../{file_path}")
    return df

df = load_data()

# Making a Title and Introduction
st.title("📊 E-Commerce Customer Segmentation")
st.markdown("""
This dashboard provides an overview of customer value using **RFM Analysis**. 
Filters on the left can be used to explore different customer segments.
""")

# Sidebar Filters
st.sidebar.header("Filter Customers")
segment_options = df['Segment'].unique().tolist()
selected_segments = st.sidebar.multiselect(
    "Select Customer Segments:",
    options=segment_options,
    default=segment_options
) 

filtered_df = df[df['Segment'].isin(selected_segments)]


# Display Key Performance Indicators
st.subheader("Key Performance Indicators")

# Creating 3 columns for metrics
col1, col2, col3 = st.columns(3)

# Calculating metrics
total_customers = filtered_df['Customer ID'].nunique()
total_revenue = filtered_df['Monetary'].sum()
avg_value = filtered_df['Monetary'].mean()

# Displaying metrics
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Total Revenue", f"€{total_revenue:,.2f}")
col3.metric("Avg. Customer Value", f"€{avg_value:,.2f}")

st.markdown("---")

# --- VISUALIZATIONS ---
st.subheader("Customer Segment Visualization")

# Create two columns for charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("### Who are our customers?")
    # Bar chart: Count of customers per segment
    segment_counts = filtered_df['Segment'].value_counts().reset_index()
    segment_counts.columns = ['Segment', 'Count']
    
    fig1 = px.bar(
        segment_counts, 
        x='Segment', 
        y='Count', 
        color='Segment',
        title="Customer Count by Segment",
        text_auto=True
    )
    st.plotly_chart(fig1, use_container_width=True)

with chart_col2:
    st.markdown("### Value vs. Recency")
    # Scatter plot: Monetary vs Recency
    fig2 = px.scatter(
        filtered_df, 
        x='Recency', 
        y='Monetary', 
        color='Segment',
        hover_data=['Customer ID'], # Show ID when hovering
        log_y=True, 
        title="Recency vs. Monetary Value (Log Scale)"
    )
    st.plotly_chart(fig2, use_container_width=True)

# BUSINESS RECOMMENDATIONS
st.markdown("---")
st.subheader("💎 Recommendations based on the analysis")

st.markdown("""
Based on the RFM analysis, here are the suggested actions:

1.  **Most Valuable Customers (High Value, Recent):**
    * **Action:** Loyalty programs, exclusive offers, early access to new products. 
    * **Goal:** Goal is to retain and nurture these customers, because they drive significant revenue.
    
2.  **At Risk (High Value, Not Recent):**
    * **Action:** Pernonalized campaigns, discounts, and re-engagement strategies.
    * **Goal:** Goal is to get them back to active purchasing.

3.  **Inactive (Low Value, Not Recent):**
    * **Action:** These are low priority customers. Low budget re-engagement campaigns.
    * **Goal:** Goal is to get them back to active purchasing, but focus on more promising segments.
""")