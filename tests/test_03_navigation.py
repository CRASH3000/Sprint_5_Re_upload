from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config.data_urls import DataUrls
from config.data_test_account import DataTestAccount


class TestNavigation:

    def test_to_personal_account(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Ждем, пока кнопка "Войти в аккаунт" не станет видимой, максимум 5 секунд
        login_account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )

        # Кликаем на кнопку "Личный кабинет"
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

    def test_profile_to_constructor(self, driver):
        driver.get(DataUrls.LOGIN_URL)

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

        # Кликаем на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), "Переход на страницу профиля не произошел"

        # Кликаем на ссылку "Конструктор"
        constructor_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        # Проверяем, что перешли на главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.BASE_URL))
        assert (
            driver.current_url == DataUrls.BASE_URL
        ), "Переход на главную страницу не произошел после нажатия на ссылку 'Конструктор'"

    def test_profile_to_logo(self, driver):
        driver.get(DataUrls.LOGIN_URL)

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

        # Кликаем на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), "Переход на страницу профиля не произошел"

        # Кликаем на логотип
        logo_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGO_LINK)
        )
        logo_link.click()

        # Проверяем, что перешли на главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.BASE_URL))
        assert (
            driver.current_url == DataUrls.BASE_URL
        ), f"Переход на главную страницу не произошел после нажатия на логотип"

    def test_logout(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Кликаем на кнопку "Личный кабинет"
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

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
        ), f"Переход на главную страницу не произошел. Текущий URL: {driver.current_url}"

        # Кликаем на кнопку "Личный кабинет" повторно
        account_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # Проверяем, что перешли на страницу профиля
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.ACCOUNT_PROFILE_URL))
        assert (
            driver.current_url == DataUrls.ACCOUNT_PROFILE_URL
        ), f"Переход на страницу профиля не произошел. Текущий URL: {driver.current_url}"

        # Кликаем на кнопку "Выход"
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверяем, что перешли на страницу логина после выхода
        WebDriverWait(driver, 5).until(EC.url_to_be(DataUrls.LOGIN_URL))
        assert (
            driver.current_url == DataUrls.LOGIN_URL
        ), f"Переход на страницу логина не произошел после выхода. Текущий URL: {driver.current_url}"

    def test_default_buns_tab_active(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert (
            constructor_section.is_displayed()
        ), "Раздел конструктора бургеров отсутствует"

        # Проверяем, что вкладка "Булки" активна по умолчанию
        active_buns_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_BUNS_TAB)
        )
        assert active_buns_tab.is_displayed(), "Вкладка 'Булки' не активна по умолчанию"

    def test_sauce_scroll(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert (
            constructor_section.is_displayed()
        ), "Раздел конструктора бургеров отсутствует"

        # Нажимаем на кнопку "Соусы"
        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCE_TAB)
        )
        sauce_tab.click()

        # Проверяем, что вкладка "Соусы" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_SAUCE_TAB)
        )

        # Проверяем, что произошел скролл до элемента "Соус Spicy-X"
        spicy_x_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
        )
        assert spicy_x_sauce.is_displayed(), "Скролл до раздела 'Соусы' не произошел"

    def test_toppings_scroll(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert (
            constructor_section.is_displayed()
        ), "Раздел конструктора бургеров отсутствует"

        # Нажимаем на кнопку "Начинки"
        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.TOPPINGS_TAB)
        )
        sauce_tab.click()

        # Проверяем, что вкладка "Начинки" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_TOPPINGS_TAB)
        )

        # Проверяем, что произошел скролл до элемента "Мясо бессмертных моллюсков Protostomia"
        spicy_x_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PROTOSTOMIA_MEAT)
        )
        assert spicy_x_sauce.is_displayed(), f"Скролл до раздела 'Начинки' не произошел"

    def test_sauce_and_buns_scroll(self, driver):
        driver.get(DataUrls.BASE_URL)

        # Проверяем наличие раздела конструктора бургеров
        constructor_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.CONSTRUCTOR_SECTION)
        )
        assert (
            constructor_section.is_displayed()
        ), "Раздел конструктора бургеров отсутствует"

        # Нажимаем на кнопку "Соусы"
        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCE_TAB)
        )
        sauce_tab.click()

        # Проверяем, что вкладка "Соусы" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_SAUCE_TAB)
        )

        # Проверяем, что произошел скролл до элемента "Соус Spicy-X"
        spicy_x_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.SPICY_X_SAUCE)
        )
        assert spicy_x_sauce.is_displayed(), "Скролл до раздела 'Соусы' не произошел"

        # Нажимаем на кнопку "Булки"
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_TAB)
        )
        buns_tab.click()

        # Проверяем, что вкладка "Булки" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_BUNS_TAB)
        )

        # Проверяем, что произошел скролл до элемента "Флюоресцентная булка R2-D3"
        r2d3_bun = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.R2D3_BUN)
        )
        assert r2d3_bun.is_displayed(), "Скролл до раздела 'Булки' не произошел"
