# import time
# from selenium import webdriver  # импортируем webdriver
#
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
# driver.get("https://practice.automationtesting.in")
# time.sleep(1)
# My_Account_btn = driver.find_element_by_css_selector("a[href=\"https://practice.automationtesting.in/my-account/\"]")
# My_Account_btn.click()
#
# Email_send = driver.find_element_by_css_selector("input[type=\"email\"]")
# Email_send.send_keys("apoik4@yandex.ru")
# time.sleep(1)
# Password_send = driver.find_element_by_css_selector("input[id=\"reg_password\"]")
# Password_send.send_keys("147258369aAax!z")
# time.sleep(1)
# Register_btn = driver.find_element_by_css_selector("input[value=\"Register\"]")
# Register_btn.click()


#####Registration_login: логин в систему

import time
from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
driver.get("https://practice.automationtesting.in")
time.sleep(1)
My_Account_btn = driver.find_element_by_css_selector("a[href=\"https://practice.automationtesting.in/my-account/\"]")
My_Account_btn.click()

Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
Username_Login_send.send_keys("apoik4@yandex.ru")
time.sleep(1)
Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
Password_Login_send.send_keys("147258369aAax!z")
time.sleep(1)
Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
Login_btn.click()