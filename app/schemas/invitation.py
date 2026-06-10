from pydantic import BaseModel

class InvitationResponse(BaseModel):
    slug: str
    bride_name: str
    groom_name: str
    type: str

    class Config:
        from_attributes=True