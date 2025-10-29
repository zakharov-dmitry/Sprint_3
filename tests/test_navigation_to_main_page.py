import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.mapping import header, burger_logo, personal_account_button, constructor_button


def test_navigate_to_main_page_from_personal_account_via_burger_logo(create_new_user_and_login):
    # it is possible to jump to the main page via clicking on the burger logo on the personal account page
    driver, _ = create_new_user_and_login
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, burger_logo)))
    time.sleep(3)
    driver.find_element(By.XPATH, burger_logo).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()


def test_navigate_to_main_page_from_personal_account_via_constructor_button(create_new_user_and_login):
    # it is possible to jump to the main page via clicking on constructor button on the personal account page
    driver, _ = create_new_user_and_login
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, constructor_button)))
    time.sleep(3)
    driver.find_element(By.XPATH, constructor_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()


