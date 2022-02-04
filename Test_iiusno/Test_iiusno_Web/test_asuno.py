import allure
import pytest

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.Base_URL import Start_url


@allure.feature('Тесты для Web')
class TestAsuno:

    @allure.story('Проверки АСУНО')
    @allure.title('Авторизация АСУНО')
    @allure.description('Проверка возможности авторизации')
    @allure.severity('blocker')
    @pytest.mark.skip('Нет пользователей для авторизации')
    def test_asuno_Authorization(self, setup):
        setup.get(f'{Start_url}asuno')
        wait = WebDriverWait(setup, 15, 0.3)

        with allure.step('Открытие страницы авторизации "АСУНО"'):
            assert setup.title == 'АСУНО'

        login: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="login"]')))
        password: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]')))
        authButton: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))

        with allure.step('Наличие поля "Логин"'):
            assert login.get_attribute("id") == 'login'

        with allure.step('Наличие поля "Пароль"'):
            assert password.get_attribute("id") == 'password'