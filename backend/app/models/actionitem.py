from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.db import Base

class ActionItem(Base):
    __tablename__ = "action_items"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"))
    description = Column(String)
    owner = Column(String, nullable=True)