from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.invitation import Invitation
from app.routers.invitations import router as invitations_router

import os


app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://www.invitamx.lat",
    "https://invitamx.lat",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(invitations_router)

Base.metadata.create_all(bind=engine)