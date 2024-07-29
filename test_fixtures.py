import pytest


@pytest.fixture
def browser():
    print("Do before test")

    yield

    print("After test do")


@pytest.fixture
def main_page(browser):
    pass


@pytest.fixture(scope="session")
def user():
    print("Test user")

    yield

    print("Back test user")


def test_first(browser, user, main_page):
    pass


def test_second(browser, user, main_page):
    pass
