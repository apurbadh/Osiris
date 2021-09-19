from sqlalchemy import Boolean, Column, Integer, String

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

