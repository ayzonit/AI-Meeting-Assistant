from sqlalchemy.orm import Session
from app.models.summary import Summary
from app.models.actionitem import ActionItem

def save_summary(db: Session, meeting_id: int, summary_text: str, actions: list):
    summary = Summary(meeting_id=meeting_id, content=summary_text)
    db.add(summary)

    for a in actions:
        item = ActionItem(
            meeting_id=meeting_id,
            description=a["task"],
            owner=a.get("owner")
        )
        db.add(item)

    db.commit()