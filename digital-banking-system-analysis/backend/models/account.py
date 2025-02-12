from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from database import Base

class Account(Base):
    __tablename__ = 'Accounts'

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    account_number = Column(String, unique=True, nullable=False)
    account_type = Column(String, nullable=False)
    balance = Column(DECIMAL(12,2), default=0)
