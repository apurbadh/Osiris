#!/usr/bin/env python
# -*- coding: utf-8 -*-

import models

from fastapi import FastAPI
from machinelearning import prediction
from db import SessionLocal, engine
from  sqlalchemy.orm import Session




models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/api/predict")
async def get_prediction(data: str):
    data = data.split(",")
    ans = prediction(data) 
    return {"prediction" : ans}


