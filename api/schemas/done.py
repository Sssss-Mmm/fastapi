from pydantic import BaseModel

class DoneCreateResponse(BaseModel):
    """
    완료(Done) 생성 응답에 사용되는 스키마

    :param id: 생성된 완료 기록의 ID (Task ID와 동일)
    """
    id: int

    class Config:
        orm_mode = True