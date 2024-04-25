from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.users_routes import users_router
from src.routes.artists_routes import artists_router
from src.models.artists_models import Base as artists_models_base
from src.models.users_models import Base as users_models_base
from database.connection import engine

artists_models_base.metadata.create_all(bind=engine)
users_models_base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(artists_router)
app.include_router(users_router)

origins = [ '*' ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)