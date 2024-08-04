from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.data_urls import DataUrls
from config.data_test_account import DataTestAccount


class TestAuthorization:

    def test_login_button(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Ждем, пока кнопка "Войти в аккаунт" не станет видимой, максимум 5 секунд
        login_account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_BUTTON)
        )

        # Кликаем на кнопку "Войти в аккаунт"
        login_account_button.click()

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

        # Кликаем на кнопку "Личный кабинет" повторно
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), "Переход на страницу профиля не произошел"

    def test_login_and_profile_access(self, driver):
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

        # Кликаем на кнопку "Личный кабинет" повторно
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), "Переход на страницу профиля не произошел"

    def test_login_via_registration_page(self, driver):
        driver.get(DataUrls.REGISTER_URL)

        # Ждем, пока ссылка "Восстановить пароль" не станет видимой, максимум 5 секунд
        forgot_password_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
        )

        # Кликаем на ссылку "Войти"
        forgot_password_link.click()

        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), "Переход на страницу авторизации не произошел"

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

        # Кликаем на кнопку "Личный кабинет" повторно
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), "Переход на страницу профиля не произошел"

    def test_login_forgot_password_and_login(self, driver):
        driver.get(DataUrls.LOGIN_URL)

        # Ждем, пока ссылка "Восстановить пароль" не станет видимой, максимум 5 секунд
        forgot_password_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        )

        # Кликаем на ссылку "Восстановить пароль"
        forgot_password_link.click()

        # Проверяем, что перешли на страницу восстановления пароля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.FORGOT_PASSWORD_URL))
        assert (
            driver.current_url == DataUrls.FORGOT_PASSWORD_URL
        ), "Переход на страницу восстановления пароля не произошел"

        # Нажимаем на кнопку "Войти"
        login_from_forgot_password_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_FROM_REGISTER_LINK)
        )
        login_from_forgot_password_link.click()

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
