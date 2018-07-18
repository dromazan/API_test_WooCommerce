from faker import Faker
import random

f = Faker()


class Product:

    def __init__(self):
        p_type = ['simple', 'grouped', 'external', 'variable']

        self.data = {
            "name": f.pystr(1, 20),
            "type": random.choice(p_type),
            "regular_price": '20.21', # str(f.pydecimal(2, 2, True)),
            "description": f.text(),
            "short_description": f.text(),
            "categories": [

            ],
            "images": [

            ]
        }
