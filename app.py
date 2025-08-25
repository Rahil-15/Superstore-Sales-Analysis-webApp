from flask import Flask, render_template
import analysis

app = Flask(__name__)

@app.route("/")
def index():
    summary = analysis.sales_profit_overview()

    # Charts
    category_chart = analysis.category_analysis()
    subcategory_chart = analysis.subcategory_analysis()
    region_chart = analysis.region_analysis()
    monthly_chart = analysis.monthly_sales_trend()
    segment_chart = analysis.segment_pie_chart()

    # Tables (new)
    summary_table = analysis.summary_table_html()
    category_table = analysis.category_sales_profit_table_html()
    region_table = analysis.region_sales_profit_table_html()

    return render_template(
        "index.html",
        summary=summary,
        category_chart=category_chart,
        subcategory_chart=subcategory_chart,
        region_chart=region_chart,
        monthly_chart=monthly_chart,
        segment_chart=segment_chart,
        summary_table=summary_table,
        category_table=category_table,
        region_table=region_table,
    )

if __name__ == "__main__":
    app.run(debug=True)
