from product_fixtures import get_random_product_id
from Helpers.global_fixtures import request, db_connect
import pytest
from Helpers.assertions import assert_valid_schema


@pytest.mark.usefixture
def test_delete_a_product(request, db_connect, get_random_product_id):
    """

    :param request:
    :param db_connect:
    :param get_random_product_id:
    :return:
    """

    # get random product id
    prod_id = get_random_product_id

    # getting product by id
    response = request.delete('products/{}?force=true'.format(prod_id))

    status_code = response[0]
    response_data = response[1]

    # verifying status code
    assert status_code == 200, 'Status code is not 200'

    # validate json schema
    assert_valid_schema(response_data, 'product.json')

    # get product data from DB
    query = """
        select * from wp43.wp_posts where id={}
        """.format(prod_id)

    # executing select statement
    qresp = db_connect.select('wp43', query)

    assert not qresp, 'DB select result is not empty, product is not deleted from the DB'
