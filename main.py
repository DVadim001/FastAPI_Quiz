from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    beginner = 'beginner'
    middle = 'middle'
    advanced = 'advanced'


app = FastAPI(docs_url='/')


@app.get('/')
async def home():
    return {'test': 'test'}
