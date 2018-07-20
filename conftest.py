from pytest import fixture
from Helpers.db_connect import DBConnect
from Helpers.request import Request


@fixture
def request():
    return Request()


@fixture
def db_connect():
    return DBConnect()
