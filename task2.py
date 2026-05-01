import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Load dataset
# -----------------------------
df = pd.read_csv("cleaned_superstore.csv")

print("✅ Dataset Loaded Successfully\n")

# -----------------------------
# STEP 2: Basic Info
# -----------------------------
print("📌 Dataset Info:")
print(df.info())

print("\n📌 Statistical Summary:")
print(df.describe())

# -----------------------------
# STEP 3: KPIs
# -----------------------------
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("\n📊 KPIs:")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# -----------------------------
# STEP 4: Top 5 Products
# -----------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

print("\n🔥 Top 5 Products by Sales:")
print(top_products)

# -----------------------------
# STEP 5: Profit by Region
# -----------------------------
region_profit = df.groupby('Region')['Profit'].sum()

print("\n🌍 Profit by Region:")
print(region_profit)

# -----------------------------
# STEP 6: Monthly Sales Trend
# -----------------------------
df['Order Date'] = pd.to_datetime(df['Order Date'])

monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

print("\n📅 Monthly Sales Trend:")
print(monthly_sales)

# -----------------------------
# STEP 7: Visualization (SAVE IMAGES)
# -----------------------------

# Histogram
plt.figure()
df['Sales'].hist()
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("sales_histogram.png")
plt.close()

# Bar Chart
plt.figure()
region_profit.plot(kind='bar')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.savefig("region_profit_bar.png")
plt.close()

# Scatter Plot
plt.figure()
plt.scatter(df['Sales'], df['Profit'])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("sales_vs_profit.png")
plt.close()

print("\n📊 Charts saved as images!")

# -----------------------------
# STEP 8: Save Results
# -----------------------------
top_products.to_csv("top_products.csv")
region_profit.to_csv("region_profit.csv")
monthly_sales.to_csv("monthly_sales.csv")

print("\n✅ Task 2 Completed Successfully!")