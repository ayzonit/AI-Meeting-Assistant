from sqlalchemy.orm import Session
from app.services.llmservice import generate_summary
from app.services.summaryservice import save_summary
from app.utils.parser import parse_output
from app.models.meeting import Meeting

def process_meeting(db: Session, meeting_id: int):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        return

    output = generate_summary(meeting.transcript)
    parsed = parse_output(output)

    save_summary(db, meeting_id, parsed["summary"], parsed["actions"])

    meeting.status = "completed"
    db.commit()