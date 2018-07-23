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

    def put(self, endpoint, data):
        """

        :param data:
        :param endpoint:
        :return:
        """
        response = self.wcapi.put(endpoint, data)

        response_code = response.status_code
        response_body = response.json()
        response_url = response.url

        return [response_code, response_body, response_url]
