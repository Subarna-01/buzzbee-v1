from sqlalchemy import Integer, Column, String
from database.connection import Base

class CategorySongs(Base):
    
    __tablename__ = 'category_songs'
    __table_args__ = { 'extend_existing': True }

    category_id = Column(String(50),primary_key=True,nullable=False)
    category_name = Column(String(50),nullable=False)
    total_no_of_songs = Column(Integer,nullable=False)
