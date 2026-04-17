from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.dto.meetingdto import MeetingCreate, MeetingOut
from app.services.meetingservice import create_meeting, get_meetings, get_meeting
from app.task.processmeeting import process_meeting

router = APIRouter()

@router.post("/", response_model=MeetingOut)
def create(meeting: MeetingCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    m = create_meeting(db, meeting.title, meeting.transcript)
    background_tasks.add_task(process_meeting, db, m.id)
    return m

@router.get("/", response_model=list[MeetingOut])
def list_all(db: Session = Depends(get_db)):
    return get_meetings(db)

@router.get("/{meeting_id}", response_model=MeetingOut)
def get_one(meeting_id: int, db: Session = Depends(get_db)):
    return get_meeting(db, meeting_id)