import os
import time
import pytest
import allure
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5433/testdb")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


@allure.step("Ініціалізація бази даних")
def init_db():
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="module")
def db_session():
    # Ожидание готовности БД (Healthcheck на уровне кода)
    retries = 5
    while retries > 0:
        try:
            init_db()
            break
        except OperationalError:
            retries -= 1
            if retries == 0:
                raise
            time.sleep(2)

    session = SessionLocal()
    yield session
    session.close()


@allure.epic("Керування користувачами")
@allure.feature("CRUD операції з базою даних")
class TestUserCRUD:

    @allure.story("Підʼєднання до БД")
    @allure.title("Перевірка зʼєднання з базою даних")
    def test_connection(self, db_session):
        with allure.step("Перевірити, що сесія з базорю даних створена"):
            assert db_session is not None

    @allure.story("Створення користувача")
    @allure.title("Успішне додавання нового користувача до БД")
    def test_create_user(self, db_session):
        with allure.step("Створити обʼєкт користувача 'Ivan'"):
            new_user = User(name="Ivan")

        with allure.step("Додати користувача до сесії та комітити"):
            db_session.add(new_user)
            db_session.commit()

        with allure.step("Перевірити, що у доданого користувача є ID"):
            assert new_user.id is not None

    @allure.story("Зчитування даних")
    @allure.title("Пошук користувача за імʼям")
    def test_read_user(self, db_session):
        with allure.step("Виконати запит на пошук користувача з імʼям 'Ivan'"):
            user = db_session.query(User).filter_by(name="Ivan").first()

        with allure.step("Перевірити коректність даних, що повертаються"):
            assert user is not None
            assert user.name == "Ivan"

    @allure.story("Оновлення даних")
    @allure.title("Зміна імʼя існуючого користувача")
    def test_update_user(self, db_session):
        with allure.step("Знайти користувача 'Ivan'"):
            user = db_session.query(User).filter_by(name="Ivan").first()

        with allure.step("Змінити імʼя на 'Petro' та зберегти"):
            user.name = "Petro"
            db_session.commit()

        with allure.step("Переконатись, що імʼя з базі оновилось"):
            updated_user = db_session.query(User).filter_by(id=user.id).first()
            assert updated_user.name == "Petro"

    @allure.story("Видалення даних")
    @allure.title("Видалення користувача з системи")
    def test_delete_user(self, db_session):
        with allure.step("Знайти користувача 'Petro'"):
            user = db_session.query(User).filter_by(name="Petro").first()

        with allure.step("Видалити користувача з БД"):
            db_session.delete(user)
            db_session.commit()

        with allure.step("Перевірити, що користувача больше не існує"):
            deleted_user = db_session.query(User).filter_by(name="Petro").first()
            assert deleted_user is None