import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.credentials_generator import Credential
from libs.mapping import personal_account_button, registration_link, registration_name_input, registration_email_input, \
    registration_password_input, registration_button, header, login_input, password_input, login_button


@pytest.fixture()  # creates (registration) new user and open on the main page without login
def create_new_user():
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
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))

    return driver, credentials


@pytest.fixture()  # creates (registration) new user and login with them
def create_new_user_and_login():
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

    # login with newly created account
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_input).clear()
    driver.find_element(By.XPATH, login_input).send_keys(credentials.mail)
    driver.find_element(By.XPATH, password_input).clear()
    driver.find_element(By.XPATH, password_input).send_keys(credentials.password)
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))

    return driver, credentials
