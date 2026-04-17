from pydantic import BaseModel
from datetime import datetime

class MeetingCreate(BaseModel):
    title: str | None = None
    transcript: str

class MeetingOut(BaseModel):
    id: int
    title: str | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True