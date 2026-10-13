# Duka Electronics Dashboard Documentation

## Purpose

The dashboard presents sales performance for Duka Electronics from 1 January to 30 June 2026. It is intended to help management review headline KPIs, compare sales over time, and investigate performance by product, channel, branch, region, and customer tier.

## KPI Scorecards

| KPI | Definition |
|---|---|
| Total Revenue | Sum of quantity multiplied by unit price |
| Distinct Order Count | Number of unique order IDs |
| Average Revenue per Order | Total revenue divided by distinct order count |

The unfiltered dataset reports total revenue of KES 81,391,500, 1,000 distinct orders, and average revenue per order of KES 81,391.50.

## Required Visualisations

1. **Monthly revenue trend:** Compares revenue by month and highlights changes during the reporting period.
2. **Revenue by product:** Identifies product categories contributing most to total revenue.
3. **Revenue by channel:** Compares online and store sales.
4. **Revenue by branch:** Compares performance across branches.
5. **Revenue by region:** Compares geographic contribution.
6. **Revenue by customer tier:** Shows the contribution of Standard and Premium customers.

## Interactive Filters

Where supported by the dashboard implementation, filters should allow users to explore:

- Start and end dates.
- Product category.
- Sales channel.
- Branch.

KPI values and charts should update consistently when filters are changed. Confirm the behaviour in the published dashboard before submission.

## Main Findings

- Total revenue was KES 81,391,500 across 1,000 orders.
- Revenue declined from KES 15,786,500 in January to KES 10,700,000 in June.
- Laptops generated KES 36,125,000, or 44.38% of total revenue.
- Online sales generated KES 44,753,000, or 54.98% of total revenue.
- Nairobi generated KES 24,652,000, or 30.29% of total revenue.

These findings are descriptive and should be interpreted alongside the limitations in the project README.

## Screenshot Evidence

The project contains these evidence files:

- [Dashboard overview](dashboard_screenshots/dashboard-overview.png)
- [Dashboard breakdowns](dashboard_screenshots/dashboard-breakdowns.png)

These files document the dashboard evidence stored with the project. Ensure the images clearly show the actual dashboard and its charts before submitting.

## Access Link

**Published dashboard URL:** Not yet recorded.

If a hosted dashboard is required, insert the actual shareable URL here after confirming access permissions. A local screenshot or a Colab notebook is not itself a published Looker Studio report.

## Technical Notes

- Source dataset: `duka_sales.csv`
- Revenue formula: `quantity × unit_price`
- Reporting period: 1 January–30 June 2026
- Currency: Kenyan shillings (KES)

## Interpretation and Limitations

Revenue does not equal profit. The dataset does not by itself explain why revenue changes. Decisions about pricing, stock, marketing, or branch investment should consider costs, stock availability, returns, and other operational information.
