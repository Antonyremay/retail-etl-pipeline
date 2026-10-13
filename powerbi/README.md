# Power BI and MySQL connection

The ETL pipeline loads rows into the MySQL `fact_retail_sales` table. The
dashboard's visuals use the existing model table
`retail_warehouse fact_retail_sales`.

## Connect the existing report

1. Open `retail_warehouse.pbix` in Power BI Desktop.
2. In Power Query Editor, select the query that loads
   `retail_warehouse fact_retail_sales`.
3. In **Advanced Editor**, update its MySQL source to match
   [mysql_fact_retail_sales.pq](./mysql_fact_retail_sales.pq), replacing
   `MYSQL_HOST` and `MYSQL_DATABASE` with the corresponding values from the
   local `.env` file. Keep the existing query name and any existing
   transformation steps needed by the model.
4. Select **Close & Apply**, then enter the MySQL username and password when
   Power BI prompts for database credentials. Use the same credentials as the
   ETL's `MYSQL_USER` and `MYSQL_PASSWORD`; do not put the password in the
   Power Query source.
5. Refresh the report and confirm its visuals load before saving the PBIX.

If Power BI reports that the MySQL connector is unavailable, install the
MySQL Connector/NET driver required by Power BI Desktop, then reopen the report.
