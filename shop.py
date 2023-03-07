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
# Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
# Username_Login_send.send_keys("apoik4@yandex.ru")
# time.sleep(1)
# Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
# Password_Login_send.send_keys("147258369aAax!z")
# time.sleep(1)
# Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
# Login_btn.click()
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
# driver.find_element_by_css_selector("a[data-product_id=\"181\"]").click()
# HTML_5_Forms_text = driver.find_element_by_class_name("entry-title").text
# print("тест, что заголовок книги назвается: \"HTML5 Forms\"")
# if HTML_5_Forms_text == "HTML5 Forms":
#     print("пройден")
# else:
#     print("не пройден")


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
# Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
# Username_Login_send.send_keys("apoik4@yandex.ru")
# time.sleep(1)
# Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
# Password_Login_send.send_keys("147258369aAax!z")
# time.sleep(1)
# Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
# Login_btn.click()
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
# driver.find_element_by_css_selector(".cat-item-19 a").click()
# HTML_product = driver.find_elements_by_class_name("product")
# print("В HTML сейчас товаров: "+(str(len(HTML_product))))


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
# Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
# Username_Login_send.send_keys("apoik4@yandex.ru")
# time.sleep(1)
# Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
# Password_Login_send.send_keys("147258369aAax!z")
# time.sleep(1)
# Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
# Login_btn.click()
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
#
# Default_sorting_value = driver.find_element_by_css_selector("option[value=\"menu_order\"]").text
# print("По умолчанию выбран вариант сортировки: \"Default sorting\"")
# Orderby_selected = driver.find_element_by_css_selector("option[selected=\"selected\"]").text
# if Default_sorting_value == Orderby_selected:
#     print("верно")
# else:
#     print("не верно")
#
# time.sleep(1)
# driver.find_element_by_css_selector("select :nth-child(6)").click()
# high_to_low = driver.find_element_by_css_selector("select :nth-child(6)").text
#
#
# Orderby_value = driver.find_element_by_css_selector("option[value=\"price-desc\"]").text
# print("Сейчас сортировка: " + Orderby_value)
#
# if high_to_low == Orderby_value:
#     print("верно")
# else:
#     print("не верно")


# import time
# from selenium import webdriver  # импортируем webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
# Username_Login_send.send_keys("apoik4@yandex.ru")
# time.sleep(1)
# Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
# Password_Login_send.send_keys("147258369aAax!z")
# time.sleep(1)
# Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
# Login_btn.click()
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
#
# driver.find_element_by_css_selector("a[data-product_id=\"169\"]").click()
#
# book_price = driver.find_element_by_css_selector(".price > del > span")
# book_price_text = book_price.text
#
# book_price_new = driver.find_element_by_css_selector(".price > ins > span")
# book_price_new_text = book_price_new.text
#
# assert book_price_text == "₹600.00"
# assert book_price_new_text == "₹450.00"
#
# book_sleep = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_sleep.click()
# book_sleep_clise = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_sleep_clise.click()




# import time
# from selenium import webdriver  # импортируем webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
# driver.get("https://practice.automationtesting.in")
# time.sleep(1)
# # My_Account_btn = driver.find_element_by_css_selector("a[href=\"https://practice.automationtesting.in/my-account/\"]")
# # My_Account_btn.click()
# #
# # Username_Login_send = driver.find_element_by_css_selector("input[id=\"username\"]")
# # Username_Login_send.send_keys("apoik4@yandex.ru")
# # time.sleep(1)
# # Password_Login_send = driver.find_element_by_css_selector("input[id=\"password\"]")
# # Password_Login_send.send_keys("147258369aAax!z")
# # time.sleep(1)
# # Login_btn = driver.find_element_by_css_selector("input[value=\"Login\"]")
# # Login_btn.click()
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
#
# Mastering_JavaScript_btn = driver.find_element_by_css_selector("a[data-product_id=\"165\"]")
# Mastering_JavaScript_btn.click()
# time.sleep(1)
#
# book_price_item = driver.find_element_by_class_name("cartcontents")
# book_price_item_text = book_price_item.text
#
# book_price_new = driver.find_element_by_css_selector("span[class=\"amount\"]")
# book_price_new_text = book_price_new.text
#
# print(book_price_item_text)
# print(book_price_new_text)
#
# assert book_price_item_text == "1 Item"
# assert book_price_new_text == "₹350.00"
# time.sleep(1)
#
# driver.find_element_by_class_name("wpmenucart-contents").click()
#
# Subtotal_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal"))).text #6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# # Subtotal_price = driver.find_element_by_class_name("cart-subtotal").text
# print(Subtotal_price)
#
# Total_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total"))).text #7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# # Total_price = driver.find_element_by_class_name("order-total").text
# print(Total_price)

