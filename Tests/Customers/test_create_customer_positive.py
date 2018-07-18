from Helpers.request import Request
from Helpers.db_connect import DBConnect
from Tests.Customers.customer_helpers import *
from Helpers.helpers import map_response
import json

req = Request()
q = DBConnect()


def test_create_customer():
    """

    :return:
    """

    customer = Customer().data

    response = req.post('customers', customer)

    status_code = response[0]
    response_body = response[1]
    response_url = response[2]

    # check the response status
    assert status_code == 201, 'Response code is not 201'

    resp_id = response_body['id']

    mapped_response = map_response(customer, response_body)

    assert mapped_response == customer, 'Requested data doesn\'t match with response data'

    # verify data in DB
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

    assert nickname == customer['username'], 'text'
    assert first_name == customer['first_name'], 'text'
    assert last_name == customer['last_name']
    assert billing_first_name == customer['billing']['first_name']
    assert billing_last_name == customer['billing']['last_name']
    assert billing_address_1 == customer['billing']['address_1']
    assert billing_city == customer['billing']['city']
    assert billing_state == customer['billing']['state']
    assert billing_postcode == customer['billing']['postcode']
    assert billing_country == customer['billing']['country']
    assert billing_email == customer['billing']['email']
    assert billing_phone == customer['billing']['phone']
    assert shipping_first_name == customer['shipping']['first_name']
    assert shipping_last_name == customer['shipping']['last_name']
    assert shipping_address_1 == customer['shipping']['address_1']
    assert shipping_city == customer['shipping']['city']
    assert shipping_state == customer['shipping']['state']
    assert shipping_postcode == customer['shipping']['postcode']
    assert shipping_country == customer['shipping']['country']
