# Retail ETL Pipeline & Sales Analytics Dashboard

An end-to-end retail data engineering and analytics project that uses Python, Pandas, MySQL, and Power BI to clean retail transaction data, load it into a database, and analyze sales performance.

## Project Dashboard

Click the screenshot to open the published Power BI report.

[![Retail Analytics Dashboard](retail-dashboard.png)](https://app.powerbi.com/groups/me/reports/8b937f24-11c6-448a-b1af-04ddaf027277/d1a562e65c0bf2b37de8?experience=power-bi)

[Open Dashboard Page](dashboard.md)

## Project Workflow

1. **Extract:** Read retail transaction data using Python and Pandas.
2. **Transform:** Clean and standardize data, validate fields, and remove duplicates.
3. **Load:** Insert the cleaned data into MySQL.
4. **Validate:** Reconcile loaded records against the source data.
5. **Analyze:** Use Power BI to explore sales trends, products, categories, and city-level performance.

## Technologies Used

- **Python** — ETL scripting and data processing
- **Pandas** — Data cleaning and transformation
- **MySQL** — Relational database and SQL queries
- **Power BI** — Interactive sales dashboard
- **Git and GitHub** — Version control and project documentation

## Dataset

The public practice dataset is available in [`public_data/retail_sales_public.csv`](public_data/retail_sales_public.csv).

- 25,000 rows
- 12 columns
- Synthetic retail sales data

The public dataset is intended for portfolio demonstration and excludes selected identifying fields from the original project data.

## Run the ETL Pipeline

1. Clone this repository.
2. Install the dependencies:

   ```bash
   pip install -r requirements_for_pipeline.txt
   ```

3. Configure your MySQL connection using environment variables. Keep credentials in a local `.env` file and never commit that file.
4. Ensure the required source data and MySQL database are available.
5. Run:

   ```bash
   python etl_pipeline.py
   ```

Refer to the code and database setup documentation for the exact configuration required by your environment.

## Repository Structure

```text
retail-etl-pipeline/
├── etl_pipeline.py
├── requirements_for_pipeline.txt
├── public_data/
│   ├── README.md
│   └── retail_sales_public.csv
├── powerbi/
│   ├── README.md
│   └── mysql_fact_retail_sales.pq
├── retail-dashboard.png
└── dashboard.md
```

## Project Highlights

- Built a Python-based ETL workflow for retail transaction data.
- Implemented data cleaning, validation, duplicate removal, and source-to-target reconciliation.
- Loaded transformed data into MySQL.
- Created a Power BI dashboard to analyze sales performance.

## Notes

The Power BI report may require Microsoft sign-in because public web publishing is not enabled for this report. The dashboard screenshot above provides a visual preview without requiring access to the interactive report.
