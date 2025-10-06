# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summa(a, b):
    return a + b

print(summa(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_list_value(lst):
    summ = 0
    for item in lst:
        summ += item
    return summ / len(lst)

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(average_list_value(test_list))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(formal_string):
    reversed_string = formal_string[::-1]
    return reversed_string

simple_test = "Geeksforgeeks"
print(reverse_string(simple_test))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_word_in_list(lst):
    max_word = lst[0]
    for word in lst:
        if len(word) > len(max_word):
            max_word = word
    return max_word

test_list = ["Yan", "Ivan", "Vitaliy", "Svyatoslav"]
print(max_word_in_list(test_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    if index == -1:
        return -1
    else:
        return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7 (task 3 from homework 6)
#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
#Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими

#function extracts lines from list and returns new list with lines
def extract_lines_from_list(lst):
    lst2 = []
    for item in lst:
        if isinstance(item, str):
            lst2.append(item)
    return lst2

print(extract_lines_from_list([1,2,3,4,5])) #expected result -> empty list
print(extract_lines_from_list([1,'Hi',3,'Positive',5])) #expected result -> ['Hi','Positive']

# task 8 (task 4 from homework 6)
#Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі
#function returns value of sum of paired numbers
def sum_of_paired_numbers(lst):
    list_sum = 0
    for item in lst:
        if item % 2 == 0:
            list_sum += item
    return list_sum

print(sum_of_paired_numbers([1,2,3,4,5,6,7,8,9,10])) #expected result sum = 30
print(sum_of_paired_numbers([1,3,5,7,9,11])) #expected result sum = 0

# task 9 (task 3 from homework 4)
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
def remove_extra_spaces(row):
    words = row.split()
    return " ".join(words)

row_with_extra_spaces = "Hi   this  sentance with           extra    spaces "
cleaned_row = remove_extra_spaces(row_with_extra_spaces)
print(f'Рядок з пробілами: {row_with_extra_spaces}')
print(f'Очищений рядок: {cleaned_row}')

# task 10 (Пошук автомобіля по крітеріях з homework 6)
#Шукає автомобілі, що відповідають критеріям, сортує їх за ціною (за зростанням)
#і повертає задану кількість (за замовчуванням 5) найкращих результатів.
#Функція реалізована з використанням filter() і map().
def find_and_sort_cars(car_data, search_criteria, limit=5):
    min_year, min_engine_volume, max_price = search_criteria
    def passes_criteria(item):
        """Перевіряє, чи відповідає елемент словника критеріям пошуку."""
        # item: ('Назва', (колір, рік, об'єм, тип, ціна))
        data = item[1]
        year = data[1]
        engine = data[2]
        price = data[4]
        return year >= min_year and engine >= min_engine_volume and price <= max_price

    # Застосовуємо фільтр до елементів словника car_data.items()
    filtered_items = filter(passes_criteria, car_data.items())

    def transform_data(item):
        """Перетворює відфільтрований елемент на кортеж (Назва, Рік, Об'єм, Ціна)."""
        name = item[0]
        data = item[1]
        return (name, data[1], data[2], data[4])
    # Перетворюємо відфільтровані елементи на список потрібних кортежів
    mapped_cars = list(map(transform_data, filtered_items))
    mapped_cars.sort(key=lambda x: x[3])
    return mapped_cars[:limit]

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria = (2017, 1.6, 36000)
top_cars = find_and_sort_cars(car_data, search_criteria)
print("--- Топ 5 знайдених автомобілів (за зростанням ціни) ---")
for name, year, engine, price in top_cars:
    print(f"Марка: {name:<10} | Рік: {year} | Об'єм: {engine:.1f} | Ціна: {price}")
if not top_cars:
    print("Автомобілі, що відповідають усім критеріям, не знайдено.")