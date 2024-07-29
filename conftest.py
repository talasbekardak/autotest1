import pytest


@pytest.fixture(scope="session")
def user():
    print("Test user")

    yield

    print("Back test user")
