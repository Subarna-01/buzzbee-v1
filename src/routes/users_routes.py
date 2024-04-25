from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database.connection import get_db
from src.controllers.users_controllers import UsersController
from src.schemas.users_schemas import UserSignInSchema, UserSignUpSchema

users_router = APIRouter(prefix='/users')

@users_router.post('/sign-up')
async def user_sign_up(request_body: UserSignUpSchema,response: Response,db: Session = Depends(get_db)):
    response = await UsersController().create_user(request_body,response,db)
    return jsonable_encoder(response)

@users_router.post('/sign-in')
async def user_sign_in(request_body: UserSignInSchema,response: Response,db: Session = Depends(get_db)):
    response = await UsersController().authenticate_user(request_body,response,db)
    return jsonable_encoder(response)