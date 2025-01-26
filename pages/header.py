from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep



class Header(BasePage):

    CLICK_FILTER_SALES_STATUS = (By.CSS_SELECTOR, "[id='Location-2']")
    OUT_OF_STOCK_FROM_THE_SALES_STATUS_DROP_DOWN_FILTER =(By.CSS_SELECTOR,"[value*='Out of stock']")
    OFF_PLAN_BTN = (By.CSS_SELECTOR, '._1-link-menu.w-inline-block.w--current')
    TOTAL_PROJECT_ITEMS_ON_HEADER = (By.CSS_SELECTOR, '.proparties_text_block.mobile')
    PRE_SALE_EOI_BOX = (By.CSS_SELECTOR, "[class*='commision-text-box']")
    OUT_OF_STOCK_BOX = (By.CSS_SELECTOR,"[class*='_5-comission']")

    def click_on_off_plan_from_side_menu(self):
        self.click(*self.OFF_PLAN_BTN)
        sleep(5)


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

    def verify_out_of_stock_box(self):
        self.find_element(*self.OUT_OF_STOCK_BOX)


############################

