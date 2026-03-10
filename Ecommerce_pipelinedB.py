# Databricks notebook source
df = spark.read.csv("/Volumes/shivdevcatalog/bronze/datavol/ecommerce_cleaned.csv",header=True,inferSchema=True)
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import round,sum,count

state_orders = df.groupBy("State").agg(count("Order ID").alias("Total_Orders")).orderBy("Total_Orders", ascending=False)
state_orders.show(10)

# COMMAND ----------

category_profit = df.groupBy("Category").agg(round(sum("Profit"),2).alias("Total_Profit")).orderBy("Total_Profit", ascending=False)
category_profit.show()

# COMMAND ----------

Orders_by_dayofweek = df.groupBy("Day of Week").agg(count("Order ID").alias("Total_Orders")).orderBy("Total_Orders",ascending=False)
Orders_by_dayofweek.show()

# COMMAND ----------

Revenue_by_month = df.groupBy("Month").agg(round(sum("Amount"),2).alias("Total_Revenue")).orderBy("Total_Revenue", ascending=False)

Revenue_by_month.show()

# COMMAND ----------

# Rename columns to remove spaces
df_clean = df.withColumnRenamed("Order ID", "Order_ID") \
             .withColumnRenamed("Order Date", "Order_Date") \
             .withColumnRenamed("Day of Week", "Day_of_Week") \
             .withColumnRenamed("Sub-Category", "Sub_Category")

df_clean.printSchema()

# COMMAND ----------

# Save as Delta table in Unity Catalog
df_clean.write.format("delta") \
              .mode("overwrite") \
              .saveAsTable("shivdevcatalog.bronze.ecommerce_orders")

print("Delta table saved!")


# COMMAND ----------

#Query the delta table using SQL
spark.sql("SELECT * FROM shivdevcatalog.bronze.ecommerce_orders LIMIT 5").show()

# COMMAND ----------

# Save state orders summary as Delta table
state_orders.write.format("delta") \
                  .mode("overwrite") \
                  .saveAsTable("shivdevcatalog.bronze.orders_by_state")

# Save category profit summary
category_profit.write.format("delta") \
                     .mode("overwrite") \
                     .saveAsTable("shivdevcatalog.bronze.profit_by_category")

print("Summary tables saved!")