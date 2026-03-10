# E-Commerce Sales Data Pipeline

## Problem
An e-commerce company was experiencing revenue drops 
but had no visibility into which cities, categories, 
or time periods were underperforming.

## Solution
Built an end-to-end data pipeline that takes raw order 
data, cleans and transforms it using Python, stores it 
in Azure Data Lake Gen2, and visualizes insights in a 
Power BI dashboard.

## Pipeline Architecture
Raw CSV → Python (Pandas) → ADLS Gen2 → Power BI

## Tech Stack
- Python (Pandas, azure-storage-blob)
- Azure Data Lake Storage Gen2
- Azure Blob Storage
- Power BI

## Business Questions Answered
- Which state/city has most orders?
- Which day of week has highest orders?
- Which category/subcategory is most profitable?
- Which category sells most by month?

## How to Run
1. Clone this repo
2. Install dependencies: pip install pandas azure-storage-blob python-dotenv
3. Create .env file with your Azure credentials (see .env.example)
4. Add your CSV files to /archive folder
5. Run: python ecommerce_pipeline.py
```

## Dashboard Preview
<img width="1917" height="1035" alt="Ecommimgage" src="https://github.com/user-attachments/assets/03a47455-5b06-4a43-b8a8-dbd28959e7bc" />


Shivanshu Saxena
