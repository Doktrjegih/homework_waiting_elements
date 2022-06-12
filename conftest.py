import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://10.20.53.41:8081")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "opera":
        browser = webdriver.Opera()
    else:
        raise ValueError("Браузер передан неверно")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.url
    if "url" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("url", [option_value])
