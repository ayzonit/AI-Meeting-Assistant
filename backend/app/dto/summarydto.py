from pydantic import BaseModel

class SummaryOut(BaseModel):
    content: str

    class Config:
        from_attributes = True