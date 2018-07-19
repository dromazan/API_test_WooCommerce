from Helpers.assertions import assert_valid_schema
from product_fixtures import get_random_product_id
from Helpers.request import Request
from Helpers.db_connect import DBConnect

request = Request()
q = DBConnect()


def test_retrieve_a_product():
    """
    http://woocommerce.github.io/woocommerce-rest-api-docs/#retrieve-a-product

    Retrieve a product
    This API lets you retrieve and view a specific product by ID.

    HTTP request
    GET /wp-json/wc/v2/products/<id>

    """

    # getting random product id
    prod_id = get_random_product_id()

    # getting product by id
    response = request.get('products/{}'.format(prod_id))

    status_code = response[0]
    response_data = response[1]

    # verifying status code
    assert status_code == 200, 'Status code is not 200'

    # validate json schema
    assert_valid_schema(response_data, 'product.json')

    resp_name = response_data['name'].lower()
    resp_status = response_data['status'].lower()

    # get product data from DB
    query = """
        select 
        post_name,
        post_status
        from wp43.wp_posts where id={}
        """.format(prod_id)

    # executing select statement
    qresp = q.select('wp43', query)

    db_name = qresp[0][0]
    db_status = qresp[0][1]

    # verifying data from db and response match
    assert resp_name == db_name, 'Response name and db name doesn\'t match'
    assert resp_status == db_status, 'Response status and db status doesn\'t match'
