from woocommerce import API
import configparser
from os.path import join, dirname

config = configparser.ConfigParser()
config.read(join(dirname(__file__), 'config.cfg'))


class Request:

    def __init__(self):
        """
        http://woocommerce.github.io/woocommerce-rest-api-docs/
        """
        consumer_key = config['CONNECTION']['consumer_key']
        consumer_secret = config['CONNECTION']['consumer_secret']

        self.wcapi = API(
            url=config['CONNECTION']['url'],
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            wp_api=True,
            version="wc/v2"
        )

    def post(self, endpoint, data):
        """
        this method implements POST request to the provided endpoint with provided data in the body.

        :param endpoint: endpoinf for request
        :param data: json body
        :return: lis of elements - response_code, response_body, response_url
        """

        response = self.wcapi.post(endpoint, data)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]

    def get(self, endpoint):
        """
        this method implements GET request to the provided endpoint.

        :param endpoint: endpoint for request
        :return: lis of elements - response_code, response_body, response_url
        """

        response = self.wcapi.get(endpoint)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]

    def delete(self, endpoint):
        """
        this method implements DELETE request to the provided endpoint

        :param endpoint: endpoint for request
        :return: lis of elements - response_code, response_body, response_url
        """
        response = self.wcapi.delete(endpoint)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]

    def put(self, endpoint, data):
        """
        this method implements PUT request to the provided endpoint with provided data
        :param data: json body
        :param endpoint: endpoint for request
        :return: lis of elements - response_code, response_body, response_url
        """
        response = self.wcapi.put(endpoint, data)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]
