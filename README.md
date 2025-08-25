
# 📊 Superstore Sales Analysis

A **Flask-based dashboard** that performs **Exploratory Data Analysis (EDA)** on the Superstore dataset.  
It provides insights into **sales, profit, categories, regions, customer segments, and trends** through interactive tables and charts.

---

##📁 Project Structure


superstore\_sales\_analysis/
├── app.py               # Flask app entry
├── analysis.py          # EDA functions (tables + charts)
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── static/
│   └── style.css        # CSS styling
├── templates/
│   └── index.html       # Dashboard (HTML + footer)
└── data/
└── Superstore.csv   # Dataset



---

## ⚙️ Setup Instructions

### 1. Clone / Download this repository
```bash
git clone https://github.com/yourusername/superstore_sales_analysis.git
cd superstore_sales_analysis
````

### 2. Create & activate a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

or using Flask CLI:

```bash
flask run
```

### 5. Open in browser

Visit **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** to view the dashboard.

---

## 📊 Features

### ✅ Tables

* **Summary Table**: Total Sales, Total Profit, Total Quantity
* **Category vs. Sales/Profit**
* **Region-wise Sales/Profit**

### ✅ Charts

* **Bar Chart**: Sales by Category
* **Bar Chart**: Sales by Sub-category
* **Bar Chart**: Sales by Region
* **Line Chart**: Monthly Sales Trend
* **Pie Chart**: Sales Share by Segment

---

## 🛠️ Requirements

* Python 3.8+
* Flask
* Pandas
* Plotly

Install via:

```bash
pip install -r requirements.txt
```

---

## 🎨 UI Enhancements

* Bootstrap 5 for responsive layout
* Interactive Plotly charts
* Custom CSS for cards and tables
* **Footer**: Developed by **Mohammadrahil Nasardi** with social links

---

## 🔗 Developer Info

👨‍💻 **Developed by**: Mohammadrahil Nasardi

🌐 **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/your_linkedin)
📸 **Instagram**: [Your Instagram](https://www.instagram.com/your_instagram)

---

## 📌 Notes

* Place your dataset in `data/Superstore.csv`.
* Required columns:
  `Order Date`, `Ship Date`, `Category`, `Sub-Category`, `Sales`, `Profit`, `Quantity`, `Segment`, `Region`, `City`.

---

```

