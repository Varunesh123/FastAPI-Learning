from sqlalchemy import create_engine # Imports tools from SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base # Helps define database tables as Python classes
from sqlalchemy.orm import sessionmaker # Creates "sessions" (temporary connections) to the DB.

# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine("sqlite:///./test.db", echo=True)  # echo=logs what happens
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()