from Helpers.helpers import map_response
from Helpers.assertions import assert_valid_schema
from customer_fixtures import get_customer_json, get_random_customer_id, get_customer_update_json
import pytest


@pytest.mark.usefixture
def test_update_customer(get_random_customer_id, get_customer_update_json, request, db_connect):
    """
    hhttp://woocommerce.github.io/woocommerce-rest-api-docs/#update-a-customer

    Update a customer
    This API lets you make changes to a customer.

    HTTP request
    PUT /wp-json/wc/v2/customers/<id>
    """

    # getting new customer json
    customer = get_customer_update_json

    # getting random customer id
    c_id = get_random_customer_id

    # posting new customer
    response = request.put('customers/{}'.format(c_id), customer)

    status_code = response[0]
    response_body = response[1]
    response_url = response[2]
    print(response_url)

    # checking the response status
    assert status_code == 200, 'Response code is not 200. Response is {}'.format(response_body['message'])

    # validate json schema
    assert_valid_schema(response_body, 'customer.json')

    resp_id = response_body['id']

    # mapping response to the request structure
    mapped_response = map_response(customer, response_body)

    # verifying response
    assert mapped_response == customer, 'Requested data doesn\'t match with response data'

    # verifying data in DB
    fields = (
              'first_name',
              'billing_first_name',
              'shipping_first_name',
              )

    query = """
            select meta_key, meta_value from {}.wp_usermeta where user_id={} and meta_key in {}
            """.format(db_connect.db, c_id, fields)

    # executing select statement
    qresp = db_connect.select(query)

    first_name = qresp[0][1]
    billing_first_name = qresp[1][1]
    shipping_first_name = qresp[2][1]

    # verifying data from db and response match
    assert first_name == customer['first_name'], 'First name in request and db doesn\'t match'
    assert billing_first_name == customer['billing']['first_name'], 'Billing first name in request and db doesn\'t match'
    assert shipping_first_name == customer['shipping']['first_name'], 'shipping first name in request and db doesn\'t match'

