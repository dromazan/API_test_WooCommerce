from Helpers.request import Request
from Tests.Products.product_fixtures import *
from Helpers.helpers import map_response
import pytest
from Helpers.assertions import assert_valid_schema

request = Request()
q = DBConnect()


@pytest.mark.usefixtures
def test_create_a_product(get_product_json):
    """
    http://woocommerce.github.io/woocommerce-rest-api-docs/#create-a-product

    Create a product
    This API helps you to create a new product.

    HTTP request
    POST /wp-json/wc/v2/products
    """

    # getting new product json
    product = get_product_json

    # posting new product
    response = request.post('products', product)

    status_code = response[0]
    response_body = response[1]
    resp_id = response_body['id']

    # validate json schema
    assert_valid_schema(response_body, 'product.json')

    # checking the response status
    assert status_code == 201, 'Response code is not 201'

    # verifying response
    mapped_response = map_response(product, response_body)
    assert product == mapped_response, 'Requested data doesn\'t match with response data'

    # get product data from DB
    query = """
    select p.post_title, p.post_type, pm.meta_value from wp43.wp_posts as p join wp43.wp_postmeta as pm 
    on p.id=pm.post_id where p.id={} and pm.meta_key='_regular_price'
    """.format(resp_id)

    # executing select statement
    qresp = q.select('wp43', query)

    db_name = qresp[0][0]
    db_price = qresp[0][2]

    req_name = mapped_response['name']
    req_price = mapped_response['regular_price']

    # verifying data from db and response match
    assert db_name == req_name, 'name in db doesn\'t match with name in request'
    assert db_price == req_price, 'price in db doesn\'t match with price in request'

