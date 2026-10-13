# Data Methodology and Validation

## 1. Objective

Prepare a reproducible sales analysis for management using Duka Electronics transaction data covering 1 January–30 June 2026.

## 2. Source and Grain

The source file is `duka_sales.csv`. Each row represents a recorded sales transaction line. The `order_id` field identifies an order; multiple lines may belong to an order in other datasets, so distinct order counts must use unique order IDs rather than raw row counts.

## 3. Data Preparation

The validation process checks:

- Required columns are present.
- Dates can be interpreted as valid dates.
- Quantity and unit price values are numeric and positive.
- Missing values are identified.
- Duplicate rows and duplicate order identifiers are checked.
- Derived revenue values are calculated consistently.

The current dataset check recorded 1,000 rows, dates from 1 January to 30 June 2026, and no missing values, duplicate full rows, duplicate order IDs, invalid dates, or non-positive quantities or unit prices.

## 4. Measures

### Revenue

For each row:

`revenue = quantity × unit_price`

Total revenue is the sum of row-level revenue for the selected records.

### Distinct orders

Count unique values in `order_id`.

### Average revenue per order

`average revenue per order = total revenue ÷ distinct order count`

### Monthly revenue change

For each month after the first:

`month-over-month change (%) = ((current month revenue - previous month revenue) ÷ previous month revenue) × 100`

### Revenue contribution

`revenue share (%) = category revenue ÷ total revenue × 100`

When filters are applied, category shares should be calculated against the appropriate filtered total if that is how the dashboard is designed.

## 5. Validation Results

| Check | Observed result |
|---|---|
| Transaction rows | 1,000 |
| Reporting period | 1 Jan–30 Jun 2026 |
| Missing values | None recorded |
| Duplicate full rows | None recorded |
| Duplicate order IDs | None recorded |
| Invalid dates | None recorded |
| Non-positive quantity or unit price | None recorded |
| Total revenue | KES 81,391,500 |
| Distinct orders | 1,000 |
| Average revenue per order | KES 81,391.50 |

## 6. Analytical Results

- January revenue: KES 15,786,500.
- June revenue: KES 10,700,000.
- January-to-June change: approximately -32.22%.
- Leading product by revenue: Laptop, KES 36,125,000.
- Leading city by revenue: Nairobi, KES 24,652,000.
- Leading channel by revenue: Online, KES 44,753,000.

## 7. Reproducibility

From the project root:

```powershell
python -m pip install -r requirements.txt
python run_analysis.py
```

The notebook can also be opened with Jupyter and executed cell by cell. Re-run the analysis after changing the source data, and compare regenerated metrics and figures against the documented results.

## 8. Limitations

- The period covers six months and may not represent annual performance.
- Revenue is not profit because costs and margins are not included in this measure.
- The analysis is descriptive and cannot establish causation.
- Recommendations should be tested and reviewed using additional operational evidence.
