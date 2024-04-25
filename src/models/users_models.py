from sqlalchemy import Boolean, Column, String, DateTime
from database.connection import Base

class UserAccountMaster(Base):
    
    __tablename__ = 'user_account_master'
    __table_args__ = { 'extend_existing': True }

    user_id = Column(String(100),primary_key=True,nullable=False)
    username = Column(String(100),nullable=False)
    password = Column(String(100),nullable=False)
    email_id = Column(String(250),nullable=False)
    created_on = Column(DateTime,nullable=False)
    is_active = Column(Boolean,nullable=False)


