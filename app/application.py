from pages.base_page import BasePage
#from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
#from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage





class Application:
    def __init__(self,driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page  = MainPage(driver)
        #self.search_results = SearchResultsPage(driver)
        #self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
