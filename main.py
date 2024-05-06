from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.user_route import user_router
from src.routes.song_route import song_router
from src.models.user_model import Base as user_model_base
from src.models.song_model import Base as song_model_base
from src.models.artist_model import Base as artist_model_base
from database.connection import engine


user_model_base.metadata.create_all(bind=engine)
song_model_base.metadata.create_all(bind=engine)
artist_model_base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(song_router)

origins = [ '*' ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.on_event('startup')
async def startup_event():
    pass

