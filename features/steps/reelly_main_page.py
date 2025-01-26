from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click on “Off plan” at the left side menu')
def click_on_off_plan_from_left_side_menu(context):
    context.app.header.click_on_off_plan_from_side_menu()


@then('Verify Presale(EOI) box shown')
def verify_presale_eoi(context):
    context.app.header.verify_presale_eoi()


@when('Filter by sale status of “Out of Stock”')
def filter_by_sale_status_of_out_of_stock(context):
    context.app.header.filter_by_sale_status_of_out_of_stock()

@then('Verify each product contains the Out of Stock')
def verify_out_of_stock_box(context):
    context.app.header.verify_out_of_stock_box()

########################