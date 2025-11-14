import directions
import csv

def read_csv_and_convert_to_set(filepath):
    try:
        with open(filepath) as file:
            reader = csv.reader(file)
            unique_rows = set(tuple(row) for row in reader)
            return unique_rows
    except FileNotFoundError:
        print(f'Помилка! CSV файл не знайдено в шляху {filepath}')
        return set() #повернули порожню множину

csv_file1_path = directions.FILES_DIR / 'csv' / 'random.csv'
csv_file2_path = directions.FILES_DIR / 'csv' / 'random-michaels.csv'

first_set = read_csv_and_convert_to_set(csv_file1_path)
second_set = read_csv_and_convert_to_set(csv_file2_path)

result_file = first_set ^ second_set

RESULT_FILE_PATH = directions.FILES_DIR / 'csv' / 'unique_csv.csv'
with open(RESULT_FILE_PATH, 'w', newline='') as result:
    writer = csv.writer(result)
    writer.writerow(result_file)