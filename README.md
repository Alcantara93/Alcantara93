# Interactive Data Analysis Dashboard

This project provides interactive data visualizations using Plotly to analyze customer behavior, sales patterns, and demographics.

## Interactive Visualizations

### 1. Price and Age Distribution
📊 **Box Plots and Scatter Analysis**
- View distribution patterns in [`outputs/price_age_box.html`](outputs/price_age_box.html)
- Explore price-age relationships in [`outputs/price_age_scatter.html`](outputs/price_age_scatter.html)

Interactive features:
- Hover for exact values
- Box plot quartile information
- Zoom to investigate outliers
- Double-click to reset view

### 2. Customer Lifetime Value (CLV) Analysis
💰 **CLV Insights**
- Overall distribution: [`outputs/clv_distribution.html`](outputs/clv_distribution.html)
- Gender comparison: [`outputs/clv_by_gender.html`](outputs/clv_by_gender.html)
- Age correlation: [`outputs/clv_vs_age.html`](outputs/clv_vs_age.html)

Key features:
- Distribution shape analysis
- Gender-based comparisons
- Age-based value patterns
- Interactive legends

### 3. Review and Purchase Analysis
⭐ **Customer Satisfaction Impact**
- Detailed analysis: [`outputs/review_vs_purchases.html`](outputs/review_vs_purchases.html)

Interactive elements:
- Hover for exact review scores
- Purchase frequency details
- Trend line analysis
- Correlation statistics

### 4. Age-based Spending Patterns
👥 **Demographic Spending Analysis**
- Age group breakdown: [`outputs/age_spending.html`](outputs/age_spending.html)

Features:
- Spending by age group
- Interactive tooltips
- Comparative analysis
- Customizable view options

### 5. Payment Methods Analysis
💳 **Payment Preferences**
- Gender-based preferences: [`outputs/payment_methods.html`](outputs/payment_methods.html)

Interactive capabilities:
- Filter by gender
- Compare payment methods
- Percentage view option
- Detailed breakdowns

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/Alcantara93/Alcantara93.git
cd Alcantara93
```

2. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

3. Run the analysis:
```bash
python interactive_analysis.py
```

4. Open any `.html` file from the `outputs/` directory in your web browser to interact with the visualizations.

## How to Use the Interactive Plots

Each visualization is an interactive HTML file that you can open in your web browser. To use them:

1. Clone and set up the repository
2. Run the analysis script
3. Navigate to the `outputs/` directory
4. Open any `.html` file in your web browser
5. Interact with the plots:
   - 🔍 **Zoom**: Click and drag to zoom into specific areas
   - 🔄 **Reset**: Double-click to reset the view
   - 💡 **Details**: Hover over elements for detailed information
   - 🎨 **Legend**: Click legend items to show/hide data
   - 📷 **Export**: Use the camera icon to save as PNG

## Interactive Features Available

- 🔍 **Zoom & Pan**: Explore specific regions of each plot
- 💡 **Tooltips**: Hover over data points for detailed information
- 📊 **Interactive Legends**: Show/hide specific data series
- 📷 **Export Options**: Save visualizations as PNG/SVG
- 📱 **Responsive Design**: Works on desktop and mobile browsers
- 📈 **Statistical Insights**: Hover for numerical details
- 🎨 **Custom Views**: Toggle different aspects of the data

## Technical Requirements

### Software Requirements
- Python 3.x
- Plotly
- Pandas
- NumPy

### Data Requirements
The analysis expects a CSV file with these columns:
- `price`: Item price
- `age`: Customer age
- `quantity`: Number of items purchased
- `customer_id`: Unique identifier for each customer
- `gender`: Customer gender
- `review_score`: Product review rating
- `payment_method`: Method of payment used

## Running the Analysis

```bash
# Clone the repository
git clone https://github.com/Alcantara93/Alcantara93.git
cd Alcantara93

# Install dependencies
python -m pip install -r requirements.txt

# Run the analysis
python interactive_analysis.py

# Open any .html file from the outputs/ directory in your browser
```
