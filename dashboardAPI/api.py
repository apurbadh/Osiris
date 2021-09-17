from fastapi import FastAPI,Path
from typing import Optional
from dash import Doctor,Session,engine

api_session = Session(bind=engine)




app = FastAPI()




@app.get('/data')
def return_data(q:int):
	latest_data = api_session.query(Doctor).all()[0:q]
	return latest_data

@app.get('/user/{user_id}')
def individual_user(user_id:int = Path(None,description="Get individual users information",gt=0)):
	data = api_session.query(Doctor).get(user_id)
	return data
