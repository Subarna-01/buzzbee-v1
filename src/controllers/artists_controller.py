from fastapi import status,Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.models.artists_models import ArtistsMasterRecord

class ArtistsController():

    def __init__(self):
        pass    

    def get_all_artists(self,response: Response,db: Session):
        try:
            all_artists = db.query(ArtistsMasterRecord).all()
            response.status_code = status.HTTP_200_OK
            return jsonable_encoder(all_artists)
        except Exception as e:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return jsonable_encoder({ 'error': str(e.args), 'status_code': status.HTTP_400_BAD_REQUEST })
    
    def get_all_artists_by_category(self,category: str,db: Session):
        all_artists = db.query(ArtistsMasterRecord).filter(ArtistsMasterRecord.in_categories == category.lower()).all()
        return all_artists
    
    def get_all_artists_by_gender(self,gender: str,db: Session):
        all_artists = db.query(ArtistsMasterRecord).filter(ArtistsMasterRecord.gender == gender).all()
        return all_artists

    def get_all_artists_by_category_and_gender(self,category: str,gender: str,db: Session):
        all_artists = db.query(ArtistsMasterRecord).filter(and_(ArtistsMasterRecord.in_categories == category.lower(),ArtistsMasterRecord.gender == gender)).all()
        return all_artists