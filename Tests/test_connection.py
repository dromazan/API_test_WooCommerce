from Helpers.request import Request


def test_connection():
    """

    :return:
    """
    request = Request()
    response = request.get('')
    assert response[0] == 200, 'Response code is not 200'
