import uuid
from fastapi import Response, status
from sqlalchemy import and_
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from src.models.user_model import UserAccountMaster
from src.schemas.user_schema import UserSignInSchema, UserSignUpSchema
from security.hashing import HashingAlgorithm

class UserController():

    def __init__(self):
            pass
    
    async def create_user(self,request_body: UserSignUpSchema,response: Response,db: Session) -> dict:
        try:
            user_id = str(uuid.uuid1())
            username = request_body.username
            encrypted_password = HashingAlgorithm().sha256_encoder(request_body.password)
            email_id = request_body.email_id
            created_on = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

            is_active_with_email_exists = db.query(UserAccountMaster).filter(and_(UserAccountMaster.email_id==request_body.email_id,UserAccountMaster.is_active==True))
            
            if is_active_with_email_exists: raise Exception('This email already exists')
            
            new_user = UserAccountMaster(user_id=user_id,
                                         username=username,
                                         password=encrypted_password,
                                         email_id=email_id,
                                         created_on=created_on,
                                         is_active=True
                                        )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            response_json = { 'message': 'User has been created', 'is_created': 'Success', 'status_code': status.HTTP_201_CREATED }
            response.status_code = status.HTTP_201_CREATED
            return response_json
        except Exception as e:
            response_json = { 'message': 'An error occurred', 'error': str(e),'is_created': 'Failure','status_code': status.HTTP_400_BAD_REQUEST }
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response_json

    
    async def authenticate_user(self,request_body: UserSignInSchema,response: Response,db: Session) -> dict:
        try:
            encrypted_password = HashingAlgorithm().sha256_encoder(request_body.password)
            is_user_exists = db.query(UserAccountMaster).filter(and_(UserAccountMaster.username == request_body.username,
                                                                     UserAccountMaster.password == encrypted_password
                                                                )).first()
            if is_user_exists:
                response.status_code = status.HTTP_200_OK
                response_json = { 'message': 'Signed in', 'sign_in_status': 'Success', 'status_code': status.HTTP_200_OK }
                return response_json
            else:
                raise Exception('User does not exist')
        except Exception as e:
            response_json = { 'message': 'An error occurred', 'error': str(e),'sign_in_status': 'Failure','status_code': status.HTTP_401_UNAUTHORIZED }
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return response_json