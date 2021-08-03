import pandas as pd
from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()
client = MongoClient('localhost', port=27017)
db = client.testdatabase


@app.get('/admission')
async def root():
    collection = db.testcollection
    cursor = collection.find({})
    data = pd.DataFrame(list(cursor))
    data['_id'] = data['_id'].astype(str)
    return data.to_dict(orient='records')


@app.get('/imdb')
async def imdb(nconst: str):
    collection = db.imdbtitles
    cursor = collection.find({'nconst': nconst})
    data = pd.DataFrame(list(cursor))
    data['_id'] = data['_id'].astype(str)
    return data.to_dict(orient='records')
