import pandas as pd
import plotly.express as px
from pathlib import Path

# Load dataset from data folder (uses YOUR data, not sample)
DATA_PATH = Path(__file__).resolve().parent / "data" / "Superstore.csv"
df = pd.read_csv(DATA_PATH, encoding="latin-1", parse_dates=["Order Date", "Ship Date"])

# -----------------------------
# Metrics for summary cards
# -----------------------------
def sales_profit_overview():
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    avg_sales_order = df.groupby("Order ID")["Sales"].sum().mean()

    return {
        "Total Sales": f"${total_sales:,.2f}",
        "Total Profit": f"${total_profit:,.2f}",
        "Total Quantity": f"{total_quantity:,}",
        "Avg Sales/Order": f"${avg_sales_order:,.2f}",
    }

# -----------------------------
# TABLES (as per requirements)
# -----------------------------
def summary_table_html():
    data = {
        "Metric": ["Total Sales", "Total Profit", "Total Quantity"],
        "Value": [
            f"${df['Sales'].sum():,.2f}",
            f"${df['Profit'].sum():,.2f}",
            f"{int(df['Quantity'].sum()):,}",
        ],
    }
    tbl = pd.DataFrame(data)
    return tbl.to_html(index=False, classes="table table-striped table-sm table-bordered")

def category_sales_profit_table_html():
    cat = (df.groupby("Category", as_index=False)
             .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
             .sort_values("Sales", ascending=False))
    # format nicely
    cat["Sales"] = cat["Sales"].map(lambda x: f"${x:,.2f}")
    cat["Profit"] = cat["Profit"].map(lambda x: f"${x:,.2f}")
    return cat.to_html(index=False, classes="table table-striped table-sm table-bordered")

def region_sales_profit_table_html():
    reg = (df.groupby("Region", as_index=False)
             .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
             .sort_values("Sales", ascending=False))
    reg["Sales"] = reg["Sales"].map(lambda x: f"${x:,.2f}")
    reg["Profit"] = reg["Profit"].map(lambda x: f"${x:,.2f}")
    return reg.to_html(index=False, classes="table table-striped table-sm table-bordered")

# -----------------------------
# CHARTS (existing)
# -----------------------------
def category_analysis():
    category_sales = df.groupby("Category", as_index=False)[["Sales", "Profit"]].sum()
    fig = px.bar(category_sales, x="Category", y="Sales", title="Sales by Category")
    return fig.to_html(full_html=False)

def subcategory_analysis():
    subcat_sales = df.groupby("Sub-Category", as_index=False)[["Sales", "Profit"]].sum()
    subcat_sales = subcat_sales.sort_values(by="Sales", ascending=False)
    fig = px.bar(subcat_sales, x="Sub-Category", y="Sales", title="Sales by Sub-Category")
    return fig.to_html(full_html=False)

def region_analysis():
    region_sales = df.groupby("Region", as_index=False)[["Sales", "Profit"]].sum()
    fig = px.bar(region_sales, x="Region", y="Sales", title="Sales by Region")
    return fig.to_html(full_html=False)

def monthly_sales_trend():
    df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)
    monthly_sales = df.groupby("YearMonth", as_index=False)["Sales"].sum()
    fig = px.line(monthly_sales, x="YearMonth", y="Sales", title="Monthly Sales Trend")
    return fig.to_html(full_html=False)

def segment_pie_chart():
    segment_sales = df.groupby("Segment", as_index=False)["Sales"].sum()
    fig = px.pie(segment_sales, names="Segment", values="Sales", title="Sales Share by Segment")
    return fig.to_html(full_html=False)
