import requests
import allure

from base.Base_URL import Start_url
from base.Base_User import Asuno_user_list

headers_ct = {"Content-Type": "application/json; charset=utf-8"}
user_login, user_pass, user_error = Asuno_user_list['wlop']


@allure.feature('Тесты для API')
class TestAsunoAPI:

    @allure.story('Проверки авторизации')
    @allure.title('Не проходящая авторизация')
    @allure.description('Проверка с неправильным логином и паролем')
    @allure.severity('blocker')
    def test_asuno_login_no_auth(self):
        response = requests.post(f'{Start_url}asuno/api/user/login/', headers=headers_ct, json={'username': user_login, 'password': user_pass})

        with allure.step('Получение кода "200"'):
            assert response.status_code == 200

        with allure.step('Получение ошибки "Wrong login or password"'):
            assert response.json()["message"] == user_error
