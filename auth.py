import jwt
from fastapi import HTTPException, Security,Path
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.backends.implementations import InMemoryBackend
from uuid import UUID
from pydantic import BaseModel

class SessionData(BaseModel):
    username: str


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


class SessionHandler(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True

