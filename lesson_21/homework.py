import pytest

create_table_categories_q = """CREATE TABLE public.categories (
    category_id BIGINT GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NULL,
    CONSTRAINT categories_pk PRIMARY KEY (category_id));"""

create_table_products_q = """CREATE TABLE public.products (
    product_id BIGINT GENERATED ALWAYS AS IDENTITY,
    product_title VARCHAR NOT NULL,
    product_desc TEXT NULL,
    product_price NUMERIC(10, 2) NULL,
    cat_id BIGINT NULL, 
    CONSTRAINT products_pk PRIMARY KEY (product_id),
    CONSTRAINT products_categories_fk 
        FOREIGN KEY (cat_id) 
        REFERENCES public.categories(category_id));"""

import psycopg2
from faker import Faker

f = Faker()

# create connector, create cursor
dbname = 'postgres'
user = 'postgres'
password = 'SS6v29Ce3e'
host = 'localhost'
port = 5432

@pytest.fixture
def cursor():
    conn = psycopg2.connect(
	    database=dbname,
	    user=user,
        password=password,
        host=host,
        port=port
    )

    _cursor = conn.cursor()
    yield _cursor
    #знайшов що замість DELETE запитів можна просто робити ролбек
    conn.rollback()
    _cursor.close()
    conn.close()

#допоміжна фікстура, яка буде створювати категорію продукту та повертати її ID
@pytest.fixture
def category_id(cursor):
    temp_category_title = f.word()

    insert_query = f"""INSERT INTO public.categories (title) 
    VALUES ('{temp_category_title}')
    RETURNING category_id;"""

    cursor.execute(insert_query)
    new_id = cursor.fetchall()[0][0]
    yield new_id


TEST_CATEGORY_TITLES = [
    (f.word(),),
    (f.word(),),
    (f.word(),)
]

@pytest.mark.parametrize("category_title", TEST_CATEGORY_TITLES)
def test_create_new_category(cursor, category_title):

    insert_query = f"""
    INSERT INTO public.categories (title) 
    VALUES ('{category_title[0]}')
    RETURNING category_id;"""

    cursor.execute(insert_query)
    new_id = cursor.fetchall()[0][0]
    cursor.execute(f'SELECT title FROM public.categories WHERE category_id = {new_id}')
    created_title_from_db = cursor.fetchall()[0][0]

    assert created_title_from_db == category_title[0]

TEST_PRODUCTS = [
    #структура таблиці в БД така (product_title, product_desc, product_price)
    (f.sentence(nb_words=3), f.text(max_nb_chars=50), f.random_int(min=10, max=1000) / 10),
    (f.sentence(nb_words=4), f.text(max_nb_chars=60), f.random_int(min=500, max=2000) / 10),
]

@pytest.mark.parametrize("product_title, product_desc, product_price", TEST_PRODUCTS)
def test_create_product(cursor, category_id, product_title, product_desc, product_price):
    #ID категорії отримуємо фікстурою
    cat_id = category_id
    price_str = f'{product_price:.2f}'

    insert_query = f"""INSERT INTO public.products (product_title, product_desc, product_price, cat_id) 
                VALUES ('{product_title}', '{product_desc}', {price_str}, {cat_id}) 
                RETURNING product_id, product_title, product_desc, product_price, cat_id;"""
    cursor.execute(insert_query)
    created_product = cursor.fetchone()

    db_product_title = created_product[1]
    db_cat_id = created_product[4]
    db_product_price = created_product[3]

    assert db_product_title == product_title
    assert db_cat_id == category_id
    #перевіряємо - ціна продукту встановлена правильно
    assert round(float(db_product_price), 2) == round(product_price, 2)