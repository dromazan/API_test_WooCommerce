import pytest
from Helpers.assertions import assert_valid_schema
from product_fixtures import get_random_product_id


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
    response_body = response[1]

    # verifying status code
    assert status_code == 200, 'Response code is not 200. Response is {}'.format(response_body['message'])

    # validate json schema
    assert_valid_schema(response_body, 'product.json')

    # get product data from DB
    query = """
        select * from {}.wp_posts where id={}
        """.format(db_connect.db, prod_id)

    # executing select statement
    qresp = db_connect.select(query)

    assert not qresp, 'DB select result is not empty, product is not deleted from the DB'
