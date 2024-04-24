from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from backend.routers import default, chat #, vector_store

app = FastAPI()
app.include_router(default.router)
app.include_router(chat.router)
# app.include_router(vector_store.router)
