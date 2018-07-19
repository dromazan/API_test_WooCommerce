from Helpers.request import Request
from Tests.Customers.customer_helpers import *
from Helpers.helpers import map_response
from Helpers.assertions import assert_valid_schema

req = Request()
q = DBConnect()


def test_create_customer():
    """
    http://woocommerce.github.io/woocommerce-rest-api-docs/#create-a-customer

    Create a customer
    This API helps you to create a new customer.

    HTTP request
    POST /wp-json/wc/v2/customers
    """

    # getting new customer json
    customer = Customer().data

    # posting new customer
    response = req.post('customers', customer)

    status_code = response[0]
    response_body = response[1]
    response_url = response[2]

    # checking the response status
    assert status_code == 201, 'Response code is not 201'

    # validate json schema
    assert_valid_schema(response_body, 'customer.json')

    resp_id = response_body['id']

    # mapping response to the request structure
    mapped_response = map_response(customer, response_body)

    # verifying response
    assert mapped_response == customer, 'Requested data doesn\'t match with response data'

    # verifying data in DB
    fields = ('nickname',
              'first_name',
              'last_name',
              'billing_first_name',
              'billing_last_name',
              'billing_address_1',
              'billing_city',
              'billing_state',
              'billing_postcode',
              'billing_country',
              'billing_email',
              'billing_phone',
              'shipping_first_name',
              'shipping_last_name',
              'shipping_address_1',
              'shipping_city',
              'shipping_state',
              'shipping_postcode',
              'shipping_country'
              )

    query = """
            select meta_key, meta_value from wp43.wp_usermeta where user_id={} and meta_key in {}
            """.format(resp_id, fields)

    # executing select statement
    qresp = q.select('wp43', query)

    nickname = qresp[0][1]
    first_name = qresp[1][1]
    last_name = qresp[2][1]
    billing_first_name = qresp[3][1]
    billing_last_name = qresp[4][1]
    billing_address_1 = qresp[5][1]
    billing_city = qresp[6][1]
    billing_state = qresp[7][1]
    billing_postcode = qresp[8][1]
    billing_country = qresp[9][1]
    billing_email = qresp[10][1]
    billing_phone = qresp[11][1]
    shipping_first_name = qresp[12][1]
    shipping_last_name = qresp[13][1]
    shipping_address_1 = qresp[14][1]
    shipping_city = qresp[15][1]
    shipping_state = qresp[16][1]
    shipping_postcode = qresp[17][1]
    shipping_country = qresp[18][1]

    # verifying data from db and response match
    assert nickname == customer['username'], 'Username in request and db doesn\'t match'
    assert first_name == customer['first_name'], 'First name in request and db doesn\'t match'
    assert last_name == customer['last_name'], 'Last name in request and db doesn\'t match'
    assert billing_first_name == customer['billing']['first_name'], 'Billing first name in request and db doesn\'t match'
    assert billing_last_name == customer['billing']['last_name'], 'Billing last name in request and db doesn\'t match'
    assert billing_address_1 == customer['billing']['address_1'], 'billing address in request and db doesn\'t match'
    assert billing_city == customer['billing']['city'], 'billing city in request and db doesn\'t match'
    assert billing_state == customer['billing']['state'], 'billing state in request and db doesn\'t match'
    assert billing_postcode == customer['billing']['postcode'], 'billing postcode in request and db doesn\'t match'
    assert billing_country == customer['billing']['country'], 'billing country in request and db doesn\'t match'
    assert billing_email == customer['billing']['email'], 'billing email in request and db doesn\'t match'
    assert billing_phone == customer['billing']['phone'], 'billing phone in request and db doesn\'t match'
    assert shipping_first_name == customer['shipping']['first_name'], 'shipping first name in request and db doesn\'t match'
    assert shipping_last_name == customer['shipping']['last_name'], 'shilling last name in request and db doesn\'t match'
    assert shipping_address_1 == customer['shipping']['address_1'], 'shipping address in request and db doesn\'t match'
    assert shipping_city == customer['shipping']['city'], 'shipping city in request and db doesn\'t match'
    assert shipping_state == customer['shipping']['state'], 'shipping state in request and db doesn\'t match'
    assert shipping_postcode == customer['shipping']['postcode'], 'shipping postcode in request and db doesn\'t match'
    assert shipping_country == customer['shipping']['country'], 'shipping country in request and db doesn\'t match'
