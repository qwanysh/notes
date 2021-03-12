from fastapi import FastAPI
from app.routes import note_routes

app = FastAPI()

app.include_router(note_routes.router, prefix='/notes')
