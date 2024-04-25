from sqlalchemy import Boolean, Column, String
from database.connection import Base

class ArtistsMasterRecord(Base):
    
    __tablename__ = 'artists_master_record'
    __table_args__ = { 'extend_existing': True }

    artist_id = Column(String(10),primary_key=True,nullable=False)
    artist_name = Column(String(100),nullable=False)
    in_categories = Column(String(250),nullable=False)
    is_account_active = Column(Boolean,nullable=True)
    gender = Column(String(6),nullable=True)




