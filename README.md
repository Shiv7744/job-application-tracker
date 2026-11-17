# Job Application Tracker

A full stack web app for tracking job applications, with a live analytics dashboard on top of the same database.

Built because a spreadsheet stopped being enough, and because I wanted to build a REST API from scratch rather than read about one.

## Architecture

```
                Postgres (applications table)
                   ↑                    ↑
         SQLAlchemy │                   │ live SQL connection
                    │                   │
            FastAPI (app/main.py)       │
                 :8000                  │
                ↑        ↑              │
          HTTP  │        │ HTTP         │
                │        │              │
         Swagger UI   index.html   Tableau dashboard
          (/docs)     (the app)      (analytics)
```

One database, two consumers. The API handles reads and writes for the application itself.
Tableau connects directly to the same table, read only, for aggregate analysis.

## Features

- Add, view, update and delete job applications
- Tracks company, role, location, status, date applied, link and notes
- REST API with automatic interactive documentation through Swagger UI
- Web interface that reads from the API and renders applications in a live table
- Tableau dashboard connected live to Postgres, showing response rate and application volume across 200 real applications

## Tech Stack

- **Database:** PostgreSQL
- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** HTML, JavaScript (fetch API)
- **Analytics:** Tableau Desktop, live connection to Postgres

## Schema

### applications

| Column | Type | Notes |
| --- | --- | --- |
| id | SERIAL PRIMARY KEY | |
| company | VARCHAR(100) | required |
| role | VARCHAR(100) | required |
| location | VARCHAR(100) | optional |
| status | TEXT | defaults to "Applied" |
| date_applied | DATE | required |
| link | TEXT | optional |
| notes | TEXT | optional |
| salary | TEXT | optional |
| rejection_reason | TEXT | optional |

## API Endpoints

| Method | Route | Description |
| --- | --- | --- |
| GET | /applications | List all applications |
| POST | /applications | Create a new application |
| PUT | /applications/{id} | Update an existing application |
| DELETE | /applications/{id} | Delete an application |

## Setup

**1. Clone the repo and create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Create the database**

```bash
createdb jobtracker
```

**3. Create the table**

Run the SQL in `schema.sql` against the `jobtracker` database.

**4. Start the server**

```bash
uvicorn app.main:app --reload
```

**5. Open the app**

Open `index.html` in a browser for the web interface, or visit
`http://127.0.0.1:8000/docs` for the interactive API docs.

## Loading data in bulk

The 200 applications in the database were loaded from a CSV export using a staging
table. Everything lands as text first, where nothing can fail on a malformed date or
a blank cell, then a single INSERT SELECT handles type conversion and filtering into
the real table. Raw first, then clean, rather than parsing on the way in.

## What I would do next

- Deploy the database to AWS RDS so the dashboard is not tied to a local machine
- Add an export endpoint to the API so the dashboard reads through the same layer the app does
- Add days since applied as a computed field
