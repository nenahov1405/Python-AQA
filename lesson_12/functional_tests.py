import unittest

from lesson_07.homework_07 import multiplication_table, summa, average_list_value, max_word_in_list, find_and_sort_cars

CAR_DATA = {'Toyota': ('blue', 2020, 1.8, 'sedan', 25000),
    'Audi': ('black', 2018, 2.0, 'sedan', 55000),
    'BMW': ('white', 2021, 3.0, 'suv', 70000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Lexus': ('gray', 2017, 2.5, 'coupe', 45000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000)
    }

class FunctionalTests(unittest.TestCase):

    #задача перевірити зупинку циклу при перевищенні порогу в 25
    def test_stop_when_result_exceeds_25(self):
        actual_result = multiplication_table(6)
        expected_result = ["6x1=6", "6x2=12", "6x3=18", "6x4=24"]
        self.assertEqual(actual_result, expected_result)

    #перевіряємо, що функція повертає порожній список, якщо > 25 (таблиці бути не повинно)
    def test_result_when_value_more_than_25(self):
        actual_result = multiplication_table(30)
        #в Пайтоні порожній список = False, тому можемо скористатись таким Assert-ом:
        self.assertFalse(actual_result)

    #перевіряємо, що функція multiplication_table(value) поверне помилку якщо передати рядок
    def test_multiplication_table_with_str_value(self):
        with self.assertRaises(TypeError):
            multiplication_table("5")

    # перевіряємо, що функція для додавання двох чисел вміє додавати строки
    def test_add_str_args(self):
        actual_result = summa("Hi", " Bob")
        self.assertIsInstance(actual_result, str)

    # перевіряємо випадок, коли функція для підрахунку AVG списку отримує на вхід порожній список
    def test_empty_list_avg(self):
        with self.assertRaises(ZeroDivisionError):
            average_list_value([])

    # #тестуємо функцію, яка приймає список слів та повертає найдовше слово у списку.
    # #цікавить випадок, коли кілька слів мають однакову (максимальну) довжину
    def test_max_word_in_list(self):
        fruits = ["apple", "pear", "kiwi", "grape"]
        result = max_word_in_list(fruits)
        self.assertEqual(result, "apple")

    #тестуємо функцію з фільтрацією авто
    #cценарій 1 -> виконуються всі умови фільтрації (happy path)
    def test_car_filtering_happy_path(self):
        result = find_and_sort_cars(CAR_DATA, (2018, 1.8, 50000))
        self.assertTrue(all(y >= 2018 and e >= 1.8 and p <= 50000 for _, y, e, p in result))

    #cценарій 2 -> якщо під параметри фільтру підпадає більше 3 машин (limit)
    def test_car_filtering_limited(self):
        result = find_and_sort_cars(CAR_DATA, (2016, 1.5, 100000), limit = 3)
        self.assertEqual(len(result), 3)

    #сценарій 3 -> перевіряємо, що відфільтровані машини ДІЙСНО відсортовані за зростанням ціни
    def test_car_filtering_happy_sorting(self):
        result = find_and_sort_cars(CAR_DATA, (2016, 1.5, 100000))
        prices = [r[3] for r in result]
        self.assertEqual(prices, sorted(prices))

    #сценарій 4 -> перевіряємо випадок коли кілька авто з однаковою ціною - їх порядок після сортування не змінеться
    def test_equal_prices_stability(self):
        data = {
            'CarA': ('red', 2020, 2.0, 'sedan', 30000),
            'CarB': ('blue', 2021, 2.0, 'sedan', 30000),
            'CarC': ('black', 2022, 2.0, 'sedan', 30000),
        }
        result = find_and_sort_cars(data, (2010, 1.0, 50000))
        names = [r[0] for r in result]
        self.assertEqual(names, ['CarA', 'CarB', 'CarC'])

if __name__ == "__main__":
    unittest.main(verbosity=2)