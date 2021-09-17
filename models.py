from sqlalchemy import Boolean, Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String,)
    username = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
