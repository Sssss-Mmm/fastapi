from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from api.db import Base

class Task(Base):
    """
    할 일(Task)을 나타내는 데이터베이스 모델

    :param id: Task의 고유 ID (PK)
    :param title: 할 일의 제목
    :param done: 완료 여부 관계 설정
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    done = relationship("Done", back_populates="task",cascade="delete")

class Done(Base):
    """
    완료된 할 일(Done)을 나타내는 데이터베이스 모델

    :param id: Task의 고유 ID (PK, FK)
    :param task: 할 일(Task)과의 관계 설정
    """
    __tablename__ = "done"
    
    id = Column(Integer, ForeignKey("tasks.id"),primary_key=True)

    task = relationship("Task", back_populates="done")
    
