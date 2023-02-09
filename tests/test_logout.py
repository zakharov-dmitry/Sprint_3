from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.mapping import personal_account_button, logout_button, login_button


def test_successful_logout_from_personal_account_page(create_new_user_and_login):
    # after logging out user is redirected to login page
    driver, _ = create_new_user_and_login
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, logout_button)))
    driver.find_element(By.XPATH, logout_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()
