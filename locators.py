class MainPage:
    LOGO = '//img[@title="Your Store"]'
    SLIDESHOW_PICTURES = '//div[@class="swiper-wrapper"]'
    SEARCH_INPUT = '//div[@id="search"]/input'
    SHOP_CART = '//button[@data-loading-text="Loading..."]'
    NAVIGATION_BAR = '//nav[@id="menu"]'


class CatalogPage:
    BREADCRUMBS = '//ul[@class="breadcrumb"]'
    ITEM = '//div[contains(@class, "product-layout")]'
    SELECT_INPUT = "//select"
    LEFT_MENU = '//div[@class="list-group"]'
    PAGE_TITLE = '//h2[text()="Monitors"]'


class ItemPage:
    ITEM_IMAGE = '//a[@class="thumbnail"]//img'
    NAME = '//h1[text()="Samsung SyncMaster 941BW"]'
    INPUT_AMOUNT = '//input[@name="quantity"]'
    ADD_TO_CART_BUTTON = '//button[text()="Add to Cart"]'
    FAVORITES_BUTTON = '//div[@class="btn-group"]//i[@class="fa fa-heart"]'


class LoginAdminPage:
    USERNAME_FIELD = '//input[@name="username"]'
    PASSWORD_FIELD = '//input[@name="password"]'
    SUMBIT_BUTTON = '//button[@type="submit"]'
    FORGET_PASSWORD = '//a[text()="Forgotten Password"]'
    OPENCART_SITE = '//a[@href="http://www.opencart.com"]'


class RegisterPage:
    RIGHT_MENU = "//aside"
    FIRSTNAME_FIELD = '//input[@name="firstname"]'
    PASSWORD_FIELD = '//input[@name="password"]'
    SUMBIT_BUTTON = '//input[@type="submit"]'
    POLICY_ARGEE_CHECKBOX = '//div[@class="pull-right"]//input[@type="checkbox"]'
