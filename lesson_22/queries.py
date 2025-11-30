from db_create_model import Session, Student, Course

def courses_by_student_name(student_name: str):
    session = Session()
    print(f'Курси студента {student_name}:')
    try:
        student = session.query(Student).filter(Student.name == student_name).first()
        if not student:
            print(f'Студента {student_name} не знайдено в базі')
            return []
        course_names = [c.name for c in student.courses]
        print(f'Знайдені курси: {course_names}')
        return course_names
    finally:
        session.close()


def students_by_course_name(course_name: str):
    session = Session()
    print(f'Студенти, що відвідують курс {course_name}:')
    try:
        course = session.query(Course).filter(Course.name == course_name).first()
        if not course:
            print(f'Курс {course_name} не знайдено в базі')
            return []
        student_names = [s.name for s in course.students]
        print(f'Знайдено студентів ({len(student_names)}): {', '.join(student_names)}')
        return student_names
    finally:
        session.close()

if __name__ == '__main__':
    test_student_name = "Test Smith"
    courses_by_student_name(test_student_name)
    students_by_course_name("Physics")
    students_by_course_name("Chemistry")
