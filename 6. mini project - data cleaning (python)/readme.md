
📌 Project Overview
This project performs end-to-end data cleaning and exploratory data analysis (EDA) on a real-world dirty cafe sales dataset. The dataset contained missing values, ERROR strings, wrong data types, and inconsistent entries — all of which were handled using Python and Pandas, Numpy.


🧹 Data Cleaning Steps
The raw dataset had several quality issues that were fixed before analysis:

👉 ERROR & blank values replaced with meaningful defaults ('UNKNOWN', 'Takeaway', 'Digital Wallet')
👉 Data type conversion — Price Per Unit, Total Spent, Quantity converted from object → float / int
👉 Logic-based imputation — missing values filled using relationships between columns:

      Total Spent = Quantity × Price Per Unit
      Quantity = Total Spent / Price Per Unit
      Price Per Unit = Total Spent / Quantity


👉 Date parsing — Transaction Date converted to datetime for monthly analysis
Rows dropped only when at least 2 of the 3 numeric columns were null (using thresh=2)


📊 Key Insights
🏆 Top 3 Selling Items
The 3 most purchased items by total quantity sold — showing customer preferences at the cafe.
💳 Revenue by Payment Method
Digital Wallet, Cash, and Credit Card compared by total revenue generated — helps identify the preferred payment mode.
📍 Most Profitable Location
In-store vs Takeaway revenue compared — showing which location drives more business.
📅 Peak Revenue Month
Month-wise revenue breakdown — identifies the busiest and most profitable months for the cafe.
💰 Total Revenue
Overall revenue generated across all transactions after data cleaning.

🛠️ Tools & Libraries Used
Python 3   -   Core programming language
Pandas  -   Data loading, cleaning, groupby analysis
NumPy  -   Handling NaN, numeric operations
VS Code   -  Development environment

📁 Project Structure
cafe-sales-analysis/
├── dirty_cafe_sales.csv        ← raw dataset
├── cafe_analysis.ipynb         ← main notebook
└── README.md                   ← this file






💡 What I Learned

How to handle real-world dirty data with ERROR strings and mixed types
Logic-based null imputation using column relationships
Using pd.to_numeric(errors='coerce') safely instead of astype() directly
GroupBy analysis to derive actionable business insights
Monthly trend analysis using dt.month on datetime columns