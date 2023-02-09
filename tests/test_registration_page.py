from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from libs.mapping import login_button, personal_account_button, registration_link, registration_name_input, \
    registration_email_input, registration_password_input, registration_button, header, error_msg_reg_pwd
from libs.credentials_generator import Credential


def test_registration_correct_inputs_successful_registration():
    # after successful registration the page for login is automatically opened
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
    # open account page for new registration
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, registration_link).click()
    credentials = Credential()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_button)))
    driver.find_element(By.XPATH, registration_name_input).clear()
    driver.find_element(By.XPATH, registration_name_input).send_keys(credentials.name)
    driver.find_element(By.XPATH, registration_email_input).clear()
    driver.find_element(By.XPATH, registration_email_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, registration_password_input).clear()
    driver.find_element(By.XPATH, registration_password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, registration_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()


def test_registration_short_password_error_message():
    # if provided by the registration password is too short(<5), you will get an error message
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
    # open account page for new registration
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, registration_link).click()
    credentials = Credential()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_button)))
    driver.find_element(By.XPATH, registration_name_input).clear()
    driver.find_element(By.XPATH, registration_name_input).send_keys(credentials.name)
    driver.find_element(By.XPATH, registration_email_input).clear()
    driver.find_element(By.XPATH, registration_email_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, registration_password_input).clear()
    driver.find_element(By.XPATH, registration_password_input).send_keys(credentials.short_password)
    driver.find_element(By.XPATH, registration_button).click()
    assert driver.find_element(By.XPATH, error_msg_reg_pwd).text == "Некорректный пароль"

    driver.quit()
