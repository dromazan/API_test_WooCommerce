from Helpers.request import Request
from Helpers.db_connect import DBConnect
from Tests.Products.generate_product_json import Product
import json

request = Request()
q = DBConnect()


def test_create_a_product():
    """
    HTTP request:
    POST /wc-api/v3/products

    :return:
    """
    product = Product().data

    response = request.post('products', product)

    status_code = response[0]
    response_body = response[1]
    response_url = response[2]

    assert status_code == 201, 'Response code is not 201'

    resp_name = response_body['name']
    resp_price = response_body['regular_price']
    resp_id = response_body['id']
    resp_type = response_body['type']

    req_name = product['name']
    req_price = product['regular_price']
    req_type = product['type']

    assert resp_name == req_name, 'product name in request and response doesn\'t match'

    assert resp_price == req_price, 'product price in request and response doesn\'t match'

    assert resp_type == req_type, 'product type in request and response doesn\'t match'

    query = """
    select p.post_title, p.post_type, pm.meta_value from wp43.wp_posts as p join wp43.wp_postmeta as pm 
    on p.id=pm.post_id where p.id={} and pm.meta_key='_regular_price'
    """.format(resp_id)

    qresp = q.select('wp43', query)

    db_name = qresp[0][0]
    db_type = qresp[0][1]
    db_price = qresp[0][2]

    assert db_name == req_name, 'name in db doesn\'t match with name in request'

    assert db_price == req_price, 'price in db doesn\'t match with price in request'

    assert db_type == req_type, 'type in db doesn\'t match with type in request' # Bug: type is always 'product'
