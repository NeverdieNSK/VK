from selenium import webdriver
import secret
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://vk.com')
driver.implicitly_wait(10)
login = driver.find_element_by_css_selector('#index_email')
login.send_keys(secret.login)
password = driver.find_element_by_css_selector('#index_pass')
password.send_keys(secret.password)
button = driver.find_element_by_id('index_login_button')
button.click()
driver.implicitly_wait(10)
time.sleep(5)
driver.get('https://vk.com/' + secret.IDFr)
driver.implicitly_wait(10)
#Найти кнопку Написать сообщение и щелкнуть
button = driver.find_element(By.XPATH, '//button[text()="Написать сообщение"]')
button.click()
#Отправить сообщение
sb = driver.find_element_by_css_selector('#mail_box_editable')
sb.send_keys('Привет')
button = driver.find_element_by_css_selector('#mail_box_send')
button.click()

