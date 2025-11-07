"""Interactive data analysis with Plotly visualizations"""

import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def ensure_output_dir():
    """Create outputs directory if it doesn't exist"""
    os.makedirs('outputs', exist_ok=True)

def load_data():
    """Load and validate the dataset"""
    try:
        df = pd.read_csv('cleaned_file.csv')
        print(f"Data loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: cleaned_file.csv not found in current directory")
        sys.exit(1)

def save_plot(fig, filename):
    """Save plot as interactive HTML"""
    output_path = os.path.join('outputs', filename)
    fig.write_html(output_path)
    print(f"Saved: {output_path}")

def plot_price_age_box(df):
    """Create box plots for price and age"""
    melted = df[['price', 'age']].melt(var_name='Variable', value_name='Value')
    fig = px.box(melted, x='Variable', y='Value', 
                 title='Distribution of Price and Age',
                 template='plotly_white')
    save_plot(fig, 'price_age_box.html')

def plot_price_age_scatter(df):
    """Create scatter plot of price vs age"""
    fig = px.scatter(df, x='price', y='age',
                    title='Price vs Age Relationship',
                    template='plotly_white')
    save_plot(fig, 'price_age_scatter.html')

def analyze_clv(df):
    """Analyze and visualize Customer Lifetime Value"""
    # Calculate CLV
    df['total_sales'] = df['quantity'] * df['price']
    clv_df = df.groupby(['customer_id', 'gender', 'age'])['total_sales'].sum().reset_index()
    clv_df.rename(columns={'total_sales': 'CLV'}, inplace=True)
    
    # CLV Distribution
    fig = px.histogram(clv_df, x='CLV', 
                      title='Customer Lifetime Value Distribution',
                      template='plotly_white',
                      marginal='box')
    save_plot(fig, 'clv_distribution.html')
    
    # CLV by Gender
    fig = px.box(clv_df, x='gender', y='CLV',
                 title='CLV Distribution by Gender',
                 template='plotly_white')
    save_plot(fig, 'clv_by_gender.html')
    
    # CLV vs Age
    fig = px.scatter(clv_df, x='age', y='CLV', color='gender',
                    title='CLV vs Age by Gender',
                    template='plotly_white')
    save_plot(fig, 'clv_vs_age.html')
    
    return clv_df

def analyze_reviews(df):
    """Analyze review scores and purchase frequency"""
    review_freq = df.groupby('review_score')['customer_id'].count().reset_index()
    review_freq.columns = ['review_score', 'purchase_count']
    
    correlation = np.corrcoef(review_freq['review_score'], 
                            review_freq['purchase_count'])[0, 1]
    
    fig = px.line(review_freq, x='review_score', y='purchase_count',
                  title=f'Review Score vs Purchase Frequency (correlation: {correlation:.2f})',
                  template='plotly_white',
                  markers=True)
    save_plot(fig, 'review_vs_purchases.html')

def analyze_age_spending(df):
    """Analyze spending patterns by age groups"""
    age_bins = [0, 20, 30, 40, 50, 60, 70, 100]
    age_labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
    
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)
    age_spending = df.groupby('age_group')['total_sales'].sum().reset_index()
    
    fig = px.bar(age_spending, x='age_group', y='total_sales',
                 title='Total Spending by Age Group',
                 template='plotly_white')
    save_plot(fig, 'age_spending.html')

def analyze_payment_methods(df):
    """Analyze payment method usage by gender"""
    payment_counts = df.groupby(['payment_method', 'gender']).size().reset_index(name='count')
    
    fig = px.bar(payment_counts, x='payment_method', y='count',
                 color='gender', title='Payment Methods by Gender',
                 template='plotly_white',
                 barmode='stack')
    save_plot(fig, 'payment_methods.html')

def main():
    """Main execution flow"""
    ensure_output_dir()
    df = load_data()
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(df[['price', 'age']].describe())
    
    # Generate all plots
    plot_price_age_box(df)
    plot_price_age_scatter(df)
    
    clv_df = analyze_clv(df)
    print("\nCLV Summary:")
    print(clv_df['CLV'].describe())
    
    analyze_reviews(df)
    analyze_age_spending(df)
    analyze_payment_methods(df)
    
    print("\nAll interactive plots have been saved to the 'outputs' directory!")

if __name__ == '__main__':
    main()