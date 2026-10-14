@'
# Retail Sales Practice Dataset

## Overview
This is a synthetic retail sales dataset prepared for a portfolio project demonstrating Python, Pandas, MySQL, ETL, and sales analytics.

## Dataset
- File: `retail_sales_public.csv`
- Rows: 25,000
- Columns: 12
- Missing values in the source data: 0

## Columns
- `order_date`: Transaction date
- `customer_city`: Customer city
- `store_code`: Store identifier
- `product_sku`: Product identifier
- `category`: Product category
- `quantity`: Quantity sold
- `unit_price`: Unit price
- `store_discount`: Store discount
- `payment_gateway_discount`: Payment gateway discount
- `tax_amount`: Tax amount
- `amount_paid`: Amount paid
- `transaction_type`: Transaction type

## Privacy
The public version excludes customer email addresses, order IDs, and order line item IDs. The dataset is described as synthetic practice data and is not intended to represent actual customer transactions.

## Usage
Use this CSV to practice data cleaning, exploratory analysis, SQL, dashboard creation, and retail sales reporting.

## Notes
Currency, discount conventions, and other business definitions should be confirmed from the project logic before interpreting financial metrics.
'@ | Set-Content -Encoding UTF8 .\public_data\README.md