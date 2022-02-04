import allure

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.Base_URL import Start_url

@allure.feature('Тесты для Web')
class TestHomePage:

    @allure.story('Проверки главной страницы')
    @allure.title('Открываем страницу ИИУСНО')
    @allure.description('Проверки на главной странице ИИУСНО')
    @allure.severity('blocker')
    def test_iiusno_open(self, setup):
        setup.get(Start_url)
        with allure.step('Открываем страницу "ИИУСНО"'):
            assert setup.title == 'ИИУСНО'

        wait = WebDriverWait(setup, 15, 0.3)

        with allure.step('Проверка наличия кнопки "АСУНО"'):
            element: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/asuno"]/div['
                                                                                         '@class="content-item-title"]')))
            assert element.get_attribute("innerText") == 'АСУНО'

        with allure.step('Проверка наличия кнопки "АС УФАП / ТОиР"'):
            element: WebElement = wait.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@href="/jsf/f?p=146"]/div['
                                                            '@class="content-item-title"]')))
            assert element.get_attribute("innerText") == 'АС УФАП / ТОиР'

    @allure.story('Проверки главной страницы')
    @allure.title('Открытие страницы авторизации "АСУНО"')
    @allure.description('Проверки открытия страницы авторизации "АСУНО" со страницы ИИУСНО')
    @allure.severity('blocker')
    def test_iiusno_open_asuno(self, setup):
        setup.get(Start_url)
        wait = WebDriverWait(setup, 15, 0.3)

        element: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/asuno"]')))
        element.click()

        with allure.step('Открытие страницы "АСУНО"'):
            assert setup.title == 'АСУНО'

    @allure.story('Проверки главной страницы')
    @allure.title('Открытие страницы авторизации "АС УФАП / ТОиР"')
    @allure.description('Проверки открытия страницы авторизации "АС УФАП / ТОиР" со страницы ИИУСНО')
    @allure.severity('blocker')
    def test_iiusno_open_toir(self, setup):
        setup.get(Start_url)

        wait = WebDriverWait(setup, 15, 0.3)

        element: WebElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/jsf/f?p=146"]')))
        element.click()

        with allure.step('Открытие страницы "АС УФАП / ТОиР"'):
            assert setup.title == 'Автоматизированная система управления материальными фондами, активами, техническим обслуживанием и ремонтами'