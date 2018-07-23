import pytest
from customer_fixtures import get_customer_json

@pytest.mark.usefixture
def test_create_customer_with_empty_body(request):

    data = {}

    response = request.post('customers', data)

    response_code = response[0]
    response_body = response[1]

    assert response_code == 400, 'Response code is not 400 - Bad request'

    assert response_body['code'] == 'rest_missing_callback_param', 'Incorrect response error code'

    assert response_body['message'] == 'Missing parameter(s): email', 'Incorrect response error message'


@pytest.mark.usefixture
def test_create_customer_with_incorrect_email(get_customer_json, request):

    data = get_customer_json

    data['email'] = 'incorrect'

    response = request.post('customers', data)

    response_code = response[0]
    response_body = response[1]

    assert response_code == 400, 'Response code is not 400 - Bad request'

    assert response_body['code'] == 'customer_invalid_email', 'Incorrect response error code'

    assert response_body['message'] == 'Invalid email address', 'Incorrect response error message'


@pytest.mark.usefixture
def test_create_customer_with_incorrect_first_name(get_customer_json, request):

    data = get_customer_json

    data['first_name'] = 12345

    response = request.post('customers', data)

    response_code = response[0]
    response_body = response[1]

    assert response_code == 400, 'Response code is not 400 - Bad request'

    assert response_body['code'] == 'rest_invalid_param', 'Incorrect response error code'

    assert response_body['message'] == 'Invalid parameter(s): first_name', 'Incorrect response error message'

