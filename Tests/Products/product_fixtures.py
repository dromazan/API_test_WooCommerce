from faker import Faker
import random
from pytest import fixture, mark


@fixture
def get_product_json():
    """"
    Returns product json
    """
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


@fixture
@mark.usefixture
def get_random_product_id(db_connect):
    """
    Getting random product id

    :param db_connect: global fixture, DB connection
    :return: id
    """

    query = """
    SELECT ID
    FROM {}.wp_posts
    WHERE post_type='product'
    ORDER BY RAND() LIMIT 1;
    """.format(db_connect.db)

    id = db_connect.select(query)
    return id[0][0]

