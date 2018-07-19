from faker import Faker
from Helpers.db_connect import DBConnect
import random
from pytest import fixture


@fixture
def get_product_json():
    p_type = ['simple', 'grouped', 'external', 'variable']
    f = Faker()
    data = {
        "name": f.pystr(1, 20),
        "type": random.choice(p_type),
        "regular_price": str(f.pydecimal(2, 2, True)),
        "description": f.text(),
        "short_description": f.text(),
    }
    return data


def get_random_product_id():

    d = DBConnect()

    query = """
    SELECT ID
    FROM wp43.wp_posts
    WHERE post_type='product'
    ORDER BY RAND() LIMIT 1;
    """

    id = d.select('wp43', query)
    return id[0][0]

