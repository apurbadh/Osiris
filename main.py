from datetime import datetime
from sqlalchemy.sql.functions import user
from starlette.responses import RedirectResponse
from models import User, Doctor, Base, Messages
from fastapi import FastAPI, Depends,Path, Response
from passlib.hash import bcrypt
from machinelearning import prediction
from db import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
from auth import AuthHandler, SessionData, SessionHandler
from uuid import uuid4
from uuid import UUID
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi import HTTPException

cookie_params = CookieParameters()

# Uses UUID
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

backend = InMemoryBackend[UUID, SessionData]()

Base.metadata.create_all(bind=engine)
from pydantic import BaseModel

verifier = SessionHandler(identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),)

app = FastAPI()
auth_handler = AuthHandler()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/predict",dependencies=[Depends(cookie)])
async def get_prediction(data: str, session_data: SessionData = Depends(verifier)):
    data = data.split(",")
    ans = prediction(data) 
    return {"prediction" : ans}


@app.post("/api/register")
async def register_user(name: str, username:str, email:str, password:str):
    localSession = Session(bind=engine)
    hashed_password =  bcrypt.hash(password)
    user = User(name, username, email, hashed_password)
    try:
        localSession.add(user)
        localSession.commit()
    except IntegrityError:
        return {"message" : "Username or email already exists"}
    return {"message" : "Successfully registered"}


@app.post("/api/login")
async def login_user(username: str, password:str, response : Response):
    localSession = Session(bind=engine)
    found_user = localSession.query(User).filter(User.username == username).first()
    if not found_user:
        return {"message" : "Username does not exist"}
    elif not bcrypt.verify(password, found_user.hashed_password):
        return {"message" : "Password does not match"}
    token = auth_handler.encode_token(found_user.username)
    session = uuid4()
    data = SessionData(username=username)
    await backend.create(session, data)
    cookie.attach_to_response(response, session)
    return {"message" : "Successfully logged in", "token" : token}     

@app.post("/api/login/doctor")
async def register_doctor(username : str, qualification : str, speciality:str, contact_email:str, contact_number:int):
    localSession  = Session(bind=engine)
    doctor = Doctor(username, qualification, speciality, contact_email, contact_number) 
    localSession.add(doctor)
    localSession.commit()
    # valid_doctor = localSession.query(Doctor).filter(Doctor.accepted == 0).first()

<<<<<<< HEAD
@app.get("/api/doctor")
async def get_doctors(page : int, username=Depends(auth_handler.auth_wrapper),):
=======
@app.get("/api/doctor", dependencies=[Depends(cookie)], )
async def get_doctors(page : int, session_data: SessionData = Depends(verifier)):
>>>>>>> fdbab994815050857ad05f959c9c5e521b63d4f5
    localSession = Session(bind=engine)
    latest_data = localSession.query(Doctor).all()[(page - 1) * 10 : page * 10]
    

@app.get("/api/doctor/{doctor_id}", dependencies=[Depends(cookie)])
async def get_doctor_by_id(doctor_id : int = Path(None, description="Get individual users information", gt=0), session_data: SessionData = Depends(verifier)):
    localSession = Session(bind=engine)
    data = localSession.query(Doctor).get(doctor_id)
    return data

<<<<<<< HEAD
# @app.get("/api/adminpanel/{doctor_id}")
# async def check(doctor_id: int,  accepted:Doctor):
#    localSession = Session(bind=engine)
#    accept = accepted(doctor_id)
#    if accept:
#        return localSession.query(Doctor).filter(Doctor.accepted == 1)
#    elif not accept:
#        return Doctor.doctors({doctor_id}).remove()
        
    
                


@app.post('/api/chat/send')
async def send_message(sender : int, reciever : int, message : str):
=======
@app.post('/api/chat/send',dependencies=[Depends(cookie)])
async def send_message(sender : int, message : str, session_data: SessionData = Depends(verifier)):
>>>>>>> fdbab994815050857ad05f959c9c5e521b63d4f5
    localSession = Session(bind=engine)
    reciever = localSession.query(User).filter(User.username == session_data.user).first().id
    message = Messages(sender, reciever, message)
    localSession.add(message)
    localSession.commit()


@app.get("/api/chat/{sender}/", dependencies=[Depends(cookie)])
async def get_chat(sender : int, session_data: SessionData = Depends(verifier)):
    localSession = Session(bind=engine)
    reciever = localSession.query(User).filter(User.username == session_data.user).first().id
    message = localSession.query(Messages).filter(Messages.sender == sender)
    message = message.filter(Messages.reciever == reciever)
    return message
