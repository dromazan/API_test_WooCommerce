from Helpers.request import Request
from Helpers.db_connect import DBConnect
from Tests.Products.generate_product_json import Product
import json

request = Request()


def test_create_a_product():
    """
    HTTP request:
    POST /wc-api/v3/products

    :return:
    """
    product = Product().data

    response = request.post('products', product)

    print(json.dumps(response[1], indent=4))

