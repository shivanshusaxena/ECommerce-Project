import pandas as pd
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient


load_dotenv() #load credentials from .env file

#os.getenv is key to load_dotenv()
#load_dotenv() → reads the .env file and loads all variables into memory
#os.getenv("STORAGE_ACCOUNT_NAME") → fetches the value of that specific variable

STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")


orders = pd.read_csv("/Users/shivanshumac/Documents/Python/Projects/archive/List of Orders.csv")
details = pd.read_csv("/Users/shivanshumac/Documents/Python/Projects/archive/Order Details.csv")
target = pd.read_csv("/Users/shivanshumac/Documents/Python/Projects/archive/Sales target.csv")

orders = orders.dropna(how='all') #remove the row where all columns are "NAN"
#print(orders.shape) #shape provide both count of rows and count of columns in a tuple

df = pd.merge(orders,details, on='Order ID', how='inner') ## merging two tables orders and orders detail on Order ID using inner join
#print(df.shape) #return rows and columns after join
#print(df.columns.tolist()) # return headers after join


# dayfirst=True tells pandas the format is DD-MM-YYYY
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True) #convert the column to date time format
df['Month'] = df['Order Date'].dt.month_name()
df['Day of Week'] = df['Order Date'].dt.day_name()


#print(df[['Order Date','Month','Day of Week']].head())

df.to_csv("ecommerce_cleaned.csv", index=False)
print("File Saved successfully")


def upload_to_adls(file_name):
    #create a connection to azure account
    connection_str = f"DefaultEndPointsProtocol=https;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={STORAGE_ACCOUNT_KEY};EndpointSuffix=core.windows.net"

    #create a client to interact with blob stoarage
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)

    #get the container
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)

    #upload the file
    with open(file_name,'rb') as data:
        blob_client.upload_blob(data,overwrite=True)
    
    print(f"✅ Uploaded {file_name} to ADLS container: {CONTAINER_NAME}")

upload_to_adls("/Users/shivanshumac/Documents/Python/ecommerce_cleaned.csv")






