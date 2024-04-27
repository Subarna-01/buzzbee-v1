import pyrebase
import os
from dotenv import load_dotenv
import collections

load_dotenv()

try:
    from collections import abc
    collections.MutableMapping = abc.MutableMapping
except:
    pass

class FirebaseConfig():

    def __init__(self):
        self.firebase_config = {
                'apiKey': os.getenv('API_KEY'),
                'authDomain': os.getenv('AUTH_DOMAIN'),
                'projectId': os.getenv('PROJECT_ID'),
                'storageBucket': os.getenv('STORAGE_BUCKET'),
                'messagingSenderId': os.getenv('MESSAGING_SENDER_ID'),
                'appId': os.getenv('APP_ID'),
                'measurementId': os.getenv('MEASUREMENT_ID'),
                'databaseURL': os.getenv('DATABASE_URL')
            }
        self.firebase_app = pyrebase.initialize_app(self.firebase_config)
        self.firebase_storage = self.firebase_app.storage()
        self.firebase_user = self.firebase_app.auth().sign_in_with_email_and_password(email=os.getenv('USER_EMAIL_ID'),password=os.getenv('USER_EMAIL_PASSWORD'))

    def get_file_download_url(self,firebase_file_path: str) -> str:
        download_url = self.firebase_storage.child(firebase_file_path).get_url(self.firebase_user['idToken'])
        return download_url
