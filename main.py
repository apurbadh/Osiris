from sqlalchemy.sql.functions import user
import models
from models import User, Doctor

from fastapi import FastAPI
from passlib.hash import bcrypt
from machinelearning import prediction
from db import SessionLocal, engine
from  sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


models.Base.metadata.create_all(bind=engine)

localSession = Session(bind=engine)

app = FastAPI()


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

    return {"message" : "Successfully logged in"}     


@app.get("/api/doctor")
async def get_doctors(page : int):
    latest_data = localSession.query(Doctor).all()[(page - 1) * 10 : page * 10]
    return latest_data


@app.get("/api/doctor/{doctor_id}")
async def get_doctor_by_id(doctor_id : int = Path(None, description="Get individual users information", gt=0)):
    data = localSession.query(Doctor).get(doctor_id)
    return data

