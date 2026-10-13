from pathlib import Path
import pandas as pd

source = Path("duka_sales.csv")
output = Path("looker_studio_upload.csv")

df = pd.read_csv(source)
df["order_date"] = pd.to_datetime(df["order_date"], errors="raise")
df["revenue"] = df["quantity"] * df["unit_price"]
df["month"] = df["order_date"].dt.strftime("%Y-%m")
df["month_label"] = df["order_date"].dt.strftime("%b %Y")

df.to_csv(output, index=False, encoding="utf-8")

print("LOOKER STUDIO DATA PREPARATION")
print("Output:", output.resolve())
print("Rows:", len(df))
print("Distinct orders:", df["order_id"].nunique())
print("Total revenue: KES", f"{df['revenue'].sum():,.2f}")
print("Average revenue per order: KES", f"{df['revenue'].sum() / df['order_id'].nunique():,.2f}")
print("Missing values:", int(df.isna().sum().sum()))
print("Columns:", ", ".join(df.columns))
print("File exists:", output.exists())
