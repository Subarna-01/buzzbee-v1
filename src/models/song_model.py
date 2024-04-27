from sqlalchemy import Integer, Column, String
from database.connection import Base

class CategorySongs(Base):
    
    __tablename__ = 'category_songs'
    __table_args__ = { 'extend_existing': True }

    category_id = Column(String(50),primary_key=True,nullable=False)
    category_name = Column(String(50),nullable=False)
    total_songs = Column(Integer,nullable=False)

class MasterSongs(Base):

    __tablename__ = 'master_songs'
    __table_args__ = { 'extend_existing': True }

    song_id = Column(String(50),primary_key=True,nullable=False)
    category_id = Column(String(50),nullable=True)
    song_name = Column(String(100),nullable=False)
    artists = Column(String(250),nullable=False)
    firebase_audio_file_path = Column(String(500),nullable=False)
    firebase_cover_img_file_path = Column(String(500),nullable=False)