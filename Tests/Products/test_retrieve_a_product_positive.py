from Helpers.assertions import assert_valid_schema
from product_fixtures import get_random_product_id
import pytest


@pytest.mark.usefixtures
def test_retrieve_a_product(get_random_product_id, request, db_connect):
    """
    http://woocommerce.github.io/woocommerce-rest-api-docs/#retrieve-a-product

    Retrieve a product
    This API lets you retrieve and view a specific product by ID.

    HTTP request
    GET /wp-json/wc/v2/products/<id>

    """

    # get random product id
    prod_id = get_random_product_id

    # getting product by id
    response = request.get(f'products/{prod_id}')

    status_code = response[0]
    response_body = response[1]

    # verifying status code
    assert status_code == 200, f"Response code is not 201. Response is {response_body['message']}"

    # validate json schema
    assert_valid_schema(response_body, 'product.json')

    resp_name = response_body['name'].lower()
    resp_status = response_body['status'].lower()

    # get product data from DB
    query = f"""
        SELECT post_name, post_status
        FROM {db_connect.db}.wp_posts where id={prod_id}
        """

    # executing select statement
    qresp = db_connect.select(query)

    db_name = qresp[0][0]
    db_status = qresp[0][1]

    # verifying data from db and response match
    assert resp_name == db_name, 'Response name and db name doesn\'t match'
    assert resp_status == db_status, 'Response status and db status doesn\'t match'
