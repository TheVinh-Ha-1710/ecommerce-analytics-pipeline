# Olist E-commerce Analytics Report Pipeline

## 📌 Overview and Datasets
In this project, I build an end-to-end analytics pipeline for the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  
I automate the process of **data transformation, modeling, and visualization**, turning raw CSV files into meaningful insights.  
The original dataset is relational data schema with many tables such as customers, orders, products, reviews, and payments.  

Key dataset entities:
- **Customers**: Customer details such as unique IDs, city, and state.
- **Sellers**: Seller details such as unique IDs, city, and state.
- **Orders**: Order details including timestamps, status, and delivery dates.
- **Order_items**: Order item details including order number, quantities, prices.  
- **Products**: Product metadata including category and dimensions.  
- **Reviews**: Customer reviews with rating scores and timestamps.  
- **Payments**: Payment method, installments, and values.  

**Original Olist Schema**:  
![Original Schema](assets/original_schema.png)

---

## ⚙️ Project Design / Techstack
I design the project workflow with the following stack:  
- **dbt** for data transformation (staging → marts).  
- **Postgres** as the data warehouse.  
- **Power BI** for reporting and visualization.  
- **Olist dataset** (CSV) as the raw data source.
- **Python** for data ingestion into data warehouse.  

**Project Design Diagram**:  
![Project Design](assets/project_design.png)

---

## 🏗️ Transformed Schema (Marts Layer Design)
I model the marts layer using a **Star Schema** approach.  
It includes fact tables for sales and reviews, and dimension tables for customers, seller, products, and dates.  

**Star Schema Diagram**:
<div align="center">

![Star Schema](assets/star_schema.png)

</div>

---

## 🔗 Data Model Lineage
The lineage of models and transformations can be explored through **dbt docs**.  
It shows the dependencies across staging and marts models.  

**Data Lineage Diagram**:  
![Data Lineage](assets/dbt-dag.png)

---

## 📊 Visualization
The final output is an interactive **Power BI dashboard**.  
It provides insights into:
- Overview of revenue and products
- Sales trends over time.  
- Customer distribution.  
- Review scores and customer satisfaction.  

**Dashboard Preview**:  
![Dashboard](assets/dashboard.jpg)

---
