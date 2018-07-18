from faker import Faker
from Helpers.db_connect import DBConnect

f = Faker()


class Customer:

    def __init__(self):
        billing = {
            "first_name": f.first_name(),
            "last_name": f.last_name(),
            "company": "",
            "address_1": f.street_address(),
            "address_2": "",
            "city": f.city(),
            "state": f.state_abbr(),
            "postcode": f.postalcode(),
            "country": f.country_code(),
            "email": f.email(),
            "phone": f.phone_number()
        }

        shipping = {
            "first_name": billing['first_name'],
            "last_name": billing['last_name'],
            "company": "",
            "address_1": billing['address_1'],
            "address_2": "",
            "city": billing['city'],
            "state": billing['state'],
            "postcode": billing['postcode'],
            "country": billing['country']
        }

        self.data = {
            "email": billing['email'],
            "first_name": billing['first_name'],
            "last_name": billing['last_name'],
            "username": f.user_name(),
            "billing": billing,
            "shipping": shipping
        }

