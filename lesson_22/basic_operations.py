from db_create_model import Session, Student, Course

def new_student_to_course(student_name: str, student_email: str, course_name: str):
    session = Session()
    print(f"Спроба додати студента {student_name} на курс '{course_name}'...")

    try:
        target_course = session.query(Course).filter(Course.name == course_name).first()
        if not target_course:
            print(f'Помилка! Курс {course_name} не знайдено')
            return

        new_student = Student(name=student_name, email=student_email)
        session.add(new_student)
        new_student.courses.append(target_course)
        session.commit()
        retrieved_student = session.get(Student, new_student.id)

        print(f"\nУспіх! Студент '{retrieved_student.name}' доданий.")
        enrolled_course_names = [c.name for c in retrieved_student.courses]
        print(f"Записаний на: {enrolled_course_names}")
    except Exception as e:
        session.rollback()
        print(f"\nВиникла помилка під час транзакції: {e}")
    finally:
        session.close()

new_student_to_course(
        student_name="Test Smith",
        student_email="smith@test.com",
        course_name="Physics"
    )