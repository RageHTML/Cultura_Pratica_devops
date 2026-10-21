from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def exibir_pagina(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={},
        status_code=200
    )