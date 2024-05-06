from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database.connection import get_db
from src.schemas.song_schema import CreatePlayListSchema
from src.controllers.song_controller import SongController
from security.jwt import get_current_user

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
async def get_songs_by_random_artist(category: str,response: Response,db: Session = Depends(get_db),user_id: str = Depends(get_current_user)):
    response = await SongController().get_songs_by_random_artist(category,response,db)
    return jsonable_encoder(response)

# @song_router.post('/create-playlist')
# async def create_playlist(request_body: CreatePlayListSchema,response: Response):
#     response = await SongController.create_playlist(request_body,response)
#     return 'Playlist has been created'