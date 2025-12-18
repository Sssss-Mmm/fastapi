from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

DB_URL = "mysql+pymysql://root:root@localhost:3306/todo"

db_engine = create_engine(DB_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session