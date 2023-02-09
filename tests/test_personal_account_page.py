from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.mapping import personal_account_button, current_name


def test_open_personal_account_page_with_valid_user(create_new_user_and_login):
    # check opening of the personal account page after successful login
    driver, _ = create_new_user_and_login
    # open account settings and check the user
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, current_name)))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    driver.quit()
