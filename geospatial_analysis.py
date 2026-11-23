
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/geospatial_sales.csv")

print("----- ORIGINAL DATA -----")
print(df.head())

# 1. Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Remove rows with missing important information
df = df.dropna(subset=[
    "City", "State", "Latitude", "Longitude",
    "Sales", "Customer_Demand", "Existing_Stores"
])

# 4. Check data types
print("\n----- DATA TYPES -----")
print(df.dtypes)

# 5. Calculate demand per existing store
df["Demand_Per_Store"] = (
    df["Customer_Demand"] / df["Existing_Stores"]
)

# 6. Calculate sales per store
df["Sales_Per_Store"] = (
    df["Sales"] / df["Existing_Stores"]
)

# 7. Rank cities based on demand per store
df["Expansion_Rank"] = df["Demand_Per_Store"].rank(
    ascending=False
)

# 8. Sort cities by expansion opportunity
df = df.sort_values(
    by="Demand_Per_Store",
    ascending=False
)

# 9. Save analyzed dataset
df.to_csv("dataset/analyzed_geospatial_sales.csv", index=False)

# 10. Display results
print("\n----- TOP EXPANSION OPPORTUNITIES -----")

print(
    df[[
        "City",
        "State",
        "Sales",
        "Customer_Demand",
        "Existing_Stores",
        "Demand_Per_Store"
    ]].head(10)
)

print("\nAnalysis completed successfully!")

import folium

# Create map centered on India
sales_map = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5,
    tiles="CartoDB positron"
)

# Identify top 5 potential expansion cities
top_cities = df.nlargest(5, "Demand_Per_Store")["City"].tolist()

# Add city markers
for _, row in df.iterrows():

    # Highlight potential expansion locations
    if row["City"] in top_cities:
        marker_color = "red"
    else:
        marker_color = "blue"

    # Circle size based on sales
    radius = max(5, min(15, row["Sales"] / 10000))

    popup_text = f"""
    <b>City:</b> {row['City']}<br>
    <b>State:</b> {row['State']}<br>
    <b>Sales:</b> ₹{row['Sales']:,}<br>
    <b>Customer Demand:</b> {row['Customer_Demand']:,}<br>
    <b>Existing Stores:</b> {row['Existing_Stores']}<br>
    <b>Demand Per Store:</b> {row['Demand_Per_Store']:.2f}<br>
    <b>Expansion Candidate:</b> {'Yes' if row['City'] in top_cities else 'No'}
    """

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=radius,
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=row["City"],
        color=marker_color,
        fill=True,
        fill_color=marker_color,
        fill_opacity=0.7
    ).add_to(sales_map)

# Add map legend
legend_html = """
<div style="
position: fixed;
bottom: 30px;
left: 30px;
width: 190px;
background-color: white;
border: 2px solid grey;
z-index: 9999;
padding: 10px;
font-size: 14px;">
<b>Geospatial Sales Map</b><br>
<span style="color:red;">●</span> Expansion candidates<br>
<span style="color:blue;">●</span> Other business locations
</div>
"""

sales_map.get_root().html.add_child(folium.Element(legend_html))

# Save map
sales_map.save("sales_map.html")

print("\nInteractive map created: sales_map.html")

import matplotlib.pyplot as plt

# Chart 1: Top 10 cities by sales
top_sales = df.nlargest(10, "Sales").sort_values("Sales")

plt.figure(figsize=(10, 6))
plt.barh(top_sales["City"], top_sales["Sales"])
plt.title("Top 10 Cities by Sales")
plt.xlabel("Sales Revenue (₹)")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("sales_by_city.png")
plt.show()


# Chart 2: Top 10 cities by customer demand
top_demand = df.nlargest(10, "Customer_Demand").sort_values(
    "Customer_Demand"
)

plt.figure(figsize=(10, 6))
plt.barh(top_demand["City"], top_demand["Customer_Demand"])
plt.title("Top 10 Cities by Customer Demand")
plt.xlabel("Customer Demand")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("customer_demand.png")
plt.show()


# Chart 3: Top 10 expansion opportunities
top_expansion = df.nlargest(10, "Demand_Per_Store").sort_values(
    "Demand_Per_Store"
)

plt.figure(figsize=(10, 6))
plt.barh(top_expansion["City"], top_expansion["Demand_Per_Store"])
plt.title("Top 10 Expansion Opportunities")
plt.xlabel("Customer Demand per Existing Store")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("expansion_opportunities.png")
plt.show()

print("\nAll charts created successfully!")

# BUSINESS INSIGHTS REPORT

print("\n========== BUSINESS INSIGHTS ==========")

# Highest sales city
highest_sales_city = df.loc[df["Sales"].idxmax()]

# Highest demand city
highest_demand_city = df.loc[df["Customer_Demand"].idxmax()]

# Best expansion opportunity
best_expansion = df.loc[df["Demand_Per_Store"].idxmax()]

# Total sales
total_sales = df["Sales"].sum()

# Total customer demand
total_demand = df["Customer_Demand"].sum()

# Total existing stores
total_stores = df["Existing_Stores"].sum()

print(f"\nTotal Sales: Rs. {total_sales:,}")
print(f"Total Customer Demand: {total_demand:,}")
print(f"Total Existing Stores: {total_stores}")

print(
    f"\nHighest Sales City: {highest_sales_city['City']}"
    f" (Rs. {highest_sales_city['Sales']:,})"
)

print(
    f"\nHighest Demand City: {highest_demand_city['City']}"
    f" ({highest_demand_city['Customer_Demand']} customers)"
)

print(
    f"\nBest Expansion Candidate: {best_expansion['City']}"
    f" (Demand per Store: {best_expansion['Demand_Per_Store']:.2f})"
)

# Top 5 expansion locations
top5 = df.nlargest(5, "Demand_Per_Store")

print("\n----- TOP 5 EXPANSION LOCATIONS -----")

print(
    top5[[
        "City",
        "State",
        "Customer_Demand",
        "Existing_Stores",
        "Demand_Per_Store"
    ]].to_string(index=False)
)

# Save insights to text file
with open("insights.txt", "w", encoding="utf-8") as file:

    file.write("GEOSPATIAL DATA ANALYSIS - BUSINESS INSIGHTS\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Total Sales: Rs. {total_sales:,}\n")
    file.write(f"Total Customer Demand: {total_demand:,}\n")
    file.write(f"Total Existing Stores: {total_stores}\n\n")

    file.write(
        f"Highest Sales City: {highest_sales_city['City']}\n"
    )

    file.write(
        f"Highest Demand City: {highest_demand_city['City']}\n"
    )

    file.write(
        f"Best Expansion Candidate: {best_expansion['City']}\n\n"
    )

    file.write("Top 5 Expansion Locations:\n")

    file.write(
        top5[[
            "City",
            "State",
            "Customer_Demand",
            "Existing_Stores",
            "Demand_Per_Store"
        ]].to_string(index=False)
    )

    file.write("\n\nConclusion:\n")

    file.write(
        "Locations with high customer demand and fewer existing stores "
        "may offer opportunities for business expansion. Further analysis "
        "of costs, competition, and profitability is recommended before "
        "making actual business decisions.\n"
    )

print("\nInsights saved successfully to insights.txt")




