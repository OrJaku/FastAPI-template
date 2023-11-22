from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from configuration import conf

engine = create_engine(
    f"postgresql://{conf.postgres_user}:{conf.postgres_password}@{conf.postgres_host}:{conf.postgres_port}/{conf.postgres_db_name}")

def get_db_session() -> Session:
    return sessionmaker(
        bind=engine,  
        autoflush=False,
        autocommit=False
        )()

def get_db() -> Generator:
    db = get_db_session()
    try:
        yield db
    except: 
        db.rollback()
    finally:
        db.close()

def get_db_script() -> Session:
    db = get_db_session()
    try:
        return db
    except: 
        db.rollback()
    finally:
        db.close()