from faker import Faker
import random
from pytest import fixture, mark


@fixture
def get_product_json():
    p_type = ['simple', 'grouped', 'external', 'variable']
    faker = Faker()
    data = {
        "name": faker.pystr(1, 20),
        "type": random.choice(p_type),
        "regular_price": str(faker.pydecimal(2, 2, True)),
        "description": faker.text(),
        "short_description": faker.text(),
    }
    return data


@fixture
@mark.usefixture
def get_random_product_id(db_connect):

    query = f"""
    SELECT ID
    FROM {db_connect.db}.wp_posts
    WHERE post_type='product'
    ORDER BY RAND() LIMIT 1;
    """

    id = db_connect.select(query)
    return id[0][0]

