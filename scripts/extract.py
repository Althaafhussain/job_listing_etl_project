import requests
import pandas as pd
import os

url ="https://remotive.com/api/remote-jobs"

response = requests.get(url)

if response.status_code ==200:
    jobs = response.json()['jobs']

    df = pd.DataFrame(jobs)

    os.makedirs("data/raw", exist_ok=True)

    df.to_csv("data/raw/jobs.csv", index=False)

    print(f"Data Extracted Successfully: {len(df)} jobs")

else:
    print(f"Error: {response.status_code}")