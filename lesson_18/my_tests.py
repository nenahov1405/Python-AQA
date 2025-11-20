import pytest
from .mars_photos import random_items_from_list

def test_random_items_from_list_length():
    """Перевіряє, що функція завжди повертає список довжиною 3."""
    test_list = list(range(100))
    result = random_items_from_list(test_list)

    assert isinstance(result, list)
    assert len(result) == 3


def test_random_items_from_list_content():
    """Перевіряє, що всі повернуті елементи є частиною оригінального списку."""
    test_list = ['a', 'b', 'c', 'd', 'e']
    result = random_items_from_list(test_list)
    for item in result:
        assert item in test_list


def test_random_items_from_list_not_enough_items():
    """Перевіряє, що функція генерує помилку, якщо елементів менше, ніж 3."""
    test_list = ['a', 'b']

    with pytest.raises(ValueError):
        random_items_from_list(test_list)