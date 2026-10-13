import pandas as pd

df = pd.read_csv("duka_sales.csv")

print("Available columns:", df.columns.tolist())

date_cols = [c for c in df.columns if "date" in c.lower()]

for col in date_cols:
    dates = pd.to_datetime(df[col], errors="coerce")
    print(f"\nDate column: {col}")
    print("Earliest:", dates.min())
    print("Latest:", dates.max())

print("\nNumeric summary:")
print(df.describe(include="number").to_string())
