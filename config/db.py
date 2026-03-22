from sqlalchemy import create_engine, MetaData
from urllib.parse import quote_plus
import os


DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", "lalasa@123"))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "restapi_db")


engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
meta = MetaData()

try:
    conn = engine.connect()
    print("Database connected!")
except Exception as e:
    print("Database connection failed:", e)