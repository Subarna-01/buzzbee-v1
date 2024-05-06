from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database.connection import get_db
from src.controllers.user_controller import UserController
from src.schemas.user_schema import UserAuthenticationSchema, UserSignUpSchema

user_router = APIRouter(prefix='/users')

@user_router.post('/sign-up')
async def user_sign_up(request_body: UserSignUpSchema,response: Response,db: Session = Depends(get_db)):
    response = await UserController().create_user(request_body,response,db)
    return jsonable_encoder(response)

@user_router.post('/sign-in')
async def user_sign_in(request_body: UserAuthenticationSchema,response: Response,db: Session = Depends(get_db)):
    response = await UserController().authenticate_user(request_body,response,db)
    return jsonable_encoder(response)