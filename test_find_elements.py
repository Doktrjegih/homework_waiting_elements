from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import locators


def is_element_present(driver, locator: str, timeout: int = 5) -> bool:
    try:
        WebDriverWait(driver=driver, timeout=timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
    except TimeoutException:
        return False
    return True


def find_elements(driver, locator: str, timeout: int = 5) -> List:
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(
            EC.visibility_of_any_elements_located((By.XPATH, locator))
        )
    except TimeoutException:
        return []


def test_main_page(driver, url):
    driver.get(url)
    assert is_element_present(driver, locators.MainPage.LOGO)
    assert len(find_elements(driver, locators.MainPage.SLIDESHOW_PICTURES)) == 2
    assert is_element_present(driver, locators.MainPage.SEARCH_INPUT)
    assert is_element_present(driver, locators.MainPage.SHOP_CART)
    assert is_element_present(driver, locators.MainPage.NAVIGATION_BAR)


def test_catalog_page(driver, url):
    driver.get(url + "/component/monitor")
    assert is_element_present(driver, locators.CatalogPage.BREADCRUMBS)
    assert len(find_elements(driver, locators.CatalogPage.ITEM)) == 2
    assert len(find_elements(driver, locators.CatalogPage.SELECT_INPUT)) == 2
    assert is_element_present(driver, locators.CatalogPage.LEFT_MENU)
    assert is_element_present(driver, locators.CatalogPage.PAGE_TITLE)


def test_item_page(driver, url):
    driver.get(url + "/component/monitor/samsung-syncmaster-941bw")
    assert is_element_present(driver, locators.ItemPage.ITEM_IMAGE)
    assert is_element_present(driver, locators.ItemPage.NAME)
    assert is_element_present(driver, locators.ItemPage.INPUT_AMOUNT)
    assert is_element_present(driver, locators.ItemPage.ADD_TO_CART_BUTTON)
    assert is_element_present(driver, locators.ItemPage.FAVORITES_BUTTON)


def test_login_admin_page(driver, url):
    driver.get(url + "/admin")
    assert is_element_present(driver, locators.LoginAdminPage.USERNAME_FIELD)
    assert is_element_present(driver, locators.LoginAdminPage.PASSWORD_FIELD)
    assert is_element_present(driver, locators.LoginAdminPage.SUMBIT_BUTTON)
    assert is_element_present(driver, locators.LoginAdminPage.FORGET_PASSWORD)
    assert is_element_present(driver, locators.LoginAdminPage.OPENCART_SITE)


def test_register_page(driver, url):
    driver.get(url + "/index.php?route=account/register")
    assert is_element_present(driver, locators.RegisterPage.RIGHT_MENU)
    assert is_element_present(driver, locators.RegisterPage.FIRSTNAME_FIELD)
    assert is_element_present(driver, locators.RegisterPage.PASSWORD_FIELD)
    assert is_element_present(driver, locators.RegisterPage.SUMBIT_BUTTON)
    assert is_element_present(driver, locators.RegisterPage.POLICY_ARGEE_CHECKBOX)
