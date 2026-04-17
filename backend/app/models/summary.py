from sqlalchemy import Column, Integer, Text, ForeignKey
from app.core.db import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"))
    content = Column(Text)