import pandas as pd

RAW_FILE = "/home/althaaf/job_listing_etl_project/data/raw/jobs.csv"
PROCESSED_FILE = "/home/althaaf/job_listing_etl_project/data/processed/jobs.csv"

df = pd.read_csv(RAW_FILE)

df = df[
    [
        "title",
        "company_name",
        "candidate_required_location",
        "salary",
        "job_type",
        "publication_date",
    ]
]

df = df.drop_duplicates()

df.columns = [
    "title",
    "company",
    "location",
    "salary",
    "job_type",
    "publication_date",
]

df.to_csv(PROCESSED_FILE, index=False)

print(f"Data Transformed Successfully: {len(df)} jobs")
