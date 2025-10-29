import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from mapping import personal_account_button, header, registration_link, registration_email_input, registration_name_input, \
    registration_password_input, registration_button, login_input, password_input, login_button, current_email, current_name
from credentials_generator import Credential



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, header)))
time.sleep(3)
print("initial location")
print(driver.find_element(By.XPATH, ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']").location)



last_card = driver.find_elements(By.XPATH, ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")[-1]




driver.execute_script("arguments[0].scrollIntoView();", last_card)

print("location after scroll")
time.sleep(3)
print(driver.find_element(By.XPATH, ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']").location)

print("location after click")
driver.find_element(By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']").click()
time.sleep(3)
print(driver.find_element(By.XPATH, ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']").location)
print(driver.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']").location)

driver.quit()
