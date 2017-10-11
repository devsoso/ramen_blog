from contextlib import contextmanager
from app import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@contextmanager
def get_session():
    Session = sessionmaker(bind=db.engine)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


