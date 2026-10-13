from pathlib import Path
import nbformat as nbf

root = Path.cwd()
script_path = root / "run_analysis.py"
notebook_path = root / "board_report.ipynb"

if not script_path.exists():
    raise FileNotFoundError("run_analysis.py was not found.")

analysis_code = script_path.read_text(encoding="utf-8-sig")

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {"name": "python"}
}

storyboard = r"""
# Duka Electronics Board Report — First Half of 2026

## Audience
The Duka Electronics board and CEO. They are non-technical decision-makers who need a concise, phone-readable summary before the board meeting.

## Decision owned by the board
Decide where to focus sales management, marketing attention and commercial investigation during the second half of 2026, based on product, location, channel and monthly revenue evidence.

## Big Idea
**Revenue is concentrated in laptops, Nairobi and online sales, while June revenue is below January. Protect the strongest revenue segments and investigate the decline before committing second-half resources.**

## SCR storyline

- **Situation:** Duka Electronics recorded KES 81.39 million in revenue across 1,000 distinct orders from January through June 2026.
- **Complication:** June revenue was 32.22% lower than January, while laptops, Nairobi and online sales represent substantial portions of total revenue; the dataset alone cannot explain the decline.
- **Resolution:** Review the monthly trend and investigate changes in demand, availability, pricing and conversion, while protecting the leading product, city and channel and testing targeted recovery actions.

## Analytical definitions
- Revenue = quantity × unit_price.
- Distinct order count = the number of unique order IDs.
- Average revenue per order = total order revenue divided by distinct orders.
- Revenue shares are calculated against total revenue for the reporting period.
- The source is `duka_sales.csv`, covering 1 January to 30 June 2026.

## Chart plan
1. Monthly revenue trend — shows the direction of revenue over time.
2. Revenue by product — compares product contribution.
3. Revenue by city — compares geographic contribution.
4. Revenue by channel — shows sales-channel composition.
5. Order revenue distribution — shows variation in order values.

All findings are descriptive. The analysis does not establish causal explanations for changes in revenue.
"""

comparison = r"""
# Before-and-after chart makeover

The two images below compare the original product revenue chart with the redesigned version.

## Design changes and reasons

1. **Descending vertical bars to sorted horizontal bars:** horizontal bars make product names easier to read on a phone.
2. **Generic title to an insight-led title:** the redesigned title names the leading product and its share of revenue.
3. **One colour for every bar to one highlight colour:** the leading product is highlighted in orange; other products use neutral grey.
4. **Implicit values to direct labels:** values are displayed on the bars, reducing the need to estimate from an axis.
5. **Generic axes to labelled units:** revenue is explicitly labelled in Kenyan shillings (KES).
6. **No source note to a source line:** readers can identify the data source and reporting period.
7. **Reduced chart clutter:** unnecessary borders and heavy gridlines are removed.

The makeover changes presentation, not the underlying data. The same product revenue aggregation is used in both versions.
"""

nb.cells = [
    nbf.v4.new_markdown_cell(storyboard),
    nbf.v4.new_markdown_cell(
        "# Data validation and analysis\n"
        "The next cell validates the source data, calculates metrics, "
        "creates the five report charts and saves the before-and-after images."
    ),
    nbf.v4.new_code_cell(analysis_code),
    nbf.v4.new_markdown_cell(comparison),
    nbf.v4.new_code_cell(
        "from IPython.display import display, Image\n"
        "from pathlib import Path\n"
        "\n"
        "for image_path in [Path('figures/before.png'), Path('figures/after.png')]:\n"
        "    print(image_path.as_posix())\n"
        "    display(Image(filename=str(image_path)))"
    ),
    nbf.v4.new_markdown_cell(
        "## Board interpretation and limitations\n\n"
        "- The January-to-June comparison describes endpoint change; it does not prove "
        "that revenue fell continuously in every intervening month.\n"
        "- Product, city and channel revenue shares identify concentration, not profit "
        "or customer acquisition cost.\n"
        "- The dataset does not provide marketing spend, stock availability, margins, "
        "returns or reasons for customer behaviour.\n"
        "- Before reallocating budgets, investigate monthly performance and validate "
        "operational explanations with additional data.\n"
        "- Use targeted experiments and monitor monthly revenue and order counts in "
        "the second half of 2026."
    )
]

nbf.write(nb, notebook_path)
print(f"Created {notebook_path.name}")
print(f"Notebook cells: {len(nb.cells)}")
print("First cell type:", nb.cells[0].cell_type)
print("Storyboard before plotting code:", nb.cells[0].cell_type == "markdown")
