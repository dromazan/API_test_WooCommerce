from faker import Faker
from pytest import fixture


@fixture
def get_customer_json():
    faker = Faker()

    billing = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "company": "",
        "address_1": faker.street_address(),
        "address_2": "",
        "city": faker.city(),
        "state": faker.state_abbr(),
        "postcode": faker.postalcode(),
        "country": faker.country_code(),
        "email": faker.email(),
        "phone": faker.phone_number()
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
        "username": faker.user_name(),
        "billing": billing,
        "shipping": shipping
    }

    return data


@fixture
def get_random_customer_id(db_connect):

    query = f"""SELECT id 
    FROM {db_connect.db}.wp_users 
    WHERE id not in (SELECT id FROM {db_connect.db}.wp_users WHERE id=1) 
    ORDER BY RAND() LIMIT 1;"""

    id = db_connect.select(query)
    return id[0][0]


@fixture
def get_customer_update_json():
    f = Faker()
    first_name = f.first_name()
    data = {
        "first_name": first_name,
        "billing": {
            "first_name": first_name
        },
        "shipping": {
            "first_name": first_name
        }
    }

    return data
