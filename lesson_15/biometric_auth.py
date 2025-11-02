#     Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника, отриманого з іншої функції від користувача.

#     Параметри користувача: id - int, name - str, second_name - str, age - int
#     Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ. Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
#     Функція повертає рівень доступу: full, read-only, forbiden

# # варіант вхідних значень
# database_users = [
#     {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
#     {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
# ]
# # варіанти user_input :
# {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
# {"id": 1, "name": "John", "second_name": "Joi", "age": 30}

import pytest

database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]

#Виходячи з умов задачі, я так розумію, що доцільно шукати до першого співпадіння (в рамках однієї проходки по базі)
#тобто, якщо співпало ІД, а все інше -ні, ми не шукаємо далі, а кажемо що forbidden
def biometric_auth(user_input):
    # рознесення даних юзера по окремих змінних
    id1 = user_input.get("id")
    name1 = user_input.get("name")
    second_name1 = user_input.get("second_name")
    age1 = user_input.get("age")
    #перебираємо кожен рядок таблиці Users в БД
    number_of_matches = None
    for user in database_users:
        number_of_matches = 0
        if id1 == user.get('id'):
            number_of_matches += 1
        if name1 == user.get('name'):
            number_of_matches += 1
        if second_name1 == user.get('second_name'):
            number_of_matches += 1
        if age1 == user.get('age'):
            number_of_matches += 1
        if number_of_matches < 3:
            return "forbidden"
        if number_of_matches == 3:
            return "read-only"
        if number_of_matches == 4:
            return "full"
    return None


@pytest.mark.parametrize("input_value, expected_output", [
    ({"id": 1, "name": "John", "second_name": "Doe", "age": 30}, "full"),
    ({"id": 1, "name": "John", "second_name": "Dop", "age": 30}, "read-only"),
    ({"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}, "forbidden"),
])
def test_biometric_auth(input_value, expected_output):
    assert biometric_auth(input_value) == expected_output