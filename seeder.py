from main import Doctor,Session,engine


class SeedingRandomData:
    def __init__(self):
        self.localsession = Session(bind=engine)
        


    def main(self,name,qualificaion,speciality,contact_email,contact_number):
        new_user = Doctor(name=name,qualificaion=qualificaion,speciality=speciality,contact_email=contact_email,contact_number=contact_number)
        self.localsession.add(new_user)
        self.localsession.commit()


newObj = SeedingRandomData()
newObj.main(name=[],qualificaion=[],speciality=[],contact_email=[],contact_number=[])