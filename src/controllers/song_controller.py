from fastapi import Response, status
from sqlalchemy.orm import Session
from src.models.song_model import CategorySongs, MasterSongs
from config.firebase_config import FirebaseConfig

class SongController():
    
    def __init__(self):
        self.firebase_config_obj = FirebaseConfig()

    async def get_song_categories(self,response: Response,db: Session) -> dict:
        all_categories = db.query(CategorySongs).all()
        return all_categories
    
    async def get_songs_by_category(self,category: str,response: Response,db: Session) -> dict:
        try:
            songs = []
            all_songs = db.query(
                            CategorySongs.category_id,
                            CategorySongs.category_name,
                            MasterSongs.song_id,
                            MasterSongs.song_name,
                            MasterSongs.artists,
                            MasterSongs.firebase_audio_file_path,
                            MasterSongs.firebase_cover_img_file_path
                        ).join(
                            MasterSongs,
                            CategorySongs.category_id == MasterSongs.category_id
                        ).filter(
                            CategorySongs.category_name == category
                        ).all()
            
            for song in all_songs:
                audio_download_url = self.firebase_config_obj.get_file_download_url(song[5])
                cover_image_download_url = self.firebase_config_obj.get_file_download_url(song[6])
                song_obj = { 
                            'category_id': song[0],
                            'category_name': song[1],
                            'song_id': song[2],
                            'song_name': song[3],
                            'artists': song[4],
                            'audio_download_url': audio_download_url,
                            'cover_image_download_url': cover_image_download_url
                        }
                songs.append(song_obj)
            
            songs_count_fetch_message = f'{len(songs)} songs fetched' if len(songs) > 1 else f'{len(songs)} song fetched'
            response_json = { 'message': songs_count_fetch_message, 'songs': songs, 'status_code': status.HTTP_200_OK }
            response.status_code = status.HTTP_200_OK
            return response_json
        except Exception as e:
            response_json = { 'message': 'An error occurred', 'error': str(e),'status_code': status.HTTP_400_BAD_REQUEST }
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response_json

