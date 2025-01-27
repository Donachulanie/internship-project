from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@given('Open Reelly main page')
def open_main(context):
    context.app.main_page.open_main()

@when('input valid {email} and {password} on sign in page')
def input_valid_email_and_password(context,email,password):
    context.app.sign_in_page.input_valid_email_and_password(email,password)

@then ('Click on the "Continue" button')
def click_continue_button(context):
    context.app.sign_in_page.click_continue_button()

@then('Verify user is logged in successfully')
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()

