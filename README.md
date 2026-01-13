# Heart Disease ETL Pipeline (Pandas + MySQL)

<p align="center">
  <img src="assets\heart.gif" alt="Project demo gif" width="400">
</p>


This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** built with **Python, Pandas, Docker, and MySQL**, following the **Medallion Lakehouse Architecture (Bronze, Silver, Gold)**.

The goal is to ingest a real-world medical dataset, apply data cleaning and transformations, persist the data into a relational database, and generate analytical tables ready for consumption.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Dataset Description](#dataset-description)
4. [Project Architecture](#project-architecture)
   - [Medallion Architecture](#medallion-architecture)
   - [Project Folder Structure](#project-folder-structure)
5. [ETL Pipeline Walkthrough](#etl-pipeline-walkthrough)
   - [Step 0 – Mental Preparation](#step-0--mental-preparation)
   - [Step 1 – Project Structure](#step-1--project-structure)
   - [Step 2 – Understanding the Dataset](#step-2--understanding-the-dataset)
   - [Step 3 – Extract (Bronze Layer)](#step-3--extract-bronze-layer)
   - [Step 4 – Transform (Silver Layer)](#step-4--transform-silver-layer)
   - [Step 5 – Database Modeling](#step-5--database-modeling)
   - [Step 6 – Database Infrastructure with Docker](#step-6--database-infrastructure-with-docker)
   - [Step 7 – Load (Silver to MySQL)](#step-7--load-silver-to-mysql)
   - [Step 8 – Gold Layer (Analytics)](#step-8--gold-layer-analytics)
6. [How to Run the Project](#how-to-run-the-project)
7. [Results and Analysis](#results-and-analysis)


---

## Project Overview

- **Objective:**  
  Build an end-to-end ETL pipeline that reads data from a CSV file, processes it using Pandas, and loads it into a SQL database for analytical use.

- **Data Source:**  
  Kaggle – Heart Disease Dataset  
  https://www.kaggle.com/datasets/neurocipher/heartdisease

- **Final Output:**  
  - A clean relational table containing patient-level data
  - An aggregated analytical table showing heart disease statistics by sex

This project focuses on **clarity, structure, and best practices**, simulating how a real-world data engineering pipeline works.

---

## Tech Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Database:** MySQL
- **Infrastructure:** Docker & Docker Compose
- **Connectivity:** SQLAlchemy, mysql-connector-python

---

## Dataset Description

The dataset contains **real-world medical data** used to predict the presence or absence of cardiovascular disease.

- Each row represents **one patient**
- Each column represents a **medical measurement or diagnostic indicator**

### Dataset Columns

| Column Name | Description | Type |
|------------|-------------|------|
| Age | Patient age | int64 |
| Sex | Gender (1 = Male, 0 = Female) | int64 |
| Chest pain type | Type of chest pain (1–4) | int64 |
| BP | Resting blood pressure (mm Hg) | int64 |
| Cholesterol | Serum cholesterol (mg/dL) | int64 |
| FBS over 120 | Fasting blood sugar > 120 mg/dL | int64 |
| EKG results | Resting ECG results (0–2) | int64 |
| Max HR | Maximum heart rate achieved | int64 |
| Exercise angina | Exercise-induced angina | int64 |
| ST depression | ST depression induced by exercise | float64 |
| Slope of ST | Slope of peak exercise ST segment | int64 |
| Number of vessels fluro | Number of major vessels (0–3) | int64 |
| Thallium | Thallium stress test result | int64 |
| Heart Disease | Target variable (Presence / Absence) | object |

---

## Project Architecture

### Medallion Architecture

This project follows the **Medallion Architecture**, commonly used in modern data platforms (e.g., Databricks).

Bronze (Raw Data)
↓
Silver (Cleaned & Standardized)
↓
Gold (Aggregated & Analytics)

**Important concept:**  
> Bronze, Silver, and Gold are **data states**, not just folders.

---

### Project Folder Structure
```
heart-disease-etl/
│
├── data/
│ ├── bronze/ # Raw data (original CSV)
│ ├── silver/ # Cleaned and standardized data
│ └── gold/ # Aggregated data (optional local storage)
│
├── src/
│ ├── extract/ # Data ingestion and inspection
│ ├── transform/# Data cleaning and transformations
│ └── load/ # Database loading and gold table creation
│
├── infra/
│ └── docker/ # Docker and database configuration
│
├── docs/
└── README.md
```

**Best Practice:**  
If the `/data` folder is deleted, the project **should still work**, since data can always be re-ingested.

---

## ETL Pipeline Walkthrough

### Step 0 – Mental Preparation

Before writing any code:

- Where does the data come from? → CSV (Kaggle)
- Where does it go? → SQL Database
- What changes in between? → Cleaning, renaming, aggregation

---

### Step 1 – Project Structure

- Code, data, and infrastructure are strictly separated
- The Medallion Architecture is used to organize data evolution

---

### Step 2 – Understanding the Dataset

- Static analysis of the dataset
- Column meanings, data types, and business context are documented
- No transformations yet

---

### Step 3 – Extract (Bronze Layer)

- The original CSV is placed in `data/bronze`
- A script in `src/extract`:
  - Reads the CSV
  - Inspects structure (columns, types, shape)
  - Does **not** modify or save data

**In companies:**  
Bronze data usually lives in a Data Lake (e.g., S3) and arrives via automated ingestion pipelines.

---

### Step 4 – Transform (Silver Layer)

- Basic transformations applied:
  - Column names standardized to `snake_case`
  - Duplicate rows removed
- Clean data saved to `data/silver`

This represents **trusted, cleaned data**, ready for persistence.

---

### Step 5 – Database Modeling

Before connecting to the database:

- Table schema is designed based on the Silver layer
- Data types are mapped from Pandas to SQL
- Primary key considerations are documented
- Nullability and future growth are considered

---

### Step 6 – Database Infrastructure with Docker

- MySQL runs inside a Docker container
- Docker Compose defines:
  - Database version
  - Credentials
  - Port mapping
  - Persistent volume

This simulates a real database environment safely and locally.

---

### Step 7 – Load (Silver to MySQL)

- The cleaned Silver CSV is loaded into MySQL
- Pandas + SQLAlchemy handle the insertion
- This completes the **core ETL pipeline**

<p align="center">
  <img src="assets\Screenshot_1.png" alt="table" width="600">
</p>


---

### Step 8 – Gold Layer (Analytics)

- Gold tables are **analytical**, not raw data
- Data is read from MySQL (Silver table)
- Aggregations are computed in Python
- A new table is created in MySQL

Example Gold table: heart_disease_by_sex

| sex | total_patients | total_with_disease | percentage_with_disease |
|-----|----------------|--------------------|-------------------------|

This table is optimized for **BI tools, dashboards, and reporting**.

<p align="center">
  <img src="assets\image.png" alt="table" width="600">
</p>
---

## How to Run the Project

1. Start the database:
   ```
   docker compose up -d
   ```
Install dependencies:
```
pip install pandas sqlalchemy mysql-connector-python

```

Run scripts in order:
```
src/extract

src/transform

src/load
```
Results and Analysis

- Clean patient-level data stored in MySQL

- Analytical Gold table summarizing heart disease by sex

- Data is ready for visualization tools like Power BI or Metabase

```
tchau :)
```
