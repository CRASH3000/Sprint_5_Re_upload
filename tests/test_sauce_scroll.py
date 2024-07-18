import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.data_urls import DataUrls

def test_sauce_scroll(driver):
    driver.get(DataUrls.BASE_URL)

    # Проверяем наличие раздела конструктора бургеров
    constructor_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
    )
    assert constructor_section.is_displayed(), "Раздел конструктора бургеров отсутствует"

    # Нажимаем на кнопку "Соусы"
    sauce_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.SAUCE_TAB)
    )
    sauce_tab.click()
    time.sleep(2)  # Пауза для визуальной проверки

    # Проверяем, что произошел скролл до элемента "Соус Spicy-X"
    spicy_x_sauce = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
    )
    assert spicy_x_sauce.is_displayed(), "Скролл до раздела 'Соусы' не произошел"
