import unittest

from lesson_07.homework_07 import multiplication_table

class FunctionalTests(unittest.TestCase):

    #задача перевірити зупинку циклу при перевищенні порогу в 25
    def test_stop_when_result_exceeds_25(self):
        actual_result = multiplication_table(6)
        expected_result = ["6x1=6", "6x2=12", "6x3=18", "6x4=24"]
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()