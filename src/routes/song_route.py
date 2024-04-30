from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database.connection import get_db
from src.controllers.song_controller import SongController

song_router = APIRouter(prefix='/songs')

@song_router.get('/get-categories')
async def get_categories(response: Response,db: Session = Depends(get_db)):
    response = await SongController().get_song_categories(response,db)
    return jsonable_encoder(response)

@song_router.get('/get-songs/{category}/')
async def get_songs_by_category(category: str,response: Response,offset: int = 0,limit: int = 3,db: Session = Depends(get_db)):
    category = category.capitalize()
    response = await SongController().get_songs_by_category(category,response,offset,limit,db)
    return jsonable_encoder(response)

@song_router.get('/get-songs-by-random-artist/{category}')
async def get_songs_by_random_artist(category: str,response: Response,db: Session = Depends(get_db)):
    response = await SongController().get_songs_by_random_artist(category,response,db)
    return jsonable_encoder(response)