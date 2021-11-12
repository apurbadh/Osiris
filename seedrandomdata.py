from main import Doctor,Session,engine
from datetime import datetime

class SeedingRandomData:
	def __init__(self):
		self.localsession = Session(bind=engine)
		


	def main(self,user_id,qualificaion,speciality,contact_email,contact_number,date_joined):
		new_user = Doctor(user_id=user_id,qualificaion=qualificaion,speciality=speciality,contact_email=contact_email,contact_number=contact_number,date_joined=date_joined)
		self.localsession.add(new_user)
		self.localsession.commit()


newObj = SeedingRandomData()
newObj.main(user_id=12,qualificaion="Masters Complete",speciality="Foot",contact_email='jack@gmail.com',contact_number=9844383924,date_joined=datetime.now())


