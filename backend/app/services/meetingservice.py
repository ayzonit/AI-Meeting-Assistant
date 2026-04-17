from sqlalchemy.orm import Session
from app.models.meeting import Meeting

def create_meeting(db: Session, title: str, transcript: str):
    meeting = Meeting(title=title, transcript=transcript)
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    return meeting

def get_meetings(db: Session):
    return db.query(Meeting).order_by(Meeting.created_at.desc()).all()

def get_meeting(db: Session, meeting_id: int):
    return db.query(Meeting).filter(Meeting.id == meeting_id).first()