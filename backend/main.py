
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="StreamFlix API",
    description="Backend API for the StreamFlix streaming platform",
    version="1.0.0"
)

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    resolution: str


movies = [
    Movie(
        id=1,
        title="Inception",
        genre="Sci-Fi",
        resolution="1080p"
    ),
    Movie(
        id=2,
        title="The Dark Knight",
        genre="Action",
        resolution="720p"
    ),
    Movie(
        id=3,
        title="Interstellar",
        genre="Sci-Fi",
        resolution="480p"
    )
]



@app.get("/")
def home():
    return {
        "message": "Welcome to StreamFlix!",
        "status": "API is running"
    }

@app.get("/movies", response_model=list[Movie])
def get_movies(genre: str | None = None):
    if genre:
        return [
            movie for movie in movies
            if movie.genre.lower() == genre.lower()
        ]

    return movies

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )
