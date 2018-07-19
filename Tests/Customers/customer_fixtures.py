from faker import Faker
from pytest import fixture


@fixture
def get_customer_json():
    f = Faker()

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

    data = {
        "email": billing['email'],
        "first_name": billing['first_name'],
        "last_name": billing['last_name'],
        "username": f.user_name(),
        "billing": billing,
        "shipping": shipping
    }

    return data

