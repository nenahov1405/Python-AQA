#1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
#В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {'Ivan', 'Maria', 'Olga', 'Bogdan'}
poker_blacklist = {'Elena', 'Semen', 'Maria', 'Olga', 'Vitaliy'}
alcohol_blacklist = {'Alex', 'Irina', 'Bogdan', 'Ivan', 'Maria'}
jackpot = australia_blacklist & poker_blacklist & alcohol_blacklist
print(jackpot)

#2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments',
# 'Oleh': 'Trench'}
#Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера.
#Використовувати цикл
dictionary = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
for user in dictionary:
    print(f'{user} is living in {dictionary[user]}')

#3 - Порахувати та вивести(print) кількість букв в строці.
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
# Прикдад:
# Юзер вводить:
# My name is Emmy Santiago.
# ВИ прінтаете щось накшталт:
# M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне,
# що б чітко було зрозуміло скільки разів зустрічаеться кожна буква)
my_line = input('Введіть строку: ')
my_dict = {}
for item in my_line:
    if item.isalpha():
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
for char, count in my_dict.items():
    print(f"'{char}': {count}")

# 4:Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічаеться у списку
# Умови:
# По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# Не використовувати методи/функції/класи
test_list = [1, 2, 'Hi', 'Bye', 2.3, False]
for item in test_list:
    if item is None:
        break
else:
    print("There is no None")

# 5 Вирішити задачу 3 без словника за 2 строки:
# 1 строка це input
# 2 строка це рішення
my_line = input('Введіть строку: ')
#тут в самій умові дуже явний натяк на dictionary компріхейшн)
my_dict = {char: my_line.count(char) for char in my_line if char.isalpha()}
print(my_dict)