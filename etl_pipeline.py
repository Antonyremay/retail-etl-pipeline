import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

df = pd.read_csv("data/store_sales_v301.dat")
print(df.head())
print(df.info())
print(df.columns)
print(df.shape)

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

print("Connected to MySQL successfully!")
connection.close()

df = df.copy()

def data_clean(df):
    print("DATA TRANSFORMING")

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    df["customer_email"] = (
        df["customer_email"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    numeric_columns = [
        "quantity",
        "unit_price",
        "store_discount",
        "payment_gateway_discount",
        "tax_amount",
        "amount_paid"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df = df[df["quantity"] >= 0]

    df = df.drop_duplicates(
        subset=["order_id", "order_line_item"]
    )

    return df

print("Cleaned data:")
print(df.head())

print("Cleaned shape:")
print(df.shape)
def validate_data(df):
    print("DATA VALIDATION")

    print("Total rows:", len(df))
    print("Total columns:", len(df.columns))

    print("Missing values:")
    print(df.isnull().sum())

    print("Duplicate records:")
    print(
        df.duplicated(
            subset=["order_id", "order_line_item"]
        ).sum())
df = data_clean(df)
validate_data(df)
def load_data(df):

    print("LOADING DATA INTO MYSQL")

    connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

    cursor = connection.cursor()

    insert_query = """
        INSERT  IGNORE INTO fact_retail_sales (
            order_id,
            order_line_item,
            order_date,
            customer_email,
            customer_city,
            store_code,
            product_sku,
            category,
            quantity,
            unit_price,
            store_discount,
            payment_gateway_discount,
            tax_amount,
            amount_paid,
            transaction_type
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    data = [
        tuple(row)
        for row in df[
            [
                "order_id",
                "order_line_item",
                "order_date",
                "customer_email",
                "customer_city",
                "store_code",
                "product_sku",
                "category",
                "quantity",
                "unit_price",
                "store_discount",
                "payment_gateway_discount",
                "tax_amount",
                "amount_paid",
                "transaction_type"
            ]
        ].itertuples(index=False, name=None)
    ]

    cursor.executemany(insert_query, data)

    connection.commit()

    print(f"{cursor.rowcount} rows loaded successfully.")

    cursor.close()
    connection.close()

load_data(df)

def reconcile_data(df):

    print("\nRECONCILIATION")

    source_row_count = len(df)
    source_amount_paid = df["amount_paid"].sum()

    connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(amount_paid)
        FROM fact_retail_sales
    """)

    target_row_count, target_amount_paid = cursor.fetchone()

    print("Source row count:", source_row_count)
    print("Target row count:", target_row_count)

    print("Source amount paid:", source_amount_paid)
    print("Target amount paid:", target_amount_paid)

    if source_row_count == target_row_count:
        print("Row count reconciliation: PASSED")
    else:
        print("Row count reconciliation: FAILED")

    if round(source_amount_paid, 2) == round(float(target_amount_paid), 2):
        print("Amount reconciliation: PASSED")
    else:
        print("Amount reconciliation: FAILED")

    cursor.close()
    connection.close()
reconcile_data(df)
