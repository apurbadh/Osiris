
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime


Base = declarative_base()
engine = create_engine('sqlite:///doctor.db',echo=True)
Session = sessionmaker()

class Doctor(Base):
	__tablename__ = 'docta'
	id = Column(Integer(),primary_key=True,nullable=False)
	name = Column(String(128),nullable=False)
	qualificaion = Column(String(128),nullable=False)
	speciality = Column(String(258),nullable=False)
	contact_email = Column(String(128),nullable=False)
	contact_number = Column(Integer(),nullable=False)
	date_joined = Column(DateTime(),default=datetime.utcnow())


	def __repr__(self):
		return f"<User id= {self.id} name={self.name} qualificaion={self.qualificaion} speciality={self.speciality} contact={self.contact_email}{self.contact_number} date_joined={self.date_joined}>"





