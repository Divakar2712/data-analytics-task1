import pandas as pd

# Load dataset
df = pd.read_csv("Superstore.csv", encoding='latin1')

# Show first rows
print(df.head())

# Info
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Summary
print(df.describe())

# Save cleaned file
df.to_csv("cleaned_superstore.csv", index=False)

print("✅ Data Cleaning Completed")