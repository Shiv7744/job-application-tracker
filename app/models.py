from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    location = Column(String(100), nullable=True)
    status = Column(String(30), nullable=False, default="Applied")
    date_applied = Column(Date, nullable=False)
    link = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)