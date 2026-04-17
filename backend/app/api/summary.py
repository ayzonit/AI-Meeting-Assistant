from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.summary import Summary
from app.models.actionitem import ActionItem

router = APIRouter()

@router.get("/{meeting_id}")
def get_summary(meeting_id: int, db: Session = Depends(get_db)):
    summary = db.query(Summary).filter(Summary.meeting_id == meeting_id).first()
    actions = db.query(ActionItem).filter(ActionItem.meeting_id == meeting_id).all()

    return {
        "summary": summary.content if summary else "",
        "action_items": actions
    }