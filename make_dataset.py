
import pandas as pd

data = {
    "City": [
        "Chennai", "Coimbatore", "Madurai", "Salem",
        "Tiruchirappalli", "Tirunelveli", "Erode", "Vellore",
        "Thoothukudi", "Dindigul", "Bengaluru", "Mysuru",
        "Hyderabad", "Vijayawada", "Kochi", "Thrissur",
        "Mumbai", "Pune", "Delhi", "Kolkata"
    ],

    "State": [
        "Tamil Nadu", "Tamil Nadu", "Tamil Nadu", "Tamil Nadu",
        "Tamil Nadu", "Tamil Nadu", "Tamil Nadu", "Tamil Nadu",
        "Tamil Nadu", "Tamil Nadu", "Karnataka", "Karnataka",
        "Telangana", "Andhra Pradesh", "Kerala", "Kerala",
        "Maharashtra", "Maharashtra", "Delhi", "West Bengal"
    ],

    "Latitude": [
        13.0827, 11.0168, 9.9252, 11.6643,
        10.7905, 8.7139, 11.3410, 12.9165,
        8.7642, 10.3673, 12.9716, 12.2958,
        17.3850, 16.5062, 9.9312, 10.5276,
        19.0760, 18.5204, 28.6139, 22.5726
    ],

    "Longitude": [
        80.2707, 76.9558, 78.1198, 78.1460,
        78.7047, 77.7567, 77.7172, 79.1325,
        78.1348, 77.9803, 77.5946, 76.6394,
        78.4867, 80.6480, 76.2673, 76.2144,
        72.8777, 73.8567, 77.2090, 88.3639
    ],

    "Sales": [
        95000, 72000, 45000, 38000, 52000,
        30000, 42000, 28000, 25000, 22000,
        110000, 65000, 98000, 58000, 68000,
        48000, 125000, 105000, 115000, 82000
    ],

    "Customer_Demand": [
        950, 850, 700, 650, 750,
        600, 720, 680, 620, 580,
        1100, 850, 1050, 800, 900,
        780, 1200, 1150, 1300, 900
    ],

    "Existing_Stores": [
        10, 3, 2, 2, 3, 1, 2, 1, 1, 1,
        12, 4, 9, 3, 5, 2, 15, 10, 14, 7
    ]
}

df = pd.DataFrame(data)

df.to_csv("dataset/geospatial_sales.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("\nTotal records:", len(df))
