from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#для github
DATABASE_URL = os.getenv("DATABASE_URL")

#для timeweb
#DATABASE_URL = f"postgresql://tss_db_user:11111@localhost/tssdatabase."

#локально
#DATABASE_URL = f"postgresql://postgres:11111@localhost:5432/tssdatabase"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()