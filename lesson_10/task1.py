# Завдання 1
#Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи,
#Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий
# атрибут department, а клас Developer - атрибут programming_language.
#Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі
# атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на
# кількість розробників у команді, якою керує керівник.

class Employee:

    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

    def who_are_you(self):
        print('I am unknown employee')

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


    def __str__(self):
        return f'Створено менеджера {self.name} в відділі {self.department} із зарплатою {self.salary}'

    def who_are_you(self):
        print('I am manager')

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)

    def __str__(self):
        return f'Створено {self.programming_language} розробника {self.name} із зарплатою {self.salary}'

    def who_are_you(self):
        print('I am developer')

class TeamLead(Manager,Developer):

    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

    def __str__(self):
        return (f'Створено {self.programming_language} ліда {self.name} у відділі {self.department} '
                f'з командою {self.team_size} осіб та зарплатою {self.salary}')


manager1 = Manager(name="Alex", salary=20000, department="Operations")
developer1 = Developer(name="Kris", salary=15000, programming_language="Python")
team_lead1 = TeamLead(name="Ivan", salary=25000, department="Operations", programming_language="Python", team_size=3)
print(manager1)
print(developer1)
print(team_lead1)