from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers.invitations import router as invitations_router

from app.core.config import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_urls,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=86400,  # 24 horas
)

app.include_router(invitations_router)

Base.metadata.create_all(bind=engine)