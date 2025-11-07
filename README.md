# Interactive Data Analysis Dashboard

This project provides interactive data visualizations using Plotly to analyze customer behavior, sales patterns, and demographics.

## Interactive Visualizations

The analysis includes the following interactive plots (all saved as HTML files):

1. **Price and Age Distribution** (`price_age_box.html`, `price_age_scatter.html`)
   - Box plots showing distribution of prices and customer ages
   - Scatter plot revealing price vs age relationships

2. **Customer Lifetime Value (CLV) Analysis** (`clv_distribution.html`, `clv_by_gender.html`, `clv_vs_age.html`)
   - Distribution of customer lifetime values
   - CLV patterns by gender
   - Age impact on customer value

3. **Review and Purchase Analysis** (`review_vs_purchases.html`)
   - Interactive visualization of review scores vs purchase frequency
   - Correlation analysis with hover details

4. **Age-based Spending Patterns** (`age_spending.html`)
   - Bar chart of total spending by age group
   - Interactive tooltips with detailed statistics

5. **Payment Methods Analysis** (`payment_methods.html`)
   - Stacked bar chart of payment methods by gender
   - Interactive legends and filtering

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

## Features

- 🔍 **Zoom & Pan**: Explore specific regions of each plot
- 💡 **Tooltips**: Hover over data points for detailed information
- 📊 **Interactive Legends**: Show/hide specific data series
- 📷 **Export Options**: Save visualizations as PNG/SVG
- 📱 **Responsive Design**: Works on desktop and mobile browsers

## Requirements
- Python 3.x
- Plotly
- Pandas
- NumPy

## Data Requirements
The analysis expects a CSV file with these columns:
- price
- age
- quantity
- customer_id
- gender
- review_score
- payment_method
