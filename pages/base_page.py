from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self,url):
        self.driver.get(url)
        logger.info(f'Opening URL {url}')

    def get_url(self):
        return self.driver.current_url

    def find_element(self,*locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self,*locator):
        logger.info(f'Clicking element by {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
        logger.info(f'Entering text "{text}" by {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message = f'Element by {locator} not visible'
                        )

    def wait_for_element_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message = f'Element by {locator} should not be visible'
                        )

    def wait_for_element_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message = f'Element by {locator} not clickable'
                        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message = f'Element by {locator} not clickable'
                        ).click()


    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text},but go {actual_text}'

    def verify_partial_url(self,expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected partial url {expected_url} not in {actual_url}'

    def verify_url(self,expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected partial url {expected_url} does not match {actual_url}'