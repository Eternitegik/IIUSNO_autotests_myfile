import allure

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.Base_URL import Start_url
from base.Base_User import Toir_user_list


@allure.feature('Тесты для Web')
class TestToir:

    @allure.story('Проверки ТОиР')
    @allure.title('Авторизация ТОиР')
    @allure.description('Проверка возможности авторизации')
    @allure.severity('blocker')
    def test_toir_Authorization(self, setup):
        setup.get(f'{Start_url}/jsf/f?p=146')
        wait = WebDriverWait(setup, 15, 0.3)

        with allure.step('Открытие страницы авторизации "ТОиР"'):
            assert setup.title == 'Автоматизированная система управления материальными фондами, активами, техническим обслуживанием и ремонтами'

        login: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="P101_USERNAME"]')))
        password: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="P101_PASSWORD"]')))
        authButton: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@value="Вход"]')))

        with allure.step('Наличие поля "Логин"'):
            assert login.get_attribute("id") == 'P101_USERNAME'

        with allure.step('Наличие поля "Пароль"'):
            assert password.get_attribute("id") == 'P101_PASSWORD'

        login_test, password_test, user_role = Toir_user_list['tested']
        login.send_keys(login_test)
        password.send_keys(password_test)

        authButton.click()

        with allure.step('Открытие страницы после авторизации'):
            element: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//b[@class="info_role"]')))

            assert element.get_attribute('innerText') == user_role
