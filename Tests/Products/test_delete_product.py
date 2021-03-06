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
    response = request.delete(f'products/{prod_id}?force=true')

    status_code = response[0]
    response_body = response[1]

    # verifying status code
    assert status_code == 200, f"Response code is not 200. Response is {response_body['message']}"

    # validate json schema
    assert_valid_schema(response_body, 'product.json')

    # get product data from DB
    query = f"""
        SELECT * FROM {db_connect.db}.wp_posts WHERE id={prod_id}
        """

    # executing select statement
    qresp = db_connect.select(query)

    assert not qresp, 'DB select result is not empty, product is not deleted from the DB'
