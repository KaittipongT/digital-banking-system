from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'Users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    address = Column(String)
    password_hash = Column(String, nullable=False)
