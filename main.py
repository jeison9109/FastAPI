from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from jwt_manager import create_token
=======
from fastapi.responses import HTMLResponse
>>>>>>> ea78abf818fb8e6811e0a5fafb85b9231627f78f

app = FastAPI()
app.title = 'Mi aplicacion FASTAPI'  
@app.get('/', tags=['Home'])

<<<<<<< HEAD
# Modelo de usuario ##
class User(BaseModel):
    email : str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating:float = Field(default=10, ge=1, le=10)
    category:str = Field(default='Categoría', min_length=5, max_length=15)
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }
        }

movies = [
    {
		"id": 1,
		"title": "Terminator",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": 2009,
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": 2009,
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags = ['home'])

def message():
    return "Hello, world!"

###  Login user ####
@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admi":
        token : str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@app.get('/movies', tags = ['movies'], status_code=200)
def get_movies():
    return JSONResponse(status_code=200,content=movies)

@app.get('/movies/{id}', tags = ['movies'], status_code=200)
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(content=[])

@app.post('/movies', tags=['movies'],response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"messages":"Se ha creado la pelicula"})
=======

def message():
 
    return HTMLResponse("<h1>Esta es la pagina principal</h1>")
>>>>>>> ea78abf818fb8e6811e0a5fafb85b9231627f78f
