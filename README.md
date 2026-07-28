# Job Application Tracker

A full-stack web app to track job applications — built with PostgreSQL, FastAPI, and vanilla JavaScript.

## Features
- Add, view, update, and delete job applications
- Tracks company, role, location, status, date applied, link, and notes
- REST API with automatic interactive documentation (Swagger UI)
- Simple web interface to view applications in a live table

## Tech Stack
- **Database:** PostgreSQL
- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** HTML, JavaScript (fetch API)

## Schema
**applications**
| Column | Type | Notes |
|---|---|---|
| id | SERIAL PRIMARY KEY | |
| company | VARCHAR(100) | required |
| role | VARCHAR(100) | required |
| location | VARCHAR(100) | optional |
| status | VARCHAR(30) | defaults to "Applied" |
| date_applied | DATE | required |
| link | TEXT | optional |
| notes | TEXT | optional |

## API Endpoints
| Method | Route | Description |
|---|---|---|
| GET | /applications | List all applications |
| POST | /applications | Create a new application |
| PUT | /applications/{id} | Update an existing application |
| DELETE | /applications/{id} | Delete an application |

## Setup

1. Clone the repo and create a virtual environment:
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   \`\`\`

2. Set up PostgreSQL and create the database:
   \`\`\`
   createdb jobtracker
   \`\`\`

3. Run the schema SQL (see `schema.sql`) to create the `applications` table.

4. Start the server:
   \`\`\`
   uvicorn app.main:app --reload
   \`\`\`

5. Open `index.html` in your browser to view the app, or visit `http://127.0.0.1:8000/docs` for the interactive API docs.

## Future Improvements
- Reporting/insights (status breakdown, days-since-applied tracking)
- Deploy database to AWS RDS