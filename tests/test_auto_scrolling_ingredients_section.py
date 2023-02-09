import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from libs.mapping import header, section_ingredients, all_ingredients_cards, button_bulki, button_sousy, button_nachinki


def test_scroll_to_bulki_part():
    # check that clicking on button "Булки" till cause th scroll of the session till the necessary part
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
    # upper left corner of the whole section with ingredient
    y_location_section_ingredients = driver.find_element(By.XPATH, section_ingredients).location['y']
    # scrolling down till the end of the section to get random position of the "Булки" ingredients
    last_card = driver.find_elements(By.XPATH, all_ingredients_cards)[-1]
    driver.execute_script("arguments[0].scrollIntoView();", last_card)
    y_random_position_bulki = driver.find_element(By.XPATH, button_bulki).location['y']
    # click on "Булки" button to bring "Булки" on top (y coordinate should be equal to y of section with ingredient)
    driver.find_element(By.XPATH, button_bulki).click()
    y_top_position_bulki = driver.find_element(By.XPATH, button_bulki).location['y']

    assert y_top_position_bulki == y_location_section_ingredients != y_random_position_bulki

    driver.quit()


def test_scroll_to_sousy_part():
    # check that clicking on button "Соусы" till cause th scroll of the session till the necessary part
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
    # upper left corner of the whole section with ingredient
    y_location_section_ingredients = driver.find_element(By.XPATH, section_ingredients).location['y']
    # scrolling down till the end of the section to get random position of the "Соусы" ingredients
    last_card = driver.find_elements(By.XPATH, all_ingredients_cards)[-1]
    driver.execute_script("arguments[0].scrollIntoView();", last_card)
    y_random_position_sousy = driver.find_element(By.XPATH, button_sousy).location['y']
    # click on "Булки" button to bring "Соусы" on top (y coordinate should be equal to y of section with ingredient)
    driver.find_element(By.XPATH, button_sousy).click()
    y_top_position_sousy = driver.find_element(By.XPATH, button_sousy).location['y']

    assert y_top_position_sousy == y_location_section_ingredients != y_random_position_sousy

    driver.quit()


def test_scroll_to_nachinki_part():
    # check that clicking on button "Начинки" till cause th scroll of the session till the necessary part
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
    # upper left corner of the whole section with ingredient
    y_location_section_ingredients = driver.find_element(By.XPATH, section_ingredients).location['y']
    # scrolling down till the end of the section to get random position of the "Начинки" ingredients
    last_card = driver.find_elements(By.XPATH, all_ingredients_cards)[-1]
    driver.execute_script("arguments[0].scrollIntoView();", last_card)
    y_random_position_nachinki = driver.find_element(By.XPATH, button_nachinki).location['y']
    # click on "Булки" button to bring "Начинки" on top (y coordinate should be equal to y of section with ingredient)
    driver.find_element(By.XPATH, button_nachinki).click()
    y_top_position_nachinki = driver.find_element(By.XPATH, button_nachinki).location['y']

    assert y_top_position_nachinki == y_location_section_ingredients != y_random_position_nachinki

    driver.quit()



