from pydantic import BaseModel,Field

class TaskCreate(BaseModel):
    title: str | None = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")

class TaskBase(BaseModel):
    """
    Task 스키마의 공통 속성을 정의하는 기본 클래스

    :param title: 할 일의 제목
    """
    title: str | None = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")

class TaskCreate(TaskBase):
    """
    Task 생성 요청에 사용되는 스키마
    """
    pass

class Task(TaskBase):
    """
    Task 조회 응답에 사용되는 스키마

    :param id: Task의 고유 ID
    :param done: 완료 여부 (True: 완료, False: 미완료)
    """
    id: int
    done: bool = Field(False, description="완료 플래그")

    class Config:
        orm_mode = True

class TaskCreateResponse(TaskCreate):
    """
    Task 생성 응답에 사용되는 스키마

    :param id: 생성된 Task의 고유 ID
    """
    id: int

    class Config:
        orm_mode = True