import allure
import pytest
from selenium import webdriver

@allure.feature('Тесты для теста')
class TestPageSearch:

    @allure.title('Тестовый - Считаем')
    @allure.description('Фигня какая то')
    @allure.story('Остальные')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize('first, second, result', [
        (1, 2, 3),
        (2, 2, 4)
    ])
    def test_call(self, first, second, result):
        with allure.step(f'Считаем {first} + {second} и должны получить {result}'):
            assert first + second == result

    @allure.title('Тестовый и специально сломанный')
    @allure.description('Фигня какая то и ничего')
    @allure.story('Остальные')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.skip('Сломан почему то')
    def test_call_null(self):
        pass
