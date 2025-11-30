from db_create_model import Session, Student, Course

def update_student_email(student_name: str, new_email: str):

    session = Session()
    print(f'Спроба оновити email для студента {student_name} на {new_email}')

    try:
        student = session.query(Student).filter(Student.name == student_name).first()
        if not student:
            print(f'Помилка, студента з таким {student_name} name не знайдено')
            return

        student.email = new_email
        session.commit()
        print(f'Email студента {student_name} успішно оновлено')
    except Exception as e:
        session.rollback()
        print(f'Помилка при оновленні даних про студента: {e}')
    finally:
        session.close()


def delete_student_by_name(student_name: str):

    session = Session()
    print(f'Спроба видалити студента {student_name}')

    try:
        student = session.query(Student).filter(Student.name == student_name).first()
        if not student:
            print(f'Помилка, студента з таким {student_name} name не знайдено')
            return

        session.delete(student)
        session.commit()
        print(f'Студент {student_name} успішно видалений з бази')
    except Exception as e:
        session.rollback()
        print(f'Помилка при видаленні даних про студента: {e}')
    finally:
        session.close()


if __name__ == '__main__':
    update_student_email("Test Smith", "new.smith.email@updated.com")
    delete_student_by_name("Test Smith")
    delete_student_by_name("Test Smith")  # Спроба видалити вдруге