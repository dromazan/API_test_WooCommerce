from woocommerce import API


class Request:

    def __init__(self):
        """
        https://woocommerce.github.io/woocommerce-rest-api-docs/v3.htm
        """
        consumer_key = 'ck_a7cab693f2efd19e67efa37d2c55f7862078aaa6'
        consumer_secret = 'cs_8e5057d6aec689775f1b16e4b073362253cdc2ea'

        self.wcapi = API(
            url='http://127.0.0.1/wp',
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version='v3'
        )

    def post(self, endpoint, data):
        """

        :param endpoint:
        :param data:
        :return:
        """

        response = self.wcapi.post(endpoint, data)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]

    def get(self, endpoint):
        """

        :param endpoint:
        :return:
        """

        response = self.wcapi.get(endpoint)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]
