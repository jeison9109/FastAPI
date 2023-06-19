from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'Mi aplicacion FASTAPI'  
@app.get('/', tags=['Home'])


def message():
 
    return HTMLResponse("<h1>Esta es la pagina principal</h1>")