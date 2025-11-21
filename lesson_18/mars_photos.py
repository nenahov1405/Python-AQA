import requests
import random
import time

def get_links_from_url(url):
    try:
        response = requests.get(url)
        data = response.json()
        list_of_items = data.get('collection').get('items')
        list_of_refs = []
        for item in list_of_items:
            item_links = item.get('links')
            for link in item_links:
                list_of_refs.append(link.get('href'))
        return list_of_refs
    except requests.exceptions.RequestException as e:
        print(f'Помилка при запиті до API NASA: {e}')
        return []

def random_items_from_list(lst):
    return random.sample(lst, 3)


def download_photos(resourse):
    for ref in resourse:
        try:
            response = requests.get(ref)
            response.raise_for_status()
            timestamp = int(time.time() * 1000)
            filename = f'downloaded_file_{timestamp}_{random.randint(1, 1000)}.jpg'
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Успішно завантажено: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Помилка завантаження файлу {ref}: {e}")
        except IOError as e:
            print(f"Помилка запису файлу на диск: {e}")

refs = get_links_from_url("https://images-api.nasa.gov/search?q=mars&media_type=image")
rnd_refs = random_items_from_list(refs)
download_photos(rnd_refs)