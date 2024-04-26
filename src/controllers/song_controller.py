from fastapi import Response
from sqlalchemy.orm import Session
from src.models.song_model import CategorySongs

class SongController():
    
    async def get_song_categories(self,response: Response,db: Session) -> dict:
        all_categories = db.query(CategorySongs).all()
        return all_categories