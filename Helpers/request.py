from woocommerce import API


class Request:

    def __init__(self):
        """
        https://woocommerce.github.io/woocommerce-rest-api-docs/v3.htm
        """
        consumer_key = 'ck_86415af47c1a300b9fcf10e8953c27dc8744a8ac'
        consumer_secret = 'cs_df7569b9b893e02f5e96631ff11d6eb32c2d74c3'

        # consumer_key = 'ck_dbad24d509287ff9de167840adf053db5fbdb01d'
        # consumer_secret = 'cs_1498d14f8568edea0269d118d25c3a808b33d3c7'

        self.wcapi = API(
            url="http://127.0.0.1/wp",
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            wp_api=True,
            version="wc/v2"
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

    def delete(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        response = self.wcapi.delete(endpoint)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]