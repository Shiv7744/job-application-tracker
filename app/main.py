from fastapi import FastAPI
from app.database import SessionLocal
from app.models import Application
from pydantic import BaseModel
from datetime import date
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

# This creates the app
app = FastAPI()

# This lets the webpage talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# What's needed to add a new application
class ApplicationCreate(BaseModel):
    company: str
    role: str
    location: Optional[str] = None
    status: Optional[str] = "Applied"
    date_applied: date
    link: Optional[str] = None
    notes: Optional[str] = None

# What's allowed when updating an application (everything optional)
class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    date_applied: Optional[date] = None
    link: Optional[str] = None
    notes: Optional[str] = None

# Get all applications
@app.get("/applications")
def get_applications():
    db = SessionLocal()               # connect to the database
    applications = db.query(Application).all()  # get every row
    db.close()                         # disconnect
    return applications                # send the data back

# Add a new application
@app.post("/applications")
def create_application(app_data: ApplicationCreate):
    db = SessionLocal()
    new_app = Application(**app_data.dict())  # build a new row
    db.add(new_app)      # queue it up
    db.commit()            # save it
    db.refresh(new_app)     # get the new id
    db.close()
    return new_app

# Update one application by id
@app.put("/applications/{application_id}")
def update_application(application_id: int, app_data: ApplicationUpdate):
    db = SessionLocal()
    application = db.query(Application).filter(Application.id == application_id).first()  # find it

    if application is None:
        db.close()
        return {"error": "Application not found"}

    update_data = app_data.dict(exclude_unset=True)  # only what was actually sent
    for key, value in update_data.items():
        setattr(application, key, value)   # change those fields

    db.commit()
    db.refresh(application)
    db.close()
    return application

# Delete one application by id
@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    db = SessionLocal()
    application = db.query(Application).filter(Application.id == application_id).first()  # find it

    if application is None:
        db.close()
        return {"error": "Application not found"}

    db.delete(application)  # remove it
    db.commit()
    db.close()
    return {"message": f"Application {application_id} deleted"}