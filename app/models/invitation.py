from sqlalchemy import Column, Integer, String
from app.database import Base

class Invitation(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, nullable=False)
    bride_name = Column(String, nullable=False)
    groom_name = Column(String, nullable=False)
    type = Column(String, nullable=False)
