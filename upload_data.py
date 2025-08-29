from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#url
uri="mongodb+srv://sensor:L7L40ucDPzJqrBPr@cluster0.tdppx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create new client and connect to server
client=MongoClient(uri)

#create database name and collection name
DATABASE_NAME='mlproject'
COLLECTION_NAME='waferfault'

df=pd.read_csv("E:\Generative AI\Projects\Sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
type(json_record)
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)