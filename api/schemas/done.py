from pydantic import BaseModel

class DoneCreateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True