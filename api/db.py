from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

import os

# Docker 내부에서는 'db:3306', 로컬 직접 실행 시에는 'localhost:3307' 사용
DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@localhost:3307/todo")

db_engine = create_engine(DB_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session