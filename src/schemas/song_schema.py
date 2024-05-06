from pydantic import BaseModel, validator
from typing import Optional

class CreatePlayListSchema(BaseModel):
    playlist_name: str
    cover_image_base64_str: str = None

    @validator('playlist_name')
    def validate_playlist_name(cls,value):
        if len(value) > 50:
            raise ValueError('Playlist name can not exceed more than 50 characters')
        elif len(value) < 1:
            raise ValueError('Playlist name can not be empty')
        return value