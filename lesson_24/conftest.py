import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('test_search.log', mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.fixture(scope='session')
def log():
    return logger

BASE_URL = "http://127.0.0.1:8080"
TEST_USER = 'test_user'
TEST_PASS = 'test_pass'


@pytest.fixture(scope='class')
def authenticated_session(log):
    log.info("--- Запуск фікстури авторизації (scope='class') ---")

    session = requests.Session()
    auth_url = f'{BASE_URL}/auth'

    try:
        response = session.post(
            url=auth_url,
            auth=HTTPBasicAuth(TEST_USER, TEST_PASS)
        )
        response.raise_for_status()
        auth_data = response.json()
        access_token = auth_data.get('access_token')

        if access_token:
            session.headers.update({
                'Authorization': f'Bearer {access_token}'
            })
            log.info("Успішна аутентифікація. Токен додано до сесії.")
            return session
        else:
            log.error(f"Аутентифікація успішна (200), але відсутній 'access_token'. Відповідь: {auth_data}")
            pytest.fail("Не вдалося отримати access_token")

    except requests.exceptions.HTTPError as e:
        log.error(f"Помилка HTTP під час аутентифікації: {e}")
        log.error(f"Відповідь сервера: {response.text}")
        pytest.fail(f"Помилка аутентифікації: {e}")
    except requests.exceptions.ConnectionError:
        log.error(
            "Не вдалося підключитися до Flask-додатку. Переконайтеся, що він запущений на http://127.0.0.1:8080.")
        pytest.fail("Помилка підключення до сервера.")