from pydantic import BaseModel

class ActionItemOut(BaseModel):
    description: str
    owner: str | None

    class Config:
        from_attributes = True