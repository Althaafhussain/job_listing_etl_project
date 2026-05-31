# Job Listings ETL Pipeline

## Project Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline that collects remote job listings from the Remotive API, cleans and transforms the data using Pandas, loads it into PostgreSQL, and automates the workflow using Apache Airflow.

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Apache Airflow
* Requests

## Project Architecture

Remotive API
↓
Extract (Python)
↓
Raw CSV
↓
Transform (Pandas)
↓
Processed CSV
↓
Load (PostgreSQL)
↓
Airflow Scheduling

## Project Structure

job_listing_etl_project/

├── data/

│   ├── raw/

│   └── processed/

├── scripts/

│   ├── extract.py

│   ├── transform.py

│   └── load.py

├── dags/

│   └── job_etl_dag.py

├── requirements.txt

└── README.md

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE jobs_db;
```

Connect to the database and create the table:

```sql
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    salary VARCHAR(100),
    job_type VARCHAR(50),
    publication_date DATE
);
```

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd job_listing_etl_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the ETL Pipeline

Run the scripts in order:

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

## Running Airflow

Start the scheduler:

```bash
airflow scheduler
```

Start the webserver:

```bash
airflow webserver
```

Open Airflow UI:

http://localhost:8080

## Features

* Extracts job data from the Remotive API
* Cleans and transforms job listings
* Stores processed data in PostgreSQL
* Automated scheduling with Apache Airflow
* End-to-end ETL workflow

## Future Improvements

* Dockerize the pipeline
* Add data validation checks
* Deploy Airflow on the cloud
* Build dashboards using Power BI or Tableau
* Integrate additional job data sources
