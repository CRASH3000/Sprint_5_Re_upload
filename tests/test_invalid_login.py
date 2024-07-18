import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.data_urls import DataUrls

def test_invalid_login(driver):
    driver.get(DataUrls.BASE_URL)

    # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )

    # Кликаем на кнопку
    account_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be(DataUrls.LOGIN_URL)
    )
    assert (
        driver.current_url == DataUrls.LOGIN_URL
    ), "Переход на страницу логина не произошел"

    # Заполняем поля логина неверными данными
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys("invalid@mail.com")

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys("wrongpassword")

    # Нажимаем на кнопку "Войти"
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что не произошло перехода на главную страницу
    assert (
        driver.current_url != DataUrls.BASE_URL
    ), f"Неожиданный переход на главную страницу: '{driver.current_url}'"

    # Проверка, что остается на странице логина
    assert (
        driver.current_url == DataUrls.LOGIN_URL
    ), f"Ожидаемый URL: 'https://stellarburgers.nomoreparties.site/login', фактический URL: '{driver.current_url}'"
