from fastapi import FastAPI
from .database import engine, Base
from .routers import custodians

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Data Catalog API", version="0.1.0")

app.include_router(custodians.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Catalog API"}