import directions
import json

def open_and_validate_json(filepath):
    try:
        with open(filepath) as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Помилка! Файл не знайдено за шляхом {filepath}')
        return None
    except json.JSONDecodeError as e:
        print(f'Помилка розрору JSON-файлу: {filepath} Деталі: {e}')
        return None


json_file1_path = directions.FILES_DIR / 'json' / 'localizations_en.json'
json_file2_path = directions.FILES_DIR / 'json' / 'localizations_ru.json'
json_file3_path = directions.FILES_DIR / 'json' / 'login.json'
json_file4_path = directions.FILES_DIR / 'json' / 'swagger.json'

open_and_validate_json(json_file1_path)
open_and_validate_json(json_file2_path)
open_and_validate_json(json_file3_path)
open_and_validate_json(json_file4_path)