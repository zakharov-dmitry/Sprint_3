from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.mapping import login_input, password_input, login_button, personal_account_button, current_email, \
    current_name, enter_in_account_button, registration_link, login_link, restore_password_link


def test_login_via_personal_account_button(create_new_user):
    # check successful login trough button personal account in header
    driver, credentials = create_new_user

    # login with newly created account
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_input).clear()
    driver.find_element(By.XPATH, login_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, password_input).clear()
    driver.find_element(By.XPATH, password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, login_button).click()

    # open account settings and check the user
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, current_email)))
    created_user_mail = driver.find_element(By.XPATH, current_email).get_attribute('value')
    created_user_name = driver.find_element(By.XPATH, current_name).get_attribute('value')
    assert credentials.mail == created_user_mail and credentials.name == created_user_name

    driver.quit()


def test_login_via_enter_in_account_button(create_new_user):
    # check successful login trough button enter in account on main page
    driver, credentials = create_new_user

    # login with newly created account
    driver.find_element(By.XPATH, enter_in_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_input).clear()
    driver.find_element(By.XPATH, login_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, password_input).clear()
    driver.find_element(By.XPATH, password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, login_button).click()

    # open account settings and check the user
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, current_email)))
    created_user_mail = driver.find_element(By.XPATH, current_email).get_attribute('value')
    created_user_name = driver.find_element(By.XPATH, current_name).get_attribute('value')
    assert credentials.mail == created_user_mail and credentials.name == created_user_name

    driver.quit()


def test_login_from_registration_form(create_new_user):
    # check successful login from registration page
    driver, credentials = create_new_user

    # open account page for new registration
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, registration_link).click()

    # navigate from account page to the login page
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_link)))
    driver.find_element(By.XPATH, login_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_input).clear()
    driver.find_element(By.XPATH, login_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, password_input).clear()
    driver.find_element(By.XPATH, password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, login_button).click()

    # open account settings and check the user
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, current_email)))
    created_user_mail = driver.find_element(By.XPATH, current_email).get_attribute('value')
    created_user_name = driver.find_element(By.XPATH, current_name).get_attribute('value')
    assert credentials.mail == created_user_mail and credentials.name == created_user_name

    driver.quit()


def test_login_from_forgot_password_form(create_new_user):
    # check successful login from forgot password page
    driver, credentials = create_new_user
    # open restore password page
    driver.find_element(By.XPATH, enter_in_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, restore_password_link)))
    driver.find_element(By.XPATH, restore_password_link).click()

    # navigate to login page from restore password page
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_link)))
    driver.find_element(By.XPATH, login_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_input).clear()
    driver.find_element(By.XPATH, login_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, password_input).clear()
    driver.find_element(By.XPATH, password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, login_button).click()

    # open account settings and check the user
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, current_email)))
    created_user_mail = driver.find_element(By.XPATH, current_email).get_attribute('value')
    created_user_name = driver.find_element(By.XPATH, current_name).get_attribute('value')
    assert credentials.mail == created_user_mail and credentials.name == created_user_name

    driver.quit()

