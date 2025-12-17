import pytest
import requests

TEST_CASES = [
    # Сортування за ціною, ліміт 5
    ('price', 5, 5, 'price'),
    # Сортування за роком, ліміт 7
    ('year', 7, 7, 'year'),
    # Сортування за брендом, ліміт None
    ('brand', None, 25, 'brand'),
    # Ліміт 2
    (None, 2, 2, None),
    # Ліміт 100
    ('engine_volume', 100, 25, 'engine_volume')
]

BASE_URL = "http://127.0.0.1:8080"


@pytest.mark.usefixtures("authenticated_session", "log")
class TestCarSearch:

    @pytest.mark.parametrize(
        "sort_by, limit, expected_count, expected_sort_field",
        TEST_CASES
    )
    def test_search_cars_with_params(
            self, authenticated_session, log,
            sort_by, limit, expected_count, expected_sort_field
    ):
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        log.info(f"--- Тест: sort_by={sort_by}, limit={limit} ---")

        response = authenticated_session.get(
            url=f'{BASE_URL}/cars',
            params=params
        )

        assert response.status_code == 200, \
            f"Очікувався статус 200, отримано {response.status_code}. Відповідь: {response.text}"
        cars = response.json()
        current_count = len(cars)

        log.info(f"Отримано {current_count} записів. Очікувалося {expected_count}.")
        assert current_count == expected_count, \
            f"Невірний ліміт. Отримано {current_count}, очікувалось {expected_count}."

        if expected_sort_field:
            if current_count > 1:

                first_value = cars[0].get(expected_sort_field)
                second_value = cars[1].get(expected_sort_field)

                if isinstance(first_value, (int, float, str)) and isinstance(second_value, (int, float, str)):
                    is_sorted = first_value <= second_value
                    log.info(
                        f"Перевірка сортування за {expected_sort_field}: {first_value} <= {second_value} -> {is_sorted}")
                    assert is_sorted, \
                        f"Невірне сортування за полем '{expected_sort_field}'. " \
                        f"Знайдено: {first_value} > {second_value}."

            log.info(f"Тест успішно пройдено з перевіркою сортування за полем: {expected_sort_field}.")
        else:
            log.info("Тест успішно пройдено без перевірки сортування.")