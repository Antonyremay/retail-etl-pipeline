let
    // Replace these with MYSQL_HOST and MYSQL_DATABASE from the local .env file.
    Server = localhost,
    Database = retail_warehouse,
    Source = MySQL.Database("localhost:3306", "retail_warehouse", [ReturnSingleDatabase=true]),
    FactRetailSales = Source{[Schema="retail_warehouse", Item="fact_retail_sales"]}[Data]
in
    FactRetailSales
