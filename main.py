import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# Сообщение для ввода
massage = "Test massage!"

# ввод сообщения
driver_chrome.find_element(By.ID, "user-message").send_keys(massage)
print(f"Ввод сообщения - \"{massage}\".")

# пауза
time.sleep(2)

# найти кнопку Get Checked Value и нажать ее
driver_chrome.find_element(By.ID, "showInput").click()
print("Кнопка Get Checked Value нажата.")

# найти и сохранить в переменную значение сообщения
value_message = driver_chrome.find_element(By.ID, "message").text
print(f"Значение результата - {value_message}.")

# проверка сообщений
assert value_message == massage, "Ошибка: Сообщения должны совпадать."
print("Сообщения совпадают.")

# пауза
time.sleep(2)

# переменные и их сумма
first_value = 12345
second_value = 67890
sum_value = str(first_value + second_value)

# найти поля для ввода переменных и установить в них значения
driver_chrome.find_element(By.ID, "sum1").send_keys(str(first_value))
print("Ввод первого значения.")
driver_chrome.find_element(By.ID, "sum2").send_keys(str(second_value))
print("Ввод второго значения.")

# пауза
time.sleep(2)

# найти кнопку Get Sum и нажать ее
driver_chrome.find_element(By.XPATH, "//*[@id='gettotal']/button").click()
print("Кнопка Get Sum нажата.")

# найти и сохранить в переменную значение результата
value_result = driver_chrome.find_element(By.ID, "addmessage").text
print(f"Значение результата - {value_result}")

# проверка значений
assert value_result == sum_value, "Ошибка: Значения должны совпадать."
print("Значения совпадают.")

# закрыть страницу
driver_chrome.quit()
print("Страница закрыта.")
