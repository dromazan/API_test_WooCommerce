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


@fixture
def get_random_customer_id(db_connect):
    """
    Getting random product id from DB

    :param db_connect: global fixture which returns db connection
    :return: id
    """

    query = """
        SELECT id
        FROM {}.wp_users
        WHERE id not in (   SELECT id 
                            FROM {}.wp_users
                            WHERE id=1)
        ORDER BY RAND()  LIMIT 1;
        """.format(db_connect.db, db_connect.db)

    id = db_connect.select(query)
    return id[0][0]


@fixture
def get_customer_update_json():
    """
    Getting json for PUT request to update customer

    :return: data dictionary
    """
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
