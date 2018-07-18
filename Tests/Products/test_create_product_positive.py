from Helpers.request import Request
from Helpers.db_connect import DBConnect
from Tests.Products.product_helpers import Product
from Helpers.helpers import map_response

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
    resp_id = response_body['id']

    # check the response status
    assert status_code == 201, 'Response code is not 201'

    # verify rresponse
    mapped_response = map_response(product, response_body)
    assert product == mapped_response, 'Requested data doesn\'t match with response data'

    query = """
    select p.post_title, p.post_type, pm.meta_value from wp43.wp_posts as p join wp43.wp_postmeta as pm 
    on p.id=pm.post_id where p.id={} and pm.meta_key='_regular_price'
    """.format(resp_id)

    qresp = q.select('wp43', query)

    db_name = qresp[0][0]
    db_type = qresp[0][1]
    db_price = qresp[0][2]

    req_name = mapped_response['name']
    req_price = mapped_response['regular_price']

    assert db_name == req_name, 'name in db doesn\'t match with name in request'

    assert db_price == req_price, 'price in db doesn\'t match with price in request'

    #assert db_type == req_type, 'type in db doesn\'t match with type in request'  # Bug: type is always 'product'
