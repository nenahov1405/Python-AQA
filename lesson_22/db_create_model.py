from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import faker
import random

f = faker.Faker()

#З'єднання з базою даних PostgreSQL
DATABASE_URL = "postgresql://postgres:SS6v29Ce3e@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

student_course_mapping = Table('student_course_mapping', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Визначення моделі даних (таблиці) за допомогою класу
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    courses = relationship(
        "Course",
        secondary=student_course_mapping,
        backref="students"
    )

# Визначення моделі даних (таблиці) за допомогою класу
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)

def init_data_in_db():
    session = Session()
    new_students = []
    for k in range(20):
        std = Student(name=f.name(), email=f.email())
        new_students.append(std)

    courses_names = ['Math', 'Physics', 'Chemistry', 'Art', 'Computer Science']
    new_courses = []
    for course_name in courses_names:
        crs = Course(name=course_name)
        new_courses.append(crs)

    try:
        session.add_all(new_students)
        session.add_all(new_courses)
        session.commit()

        for student in new_students:
            count_of_courses = random.randint(1, 3)
            chosen_courses = random.sample(new_courses, count_of_courses)

            for course in chosen_courses:
                student.courses.append(course)

        session.commit()
        print('База даних успішно заповнена початковими даними')
    except Exception as e:
        session.rollback()
        print(f'Помилка при початковому заповненні таблиць БД: {e}')
    finally:
        session.close()

if __name__ == "__main__":
    init_data_in_db()