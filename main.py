from sqlalchemy.sql.functions import user
from models import User, Doctor, Base
from fastapi import FastAPI, Depends,Path
from passlib.hash import bcrypt
from machinelearning import prediction
from db import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
from auth import AuthHandler


Base.metadata.create_all(bind=engine)
localSession = Session(bind=engine)

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

@app.get("/api/predict")
async def get_prediction(data: str):
    data = data.split(",")
    ans = prediction(data) 
    return {"prediction" : ans}


@app.post("/api/register")
async def register_user(name: str, username:str, email:str, password:str):
    hashed_password =  bcrypt.hash(password)
    user = User(name, username, email, hashed_password)
    try:
        localSession.add(user)
        localSession.commit()
    except IntegrityError:
        return {"message" : "Username or email already exists"}
    return {"message" : "Successfully registered"}


@app.post("/api/login")
async def login_user(username: str, password:str):
    found_user = localSession.query(User).filter(User.username == username).first()
    if not found_user:
        return {"message" : "Username does not exist"}
    elif not bcrypt.verify(password, found_user.hashed_password):
        return {"message" : "Password does not match"}
    token = auth_handler.encode_token(found_user["username"])
    return {"message" : "Successfully logged in", "token" : token}     


@app.get("/api/doctor")
async def get_doctors(page : int, username=Depends(auth_handler.auth_wrapper)):
    latest_data = localSession.query(Doctor).all()[(page - 1) * 10 : page * 10]
    return latest_data


@app.get("/api/doctor/{doctor_id}")
async def get_doctor_by_id(doctor_id : int = Path(None, description="Get individual users information", gt=0), username=Depends(auth_handler.auth_wrapper)):
    data = localSession.query(Doctor).get(doctor_id)
    return data

