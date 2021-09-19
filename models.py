from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String,)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    def __init__(self, name, username, email, hashed_password):
        self.name = name
        self.username = username
        self.email  = email
        self.hashed_password = hashed_password


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer(),primary_key=True,nullable=False)
    username = Column(String(128),) 
    qualificaion = Column(String(128),nullable=False)
    speciality = Column(String(258),nullable=False)
    contact_email = Column(String(128),nullable=False)
    contact_number = Column(Integer(),nullable=False)
    date_joined = Column(DateTime(),default=datetime.utcnow())


    def __init__(self, user_id, qualificaion, speciality,contact_email, contact_number):
        self.user_id = user_id
        self.qualificaion = qualificaion
        self.speciality = speciality
        self.contact_number = contact_number
        self.contact_email = contact_email

    def __repr__(self):
        return f"<User id= {self.id} name={self.name} qualificaion={self.qualificaion} speciality={self.speciality} contact={self.contact_email}{self.contact_number} date_joined={self.date_joined}>"

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer(),primary_key=True,nullable=False)
    sender = Column(Integer(),)
    reciever = Column(Integer())
    message = Column(String(10000))

    def __init__(self, sender, reciever, message):
        self.sender = sender
        self.reciever = reciever
        self.message = message



    
