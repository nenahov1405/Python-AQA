import os
import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/testdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


def init_db():
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="module")
def db_session():
    init_db()
    session = SessionLocal()
    yield session
    session.close()


def test_connection(db_session):
    assert db_session is not None


def test_crud_operations(db_session):
    #Create
    new_user = User(name="Ivan")
    db_session.add(new_user)
    db_session.commit()

    #Read
    user = db_session.query(User).filter_by(name="Ivan").first()
    assert user is not None
    assert user.name == "Ivan"

    #Update
    user.name = "Petro"
    db_session.commit()
    updated_user = db_session.query(User).filter_by(id=user.id).first()
    assert updated_user.name == "Petro"

    #Delete
    db_session.delete(updated_user)
    db_session.commit()
    deleted_user = db_session.query(User).filter_by(name="Petro").first()
    assert deleted_user is None