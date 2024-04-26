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
