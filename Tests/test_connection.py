from Helpers.request import Request
from pytest import mark


@mark.usefixtures
def test_connection(request):
    """
    simple test, verifies that we can request data from base url and get 200 response code
    :param request: global fixture, request entity
    :return: nothing
    """
    response = request.get('')
    assert response[0] == 200, 'Response code is not 200'
