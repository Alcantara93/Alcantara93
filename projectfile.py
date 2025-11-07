import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import zscore, skew, kurtosis

# Create output directory for interactive plots
os.makedirs('outputs', exist_ok=True)

# Load dataset
try:
    data = pd.read_csv('cleaned_file.csv')
    df = pd.DataFrame(data)
    print("Data loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print("Error: cleaned_file.csv not found in current directory")
    sys.exit(1)

# Step 2: Central Tendency
central_tendency = df[['price', 'age']].agg({
    'price': ['mean', 'median', lambda x: ', '.join(map(str, x.mode())) if not x.mode().empty else 'No mode'],
    'age': ['mean', 'median', lambda x: ', '.join(map(str, x.mode())) if not x.mode().empty else 'No mode']
})
central_tendency.rename(index={central_tendency.index[2]: 'mode'}, inplace=True)

# Step 3: Dispersion
range_vals = df[['price', 'age']].apply(lambda x: x.max() - x.min())
variance = df[['price', 'age']].var(ddof=0)  # Population variance
std_dev = df[['price', 'age']].std(ddof=0)
iqr = df[['price', 'age']].apply(lambda x: np.percentile(x, 75) - np.percentile(x, 25))
print("=== Dispersion ===")
print(f"Range:\n{range_vals}\n")
print(f"Variance:\n{variance}\n")
print(f"Standard Deviation:\n{std_dev}\n")
print(f"IQR:\n{iqr}\n")

# Step 6: Print Summary
print("=== Central Tendency ===")
print(central_tendency, "\n")


df[['price', 'age']].boxplot()
plt.title("Box Plot of Price and Age")
plt.ylabel("Value")
plt.grid(True)
plt.show()

# for the price 
# the median is 257
#max= 498.6
# menimum price = 12
# the value for the lower quartile range 138.2
#the value for the uper quartile range 373.9

# for the age 
#the mean age is 18
#the median is 47.3
#the value for the lower quartile range 32.9
#the value for the uper quartile range 62.5

plt.scatter(df['price'], df['age'], color='red', marker='o')

plt.xlabel('price')
plt.ylabel('age')
plt.title('scutter plot vs.age')

plt.show()

# Step 1: Calculate total sales per transaction
df['total_sales'] = df['quantity'] * df['price']

# Step 2: Group by customer_id to calculate CLV
clv_df = df.groupby(['customer_id', 'gender', 'age'])['total_sales'].sum().reset_index()
clv_df.rename(columns={'total_sales': 'CLV'}, inplace=True)

import numpy as np

# Step 3: Summary statistics for CLV
clv_summary = clv_df['CLV'].describe()
clv_std = np.std(clv_df['CLV'])

clv_summary, clv_std

# Plot CLV distribution
plt.figure(figsize=(10, 6))
sns.histplot(clv_df['CLV'], bins=30, kde=True)
plt.title('Customer Lifetime Value (CLV) Distribution')
plt.xlabel('CLV')
plt.ylabel('Frequency')
plt.show()

# Boxplot: CLV by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(data=clv_df, x='gender', y='CLV')
plt.title('CLV by Gender')
plt.xlabel('Gender')
plt.ylabel('CLV')
plt.show()

# Scatterplot: CLV vs Age
plt.figure(figsize=(10, 6))
sns.scatterplot(data=clv_df, x='age', y='CLV', hue='gender')
plt.title('CLV vs Age')
plt.xlabel('Age')
plt.ylabel('CLV')
plt.show()

#Visual Insights:
#CLV Distribution: Positively skewed — most customers have moderate CLV, while a few have very high values.

#Gender Differences: Boxplot shows that both genders have a similar median CLV, but females may have slightly more high-value outliers.

#Age vs. CLV: There's no strong visible linear correlation, but clusters suggest some age groups may spend more.

# Step 1: Calculate the number of purchases per review score
review_freq = df.groupby('review_score')['customer_id'].count().reset_index()
review_freq.columns = ['review_score', 'purchase_count']

# Step 2: Calculate correlation
correlation = np.corrcoef(review_freq['review_score'], review_freq['purchase_count'])[0, 1]

# Step 3: Visualise the relationship
plt.figure(figsize=(8, 5))
plt.plot(review_freq['review_score'], review_freq['purchase_count'], marker='o', linestyle='-')
plt.title('Review Score vs Purchase Frequency')
plt.xlabel('Review Score')
plt.ylabel('Number of Purchases')
plt.grid(True)
plt.show()

review_freq, correlation

#Key Insights:
#There is a strong positive correlation (≈ 0.91) between review score and purchase frequency.
#Higher review scores are associated with more purchases, suggesting that satisfied customers may be more likely to buy again or leave positive feedback more often.

# Step 1: Create age bins
age_bins = [0, 20, 30, 40, 50, 60, 70, 100]
age_labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

# Step 2: Calculate total spending per age group
age_spending = df.groupby('age_group')['total_sales'].sum().reset_index()

# Step 3: Summary statistics using NumPy
spending_stats = {
    'mean': np.mean(age_spending['total_sales']),
    'std': np.std(age_spending['total_sales']),
    'max': np.max(age_spending['total_sales']),
    'min': np.min(age_spending['total_sales'])
}

# Step 4: Visualize the result
plt.figure(figsize=(10, 6))
sns.barplot(data=age_spending, x='age_group', y='total_sales')
plt.title('Total Spending by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Spending')
sns.barplot(data=age_spending, x='age_group', y='total_sales', palette='Set2')
plt.show()

age_spending, spending_stats

#Summary Statistics:
#Mean Spending: 76,472.53

#Standard Deviation: 30,694.40

#Highest Spending: Age 60–69

#Lowest Spending: Age <20

#Key Insight:
#Spending generally increases with age, peaking in the 60–69 group, then dropping off in the 70+ category — indicating a potential target segment for high-value marketing.

# Step 1: Group by payment_method and gender, count occurrences
payment_gender = df.groupby(['payment_method', 'gender']).size().unstack(fill_value=0)

# Step 2: Visualize using a stacked bar chart
payment_gender.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Payment Method Usage by Gender')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

payment_gender

#Observations:
#Cash on Delivery is the most used method for both genders, with males slightly favoring it more.

#Bank Transfer and Credit Card are used relatively evenly across genders.

#No drastic gender-based differences, but small preferences are visible.






