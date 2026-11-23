# Geospatial Data Analysis for Business Expansion

## Project Overview
This project analyzes geographical sales data to identify potential locations for business expansion. It combines sales performance, customer demand, and existing store availability to discover promising regions.

The project uses Python-based data analysis and interactive mapping tools to visualize sales distribution and evaluate expansion opportunities.

> Note: This project uses a synthetic dataset created for educational and internship practice purposes.

## Objectives
- Analyze sales performance across different cities.
- Visualize sales geographically using interactive maps.
- Identify high-demand areas with relatively low store presence.
- Compare sales, customer demand, and existing store counts.
- Recommend potential expansion locations based on demand-to-store ratio.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Folium
- Plotly

## Project Structure
```text
Geospatial_Data_Analysis/
│
├── dataset/
│   ├── geospatial_sales.csv
│   └── analyzed_geospatial_sales.csv
│
├── make_dataset.py
├── geospatial_analysis.py
├── sales_map.html
├── sales_by_city.png
├── customer_demand.png
├── expansion_opportunities.png
├── insights.txt
├── requirements.txt
└── README.md
```

## Analysis Performed
1. Dataset creation and preparation
2. Data cleaning and duplicate removal
3. Missing-value checking
4. Sales analysis by city
5. Customer demand analysis
6. Demand per existing store calculation
7. Expansion opportunity ranking
8. Geographical sales visualization
9. Business insight generation

## Visualizations
- Interactive geographical sales map
- Top 10 cities by sales
- Top 10 cities by customer demand
- Top 10 expansion opportunity cities

## Key Business Insights
The analysis identifies cities where customer demand is relatively high compared with the number of existing stores.

These locations may represent potential business expansion opportunities. The results should be validated with actual market data, competition analysis, operational costs, and profitability assessment before making real business decisions.

## How to Run the Project

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate the dataset
```bash
python make_dataset.py
```

### 4. Run the analysis
```bash
python geospatial_analysis.py
```

### 5. View the map
Open `sales_map.html` in your browser.

## Conclusion
This project demonstrates how geospatial analysis can support business expansion decisions by combining geographical information, sales performance, and customer demand into meaningful visual insights.

The project was developed as a Data Analytics internship task using Python and mapping tools.
