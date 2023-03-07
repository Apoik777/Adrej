# import time
# from selenium import webdriver  # импортируем webdriver
#
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')  # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window()  # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
# driver.get("https://practice.automationtesting.in")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 600);")
# Selenium_Ruby_btn = driver.find_element_by_css_selector("a[data-product_id=\"160\"]")
# Selenium_Ruby_btn.click()
# tab_reviews = driver.find_element_by_css_selector("a[href=\"#tab-reviews\"]")
# tab_reviews.click()
# star_5_btn = driver.find_element_by_class_name("star-5")
# star_5_btn.click()
# YourReview_text = driver.find_element_by_css_selector("textarea[id=\"comment\"]")
# YourReview_text.send_keys("Nice book!")
# Name_text = driver.find_element_by_css_selector("input[id=\"author\"]")
# Name_text.send_keys("Andrej")
# Email_text = driver.find_element_by_css_selector("input[id=\"email\"]")
# Email_text.send_keys("apoik4@yandex.ru")
#
# Submit_btn = driver.find_element_by_css_selector("input[name=\"submit\"]")
# Submit_btn.click()
