import uuid
from fastapi import Response, status
from sqlalchemy import and_
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from src.models.user_model import UserAccountMaster
from src.schemas.user_schema import UserAuthenticationSchema, UserSignUpSchema
from security.hashing import HashingAlgorithm
from security.jwt import create_access_token

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

    
    async def authenticate_user(self,request_body: UserAuthenticationSchema,response: Response,db: Session) -> dict:
        try:
            encrypted_password = HashingAlgorithm().sha256_encoder(request_body.password)
            user = db.query(UserAccountMaster).filter(UserAccountMaster.username == request_body.username).first()
    
            if not user: 
                raise Exception('Invalid username provided')

            if user.password == encrypted_password:
                user_id = user.user_id
                username = user.username
                email = user.email_id
                access_token = create_access_token({ 'user_id': user_id})
                response_json = { 'message': 'Authentication successful', 
                                'user_details': { 
                                    'username': username, 
                                    'email': email 
                                    }, 
                                'access_token': access_token, 
                                'token_type': 'bearer', 
                                'status_code': status.HTTP_200_OK 
                                }
                response.status_code = status.HTTP_200_OK
                return response_json
            else:
                raise Exception('Invalid password provided')
        except Exception as e:
            response_json = { 'message': str(e), 'status_code': status.HTTP_401_UNAUTHORIZED }
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return response_json