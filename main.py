#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from machinelearning import prediction

app = FastAPI()

@app.get("/api/predict")
async def get_prediction(data: str):
    data = data.split(",")
    ans = prediction(data) 
    return {"prediction" : ans}
