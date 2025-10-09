#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
#Створіть об'єкт цього класу, представляючи студента.
#Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
#Виведіть інформацію про студента та змініть його середній бал.

class Student:

    def __init__(self, first_name, last_name, age, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_mark = average_mark

    def change_of_average_mark(self, mark):
        self.average_mark = mark

    def print_student_info(self):
        print(f'Name: {self.first_name} | Lastname: {self.last_name} | Age: {self.age} | '
              f'Average Mark: {self.average_mark}')


student1 = Student(first_name='Ivan', last_name='Popov', age=19, average_mark=4.5)
student1.print_student_info()
student1.change_of_average_mark(3.9)
student1.print_student_info()