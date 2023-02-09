# кнопка "личный кабинет" в хедере
personal_account_button = ".//a[@class='AppHeader_header__link__3D_hX' and @href='/account']"
# локатор хедера, одинаковый для всех страниц
header = ".//header[@class='AppHeader_header__X9aJA pb-4 pt-4']"
# кнопка/ссылка на страницу с регистрацией
registration_link = ".//a[@class='Auth_link__1fOlj' and @href='/register']"
# поле для ввода имени на странице с регистрацией
registration_name_input = ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']"
# поле для ввода почтового адреса на странице с регистрацией
registration_email_input = ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']"
# поле для ввода пароля на странице с регистрацией
registration_password_input = ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']"
# кнопка "Зарегистрироваться" на пформе регистрации
registration_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']"
# поле для ввода почтового адреса на странице для входа
login_input = ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']"
# поле для ввода пароля на странице для входа
password_input = ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']"
# кнопка "Войти" на странице для входа
login_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']"
# поле с текущим именем пользователя на странице с личными данными
current_name = ".//li[1]//input[@class='text input__textfield text_type_main-default input__textfield-disabled']"
# поле с почтовым адресом пользователя на странице с личными данными
current_email = ".//li[2]//input[@class='text input__textfield text_type_main-default input__textfield-disabled']"
# поле для отображения сообщения об ошибке при вводе неправильного пароля на странице регистрации
error_msg_reg_pwd = ".//p[@class='input__error text_type_main-default']"
# кнопка "Войти в аккаунт" на главной странице
enter_in_account_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
# ссылка "Войти" на странице с регистрацией
login_link = ".//a[@class='Auth_link__1fOlj' and text()='Войти']"
# ссылка "Восстановить пароль" на странице входа
restore_password_link = ".//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
# лого портала в хедере
burger_logo = ".//div[@class='AppHeader_header__logo__2D0X2']"
# кнопка "Конструктор" в хедере
constructor_button = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
# Кнопка "Выход" в личном кабинете
logout_button = ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"
# локаторы всех карточек с ингридиентами в секции для выбора ингридиентов
all_ingredients_cards = ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"
# локатор секции со всеми ингридиентами
section_ingredients = ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']"
# кнопка "Булки" в секции ингридиентов
button_bulki = ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
# кнопка "Соусы" в секции ингридиентов
button_sousy = ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
# кнопка "Начинки" в секции ингридиентов
button_nachinki = ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"




