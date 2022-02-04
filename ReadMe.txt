#-----------------------------
# Используется Python 3.9
#-----------------------------

# Команды для запуска тестов и генерации отчетов
# 1) .\venv\Scripts\activate                               Переключение в venv для генерации отчетов
# 2) pytest --alluredir results_test                       Прогон тестов для генерации файлов на отчеты
#                                                                  Перед запусктом удалить все файлы в папке results_test кроме environment.xml
# 3) allure serve results_test/                            Запуск сервера для отображения отчета в html
# 4) allure generate results_test -o result_web --clean    Генерация html файлов для отображения отчетов

# Варианты критичности теста
# @allure.severity('blocker, critical, normal, minor, trivial')



#Полезные ссылки
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected
# https://github.com/Eternitegik/iiusno_autotest/settings/pages
# https://eternitegik.github.io/iiusno_autotest/