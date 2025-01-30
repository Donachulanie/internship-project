from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.steps.reelly_main_page import verify_out_of_stock_box
from pages.base_page import BasePage
from time import sleep



class Header(BasePage):

    CLICK_FILTER_SALES_STATUS = (By.CSS_SELECTOR, "[id='Location-2']")
    OUT_OF_STOCK_FROM_THE_SALES_STATUS_DROP_DOWN_FILTER =(By.CSS_SELECTOR,"[value*='Out of stock']")
    OFF_PLAN_BTN_LEFT_SIDE_MENU = (By.CSS_SELECTOR, '._1-link-menu.w-inline-block.w--current')
    #OFF_PLAN_BTN_LEFT_SIDE_MENU = (By.CSS_SELECTOR, "[id='w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b']")
    #OFF_PLAN_BTN_LEFT_SIDE_MENU = (By.CSS_SELECTOR, "[class='_1-link-menu w-inline-block w--current']")
    TOTAL_PROJECT_ITEMS_ON_HEADER = (By.CSS_SELECTOR, '.proparties_text_block.mobile')
    PRE_SALE_EOI_BOX = (By.CSS_SELECTOR, "[class*='commision-text-box']")
    OUT_OF_STOCK_BOX = (By.CSS_SELECTOR,"[class*='_5-comission']")
    MAIN_MENU_BUTTON = (By.CSS_SELECTOR, '.div-block-33')
    SECONDARY_BTN = (By.CSS_SELECTOR, "[id='w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b']")
    #INCOME_BTN = (By.CSS_SELECTOR,"[href='/ambassadors']")
    INCOME_BTN = (By.CSS_SELECTOR,"a[href='/ambassadors'] div img")
    OFF_PLAN_BTN_FROM_HEADER = (By.CSS_SELECTOR, "[id='w-node-b528dfcf-d2ee-f936-302e-86e97f0796e8-7f66df20']")
    MY_LISTING_FROM_HEADER = (By.CSS_SELECTOR, "[href='/my-secondary-listings']")
    FILTER_BTN = (By.CSS_SELECTOR, "[class='filter-button w-inline-block']")
    CLOSE_FILTER_WINDOW = (By.CSS_SELECTOR, "[class='h2-text-filters _1']")
    MEMBER_ICON_PAGE_BOTTOM = (By.CSS_SELECTOR, "[class='text_block_account-2']")



    def click_on_off_plan_from_side_menu(self):
        # element = WebDriverWait(driver=self.driver, timeout=10).until(
        #     EC.presence_of_element_located(self.OFF_PLAN_BTN_LEFT_SIDE_MENU)
        # )
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(10)
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(10)
        # self.driver.execute_script("window.scrollBy(0,2000)", "")
        # #element.click()

        self.click(*self.OFF_PLAN_BTN_LEFT_SIDE_MENU)



    def verify_the_total_project_items(self,amount):
        self.verify_partial_text(amount,*self.TOTAL_PROJECT_ITEMS_ON_HEADER)

    def filter_by_sale_status_of_out_of_stock(self):
        self.wait_and_click(*self.CLICK_FILTER_SALES_STATUS)
        self.wait_and_click(*self.OUT_OF_STOCK_FROM_THE_SALES_STATUS_DROP_DOWN_FILTER)
        sleep(5)

    def verify_presale_eoi(self):
        self.find_element(*self.PRE_SALE_EOI_BOX)

    # def verify_url(self,current_url):
    #     self.verify_url(current_url)

    def verify_out_of_stock_box(self,text):
        self.find_elements(*self.OUT_OF_STOCK_BOX)
        elements = self.find_elements(*self.OUT_OF_STOCK_BOX)
        for element in elements:
            self.verify_text('Out of stock',*self.OUT_OF_STOCK_BOX)



    def click_on_main_menu(self):
        wait = WebDriverWait(self.driver, 15)
        self.click(*self.MAIN_MENU_BUTTON)


    def click_on_secondary_button(self):
        self.click(*self.SECONDARY_BTN)

    def click_on_income_button(self):
        self.wait_for_element_clickable(*self.INCOME_BTN)

    def click_my_listing_button_from_header(self):
        self.wait_and_click(*self.MY_LISTING_FROM_HEADER)

    def click_on_filter_button(self):
        self.click(*self.FILTER_BTN)

    def click_close_filter_window(self):
        self.click(*self.CLOSE_FILTER_WINDOW)
        sleep(5)



#######################################