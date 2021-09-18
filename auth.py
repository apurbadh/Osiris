import jwt
from fastapi import HTTPException, Security,Path
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'secret_go_brr'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def encode_token(self, user_id):
        payload = {
            "exp" : datetime.utcnow() + timedelta(days=7),
            "iat" : datetime.utcnow(),
            "sub" : user_id
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload
        except:
         	raise HTTPException(status_code=401, detail="Invalid Token")

    def auth_wrapper(self, auth : HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

