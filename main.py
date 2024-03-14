from fastapi import FastAPI
from api.test_api.tests import test_router
from api.user_api.users import user_router
from database import Base, engine

app = FastAPI(
    title="Quiz app",
    docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(test_router)


@app.get('/')
async def home():
    return {'test': 'test'}
