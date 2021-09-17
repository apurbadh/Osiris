#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

@app.get('/api/user')
def getUser():
    return {"aps" : "jjj"}


