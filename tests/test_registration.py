import pytest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.creating_test_account import TestAccount
from config.data_urls import DataUrls


def test_page_load(driver):
    driver.get(DataUrls.BASE_URL)

    assert "404" not in driver.title, "Страница вернула ошибку 404"
    assert driver.find_element(By.TAG_NAME, "body"), "Страница не загрузилась корректно"


def test_new_profile_registration(driver):
    driver.get(DataUrls.BASE_URL)

    # Ждем, пока кнопка личного кабинета не станет видимой, максимум 5 секунд
    account_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )

    # Кликаем на кнопку
    account_button.click()

    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки

    # Проверяем, что перешли на страницу авторизации
    WebDriverWait(driver, 5).until(
        EC.url_to_be(DataUrls.LOGIN_URL)
    )
    assert driver.current_url == DataUrls.LOGIN_URL, "Переход на страницу авторизации не произошел"

    register_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    )

    register_button.click()

    time.sleep(2)

    WebDriverWait(driver, 5).until(
        EC.url_to_be(DataUrls.REGISTER_URL)
    )
    assert driver.current_url == DataUrls.REGISTER_URL, "Переход на страницу авторизации не произошел"

    # Заполняем поля формы регистрации
    name_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.NAME_FIELD)
    )
    name_field.send_keys(TestAccount.LOGIN)

    email_field = driver.find_element(*Locators.EMAIL_FIELD)
    email_field.send_keys(TestAccount.EMAIL)

    password_field = driver.find_element(*Locators.PASSWORD_FIELD)
    password_field.send_keys(TestAccount.PASSWORD)

    # Нажимаем на кнопку "Зарегистрироваться"
    submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
    submit_button.click()

    time.sleep(2)  # Пауза в 2 секунды для визуальной проверки
    try:
        WebDriverWait(driver, 5).until(
            EC.url_to_be(DataUrls.LOGIN_URL)
        )
    except TimeoutException:
        print(" Регистрация не прошла успешно")
        raise

    assert driver.current_url == DataUrls.LOGIN_URL, "Регистрация прошла успешно"



