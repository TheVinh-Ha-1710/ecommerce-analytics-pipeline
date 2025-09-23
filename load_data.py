import psycopg2

# Connect to Postgres
con = psycopg2.connect(
    host="localhost",
    database="olist_data_modelling",
    user="postgres",
    password="Hathevinh@2003",
    port="5432"
)
cur = con.cursor()

# Create schema
cur.execute("CREATE SCHEMA IF NOT EXISTS dev_raw;")

# -------- ORDERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.orders (
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
    COPY dev_raw.orders
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_orders_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- ORDER ITEMS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.order_items (
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
    COPY dev_raw.order_items
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_items_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- CUSTOMERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.customers (
        customer_id TEXT,
        customer_unique_id TEXT,
        customer_zip_code_prefix INT,
        customer_city TEXT,
        customer_state TEXT
    );
""")
cur.execute("""
    COPY dev_raw.customers
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_customers_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- PRODUCTS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.products (
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
    COPY dev_raw.products
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_products_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- SELLERS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.sellers (
        seller_id TEXT,
        seller_zip_code_prefix INT,
        seller_city TEXT,
        seller_state TEXT
    );
""")
cur.execute("""
    COPY dev_raw.sellers
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_sellers_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- PAYMENTS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.payments (
        order_id TEXT,
        payment_sequential INT,
        payment_type TEXT,
        payment_installments INT,
        payment_value NUMERIC
    );
""")
cur.execute("""
    COPY dev_raw.payments
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_payments_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# -------- REVIEWS --------
cur.execute("""
    CREATE TABLE IF NOT EXISTS dev_raw.reviews (
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
    COPY dev_raw.reviews
    FROM 'D:/ecommerce-analytics-pipeline/datasets/olist_order_reviews_dataset.csv'
    DELIMITER ',' CSV HEADER;
""")

# Commit and close
con.commit()
cur.close()
con.close()

print("✅ All Olist tables loaded into Postgres successfully!")