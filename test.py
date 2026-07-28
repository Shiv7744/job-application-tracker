from app.database import SessionLocal
from app.models import Application

db = SessionLocal()

applications = db.query(Application).all()

for app in applications:
    print(app.id, app.company, app.role, app.status)

db.close()