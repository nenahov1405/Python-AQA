#---task 1-------------
#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()

#Я би робив через set так як це менш напряжно)
user_str = input('Введіть строку: ')
unique_user_chars = set(user_str)
if len(unique_user_chars) > 10:
    print("True")
else:
    print("False")

#---task 2-------------
#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
#(враховуються як великі так і маленькі). Цикл не повинен завершитися,
#якщо користувач ввів слово без букви "h".
while True:
    word = input('Введіть слово в якому буде літера Hh: ')
    if 'h' in word.lower():
        break

#---task 3-------------
#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
#Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []
for item in lst1:
    if isinstance(item, str):
        list2.append(item)
#для себе я зрозумів, що list comprehension крута штука і вирішував би так
# lst2 = [item for item in lst1 if isinstance(item, str)]

#---task 4-------------
#Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі
#я б цю задачу робив би через list comprehension)))
#якщо в список вже включено випадкові числа то буде ось так:
# list_sum = sum(k for k in my_list if x % 2 == 0)
import random
my_list = []
list_sum = 0
for k in range(1,21):
    k = random.randint(1,1000)
    my_list.append(k)
    if k % 2 == 0:
        list_sum += k
print(f'Сума парних чисел в списку: {list_sum}')