# import time
# from selenium import webdriver  # импортируем webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
# driver.get("https://practice.automationtesting.in")
# time.sleep(1)
#
# Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
# Shop_btn.click()
#
# Mastering_JavaScript_btn =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-product_id=\"165\"]"))) #что-то слабо работает это команда!!!
# Mastering_JavaScript_btn.click()
# time.sleep(1) # все равно приходится добавить ожидание.
# Mastering_JavaScript_btn.click()
#
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(1)
#
# driver.find_element_by_class_name("wpmenucart-contents").click()

# driver.find_element_by_css_selector("input[type=\"number\"]").send_keys(Keys.DELETE, '1')
# time.sleep(2)
# driver.find_element_by_css_selector("a[data-product_id=\"165\"]").click()
# driver.find_element_by_css_selector(".woocommerce-message > a").click() # Отмена удаления
#
# q1 = driver.find_element_by_css_selector("input[type=\"number\"]")
# q1.clear()
# q1.send_keys(3)
# driver.find_element_by_css_selector("input[value=\"Update Basket\"]").click()
# time.sleep(2)
# q1_text = driver.find_element_by_css_selector("input[type=\"number\"]").get_attribute("value")
#
# assert q1_text == "3"
#
# driver.find_element_by_css_selector("input[value=\"Apply Coupon\"]").click()
# time.sleep(1)
# Test_Please = driver.find_element_by_css_selector(".woocommerce-error")
# Test_Please = Test_Please.text
# # print(Test_Please)
# assert Test_Please == "Please enter a coupon code."


import time
from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
driver.get("https://practice.automationtesting.in")
time.sleep(1)


Shop_btn = driver.find_element_by_css_selector("li[id=\"menu-item-40\"]")
Shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

Mastering_JavaScript_btn =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-product_id=\"165\"]")))
Mastering_JavaScript_btn.click()
time.sleep(1)
driver.find_element_by_class_name("wpmenucart-contents").click()

# ShowLogin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".showlogin")))
# ShowLogin.click()
#

PROCEED_TO_CHECKOUT = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
PROCEED_TO_CHECKOUT.click()


Firs_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
Firs_Name.send_keys("Andrej")

driver.find_element_by_css_selector("input[id=\"billing_last_name\"]").send_keys("Shumkov")
time.sleep(1)

driver.find_element_by_css_selector("input[id=\"billing_email\"]").send_keys("apoik4@yandex.ru")
time.sleep(1)

driver.find_element_by_css_selector("input[id=\"billing_phone\"]").send_keys("+787851456")
time.sleep(1)


driver.find_element_by_css_selector("span[id=\"select2-chosen-1\"]").click()
time.sleep(2)

driver.find_element_by_css_selector("div[id=\"select2-result-label-102\"]").click()
time.sleep(1)

driver.find_element_by_css_selector("input[id=\"billing_address_1\"]").send_keys("CCCP")
time.sleep(1)

driver.find_element_by_css_selector("input[id=\"billing_city\"]").send_keys(".ru")
time.sleep(1)

driver.find_element_by_css_selector("span[id=\"select2-chosen-2\"]").click()
time.sleep(1)

driver.find_element_by_css_selector("div[id=\"select2-result-label-253\"]").click()
time.sleep(1)


driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

driver.find_element_by_css_selector("input[id=\"place_order\"]").click()
time.sleep(1)

Thank_you = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received")))
Thank_you = Thank_you.text

assert Thank_you == "Thank you. Your order has been received."

Payment_Method = driver.find_element_by_css_selector("tfoot :nth-child(3)")
Payment_Method = Payment_Method.text
print(Payment_Method)

assert Payment_Method == "Direct Bank Transfer" # баг... 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"