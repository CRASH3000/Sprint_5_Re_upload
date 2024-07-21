from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.data_urls import DataUrls
from config.creating_test_account import (
    generate_username,
    generate_email,
    generate_password,
)
from config.data_test_account import DataTestAccount


class TestRegistration:

    def test_new_profile_registration(self, driver):
        driver.get(DataUrls.BASE_URL)

        login = generate_username()
        email = generate_email()
        password = generate_password()

        # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )

        # Кликаем на кнопку
        account_button.click()

        # Проверяем, что перешли на страницу авторизации
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу авторизации не произошел"

        register_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )

        register_button.click()

        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.REGISTER_URL))
        assert (
            driver.current_url == DataUrls.REGISTER_URL
        ), "Переход на страницу авторизации не произошел"

        # Заполняем поля формы регистрации
        name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        )
        name_field.send_keys(login)

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(password)

        # Нажимаем на кнопку "Зарегистрироваться"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
                driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу логина не произошел"

    def test_register_and_login(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )

        # Кликаем на кнопку "Личный кабинет"
        account_button.click()

        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу логина не произошел"

        # Нажимаем на кнопку "Зарегистрироваться"
        register_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()

        # Проверяем, что перешли на страницу регистрации
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.REGISTER_URL))
        assert (
            driver.current_url == DataUrls.REGISTER_URL
        ), "Переход на страницу регистрации не произошел"

        # Нажимаем на кнопку "Войти" на странице регистрации
        login_from_register_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
        )
        login_from_register_button.click()

        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу логина не произошел"

        # Заполняем поля логина
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(DataTestAccount.TEST_EMAIL)

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(DataTestAccount.TEST_PASSWORD)

        # Нажимаем на кнопку "Войти"
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        # Проверяем, что перешли на главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.BASE_URL))
        assert (
            driver.current_url == DataUrls.BASE_URL
        ), "Переход на главную страницу не произошел"

    def test_existing_profile_registration(self, driver):
        driver.get(DataUrls.REGISTER_URL)

        # Заполняем поля формы регистрации
        name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        )
        name_field.send_keys(DataTestAccount.TEST_NAME)

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(DataTestAccount.TEST_EMAIL)

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(DataTestAccount.TEST_PASSWORD)

        # Нажимаем на кнопку "Зарегистрироваться"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Проверяем, что появилось сообщение об ошибке "Такой пользователь уже существует"
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ERROR_MESSAGE_USER_EXISTS)
        )

        expected_error_message = "Такой пользователь уже существует"
        actual_error_message = error_message.text
        assert actual_error_message == expected_error_message, (
            f"Ожидаемое сообщение: '{expected_error_message}', "
            f"Фактическое сообщение: '{actual_error_message}'"
        )

    def test_empty_fields_registration(self, driver):
        driver.get(DataUrls.REGISTER_URL)

        # Нажимаем на кнопку "Зарегистрироваться" без заполнения полей
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)
        )
        submit_button.click()

        # Проверяем, что не произошло перехода на страницу логина
        assert driver.current_url != DataUrls.LOGIN_URL, (
            f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
            f"Фактическое: '{driver.current_url}'"
        )

    def test_invalid_login_register(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )

        # Кликаем на кнопку
        account_button.click()

        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу логина не произошел"

        # Заполняем поля логина неверными данными
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(DataTestAccount.TEST_UNREGISTERED_EMAIL)

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(DataTestAccount.TEST_UNREGISTERED_PASSWORD)

        # Нажимаем на кнопку "Войти"
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        # Проверяем, что не произошло перехода на главную страницу
        assert (
            driver.current_url != DataUrls.BASE_URL
        ), f"Неожиданный переход на главную страницу: '{driver.current_url}'"

        # Проверка, что остается на странице логина
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), f"Ожидаемый URL: 'https://stellarburgers.nomoreparties.site/login', фактический URL: '{driver.current_url}'"

    def test_invalid_email_registration(self, driver):
        driver.get(DataUrls.REGISTER_URL)

        # Заполняем поля формы регистрации
        name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        )
        name_field.send_keys(DataTestAccount.TEST_UNREGISTERED_NAME)

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(DataTestAccount.TEST_INVALID_EMAIL)  # Неполный email без собаки и домена

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(DataTestAccount.TEST_UNREGISTERED_PASSWORD)

        # Нажимаем на кнопку "Зарегистрироваться"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Проверяем, что появилось сообщение об ошибке "Пользователь уже существует"
        error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(Locators.ERROR_MESSAGE_USER_EXISTS)
            )

        expected_error_message = "Такой пользователь уже существует"
        actual_error_message = error_message.text
        assert actual_error_message == expected_error_message, (
            f"Ожидаемое сообщение: '{expected_error_message}', "
            f"Фактическое сообщение: '{actual_error_message}'"
        )

        # Проверяем, что не произошло перехода на страницу логина
        assert driver.current_url != DataUrls.LOGIN_URL, (
            f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
            f"Фактическое: '{driver.current_url}'"
        )

    def test_short_password_registration(self, driver):
        driver.get(DataUrls.REGISTER_URL)

        # Заполняем поля формы регистрации
        name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        )
        name_field.send_keys(DataTestAccount.TEST_UNREGISTERED_NAME)

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(DataTestAccount.TEST_UNREGISTERED_EMAIL)

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(DataTestAccount.TEST_INVALID_PASSWORD)  # Неполный пароль (меньше 7 символов)

        # Нажимаем на кнопку "Зарегистрироваться"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Проверяем, что появилось сообщение об ошибке "Некорректный пароль"
        error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(Locators.ERROR_MESSAGE_INVALID_PASSWORD)
            )

        expected_error_message = "Некорректный пароль"
        actual_error_message = error_message.text
        assert actual_error_message == expected_error_message, (
            f"Ожидаемое сообщение: '{expected_error_message}', "
            f"Фактическое сообщение: '{actual_error_message}'"
        )

        # Проверяем, что не произошло перехода на страницу логина
        assert (
            driver.current_url != "https://stellarburgers.nomoreparties.site/login"
        ), (
            f"Ожидаемое: не переходить на страницу 'https://stellarburgers.nomoreparties.site/login', "
            f"Фактическое: '{driver.current_url}'"
        )
