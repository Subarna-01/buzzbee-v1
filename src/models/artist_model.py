from sqlalchemy import Integer, Column, String
from database.connection import Base

class ArtistAccountMaster(Base):
    
    __tablename__ = 'artist_account_master'
    __table_args__ = { 'extend_existing': True }

    artist_id = Column(String(50),primary_key=True,nullable=False)
    user_id = Column(String(50))
    stage_name = Column(String(100),nullable=False)
    in_categories = Column(String(250),nullable=False)
    in_genres = Column(String(250),nullable=False)