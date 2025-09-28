import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

# Connect to Postgres
con = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DATABASE"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)
cur = con.cursor()

# Create schema
cur.execute("CREATE SCHEMA IF NOT EXISTS dev_raw;")

# -------- ORDERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.order (
        order_id TEXT,
        customer_id TEXT,
        order_status TEXT,
        order_purchase_timestamp TIMESTAMP,
        order_approved_at TIMESTAMP,
        order_delivered_carrier_date TIMESTAMP,
        order_delivered_customer_date TIMESTAMP,
        order_estimated_delivery_date TIMESTAMP
    );
""")
cur.execute("""
    COPY dev_raw.order
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_orders_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- ORDER ITEMS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.order_item (
        order_id TEXT,
        order_item_id INT,
        product_id TEXT,
        seller_id TEXT,
        shipping_limit_date TIMESTAMP,
        price NUMERIC,
        freight_value NUMERIC
    );
""")
cur.execute("""
    COPY dev_raw.order_item
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_items_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- CUSTOMERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.customer (
        customer_id TEXT,
        customer_unique_id TEXT,
        customer_zip_code_prefix INT,
        customer_city TEXT,
        customer_state TEXT
    );
""")
cur.execute("""
    COPY dev_raw.customer
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_customers_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- PRODUCTS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.product (
        product_id TEXT,
        product_category_name TEXT,
        product_name_length INT,
        product_description_length INT,
        product_photos_qty INT,
        product_weight_g NUMERIC,
        product_length_cm NUMERIC,
        product_height_cm NUMERIC,
        product_width_cm NUMERIC
    );
""")
cur.execute("""
    COPY dev_raw.product
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_products_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- SELLERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.seller (
        seller_id TEXT,
        seller_zip_code_prefix INT,
        seller_city TEXT,
        seller_state TEXT
    );
""")
cur.execute("""
    COPY dev_raw.seller
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_sellers_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- PAYMENTS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.payment (
        order_id TEXT,
        payment_sequential INT,
        payment_type TEXT,
        payment_installments INT,
        payment_value NUMERIC
    );
""")
cur.execute("""
    COPY dev_raw.payment
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_payments_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- REVIEWS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.review (
        review_id TEXT,
        order_id TEXT,
        review_score INT,
        review_comment_title TEXT,
        review_comment_message TEXT,
        review_creation_date TIMESTAMP,
        review_answer_timestamp TIMESTAMP
    );
""")
cur.execute("""
    COPY dev_raw.review
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_reviews_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# Commit and close
con.commit()
cur.close()
con.close()

print("✅ All Olist tables loaded into Postgres successfully!")