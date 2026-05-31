import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:alsaja2005@localhost/jobs_db"
)

df = pd.DataFrame({
    "title": ["test"],
    "company": ["test"],
    "location": ["Remote"],
    "salary": ["1000"],
    "job_type": ["Full-time"],
    "publication_date": ["2026-05-31"]
})

print(type(engine))

df.to_sql(
    "jobs",
    con=engine,
    if_exists="append",
    index=False
)

print("Success")