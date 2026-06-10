from fastapi import APIRouter
from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.invitation import Invitation
from app.schemas.invitation import InvitationResponse

router = APIRouter(
    prefix="/api/invitations",
    tags=["invitations"],
)

@router.get("/{slug}", response_model=InvitationResponse)
def get_invitation(
        slug: str,
        db: Session = Depends(get_db),
):
    invitation = (
        db.query(Invitation)
        .filter(Invitation.slug == slug)
        .first()
    )
    if not invitation:
        raise HTTPException(status_code=404, detail="Invitation not found")
    return invitation