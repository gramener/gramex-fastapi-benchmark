import pandas as pd
from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()
client = MongoClient('localhost', 27017)
db = client.testdatabase
collection = db.testcollection


@app.get("/mongo")
async def root():
    cursor = collection.find({})
    data = pd.DataFrame(list(cursor))
    data['_id'] = data['_id'].astype(str)
    return data.to_dict(orient='records')
