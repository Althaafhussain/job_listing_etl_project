import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:YOUR_REAL_PASSWORD@localhost/jobs_db"
)

FILE_PATH = "/home/althaaf/job_listing_etl_project/data/processed/jobs.csv"

df = pd.read_csv(FILE_PATH)

df.to_sql(
    "jobs",
    con=engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully")
