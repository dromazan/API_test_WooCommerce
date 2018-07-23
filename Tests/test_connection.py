from Helpers.request import Request
from pytest import mark


@mark.usefixtures
def test_connection(request):
    """

    :return:
    """
    response = request.get('')
    assert response[0] == 200, 'Response code is not 200'
