from fastapi import FastAPI
from app.api import meetings, summaries, health
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health.router, prefix="/health")
app.include_router(meetings.router, prefix="/meetings")
app.include_router(summaries.router, prefix="/summaries")   