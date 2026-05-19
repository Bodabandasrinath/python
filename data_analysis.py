"""
Data Analysis with Pandas Project

Developed by: BODABANDA SRINATH
Role: Python Developer Intern

Features:
1. Load CSV dataset
2. Inspect dataset
3. Clean missing data
4. Filter records
5. Group and aggregate data
6. Generate insights
"""

# Import pandas library
import pandas as pd

# -------------------------------
# Step 1: Load Dataset
# -------------------------------

try:
    # Read CSV file
    df = pd.read_csv("sales_data.csv")

    print("Dataset Loaded Successfully!\n")

    # Display dataset
    print("Original Dataset:")
    print(df)

# -------------------------------
# Step 2: Inspect Dataset
# -------------------------------

    print("\nDataset Information:")
    print(df.info())

# -------------------------------
# Step 3: Clean Missing Data
# -------------------------------

    # Fill missing sales values with average sales
    average_sales = df["Sales"].mean()

    df["Sales"].fillna(average_sales, inplace=True)

    print("\nDataset After Cleaning Missing Values:")
    print(df)

# -------------------------------
# Step 4: Filtering Data
# -------------------------------

    # Filter Electronics department
    electronics = df[df["Department"] == "Electronics"]

    print("\nElectronics Department Data:")
    print(electronics)

# -------------------------------
# Step 5: Grouping and Aggregation
# -------------------------------

    # Group by department and calculate total sales
    department_sales = df.groupby("Department")["Sales"].sum()

    print("\nTotal Sales by Department:")
    print(department_sales)

# -------------------------------
# Step 6: Insights
# -------------------------------

    print("\nInsights:")
    print("1. Electronics department has the highest sales.")
    print("2. Missing sales data was cleaned using average sales.")
    print("3. Grouping helped analyze department performance.")

except FileNotFoundError:
    print("CSV file not found.")

except Exception as e:
    print("Error:", e)