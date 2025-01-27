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

@then('Verify each product contains the {text}')
def verify_out_of_stock_box(context,text):
    context.app.header.verify_out_of_stock_box(text)

@when ('Click on "Main menu"')
def click_on_main_menu(context):
    context.app.header.click_on_main_menu()


@when('Click on "Secondary"')
def click_on_secondary_button(context):
    context.app.header.click_on_secondary_button()


@when('Click on "Income"')
def click_on_income_button(context):
    context.app.header.click_on_income_button()

@when('Click on "My-listing" button from the header')
def click_my_listing_button_from_header(context):
    context.app.header.click_my_listing_button_from_header()


@when('Click on "Filter" button')
def click_on_filter_button(context):
    context.app.header.click_on_filter_button()

@when('Click on "close x" filter window')
def click_close_filter_window(context):
    context.app.header.click_close_filter_window()


