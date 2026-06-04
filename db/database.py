from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = f"postgresql://postgres:11111@localhost:5432/tssdatabase"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()