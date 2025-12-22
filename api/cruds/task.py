from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    """
    새로운 할 일을 생성합니다.

    :param db: 데이터베이스 세션
    :param task_create: 생성할 할 일 정보가 담긴 스키마
    :return: 생성된 할 일 모델 객체
    """
    task = task_model.Task(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
def get_tasks_with_done(db: Session) -> list[tuple[int,str,bool]]:
    """
    모든 할 일을 완료 여부와 함께 조회합니다.

    :param db: 데이터베이스 세션
    :return: (Task ID, 제목, 완료 여부) 튜플의 리스트
    """
    result:Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done")
        ).outerjoin(task_model.Done)
    )

    return result.all()

def get_task(db:Session,task_id:int)->task_model.Task | None:
    """
    지정된 ID의 할 일을 조회합니다.

    :param db: 데이터베이스 세션
    :param task_id: 조회할 할 일의 ID
    :return: 조회된 할 일 모델 객체 또는 None
    """
    result:Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    return result.scalars().first()

def update_task(db:Session, task_create: task_schema.TaskCreate,original:task_model.Task) -> task_model.Task:
    """
    기존 할 일의 정보를 수정합니다.

    :param db: 데이터베이스 세션
    :param task_create: 수정할 할 일 정보가 담긴 스키마
    :param original: 수정 대상인 원본 할 일 모델 객체
    :return: 수정된 할 일 모델 객체
    """
    original.title = task_create.title
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def delete_task(db:Session,original:task_model.Task)->None:
    """
    할 일을 삭제합니다.

    :param db: 데이터베이스 세션
    :param original: 삭제할 할 일 모델 객체
    """
    db.delete(original)
    db.commit()