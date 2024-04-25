from fastapi import APIRouter,Depends,Response
from sqlalchemy.orm import Session
from src.controllers.artists_controller import ArtistsController
from database.connection import get_db

artists_router = APIRouter(prefix='/artists')

@artists_router.get('/get-artists')
async def get_artists_by_category(response: Response,db: Session = Depends(get_db)):
    response = ArtistsController().get_all_artists(response,db)
    return response

@artists_router.get('/get-artists/{category}')
async def get_artists_by_category(category: str,db: Session = Depends(get_db)):
    response = ArtistsController().get_all_artists_by_category(category,db)
    return response

@artists_router.get('/get-artists/{gender}')
async def get_artists_by_gender(gender: str,db: Session = Depends(get_db)):
    response = ArtistsController().get_all_artists_by_gender(gender,db)
    return response

@artists_router.get('/get-artists/{category}/{gender}')
async def get_artists_by_category_and_gender(category: str,gender: str,db: Session = Depends(get_db)):
    response = ArtistsController().get_all_artists_by_category_and_gender(category,gender,db)
    return response