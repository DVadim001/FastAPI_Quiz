from fastapi import FastAPI
from api.user_api.users import user_router
from database import Base, engine

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)
app.include_router(user_router)


@app.get('/')
async def home():
    return {'test': 'test'}
