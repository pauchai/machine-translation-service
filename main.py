import os
from typing import Optional, List
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel


from translate import Translator
from config import *

app = FastAPI()
translator = Translator(MODEL_PATH)


class LangItem(BaseModel):
    source: str
    target: str
    text: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/lang_routes")
def get_lang_route(lang: str = 'ru'):
    all_langs = translator.get_supported_langs()
    lang_routes = [l for l in all_langs if l[0] == lang]
    return {"output": lang_routes}


@app.get("/supported_languages")
def get_supported_languages():
    langs = translator.get_supported_langs()
    return {"output": langs}


@app.post('/translate')
def get_prediction(item: LangItem):
    source = item.source
    target = item.target
    text = item.text
    translation = translator.translate(source, target, text)
    return {"output": translation}
