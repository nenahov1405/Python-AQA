import directions
import json
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def open_and_validate_json(filepath):
    try:
        with open(filepath) as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f'Файл не знайдено за шляхом: {filepath}')
        return None
    except json.JSONDecodeError as e:
        logging.error(f'Помилка розбору JSON-файлу: {filepath}. Деталі: {e}')
        return None


json_file1_path = directions.FILES_DIR / 'json' / 'localizations_en.json'
json_file2_path = directions.FILES_DIR / 'json' / 'localizations_ru.json'
json_file3_path = directions.FILES_DIR / 'json' / 'login.json'
json_file4_path = directions.FILES_DIR / 'json' / 'swagger.json'

open_and_validate_json(json_file1_path)
open_and_validate_json(json_file2_path)
open_and_validate_json(json_file3_path)
open_and_validate_json(json_file4_path)