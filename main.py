from selenium import webdriver
import secret

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://vk.com')

login = driver.find_element_by_css_selector('#index_email')
login.send_keys('darkneverdie@mail.ru')
password = driver.find_element_by_css_selector('#index_pass')
password.send_keys('lalala')

button = driver.find_element_by_id('index_login_button')
button.click()


login.send_keys(secret.login)
driver.implicitly_wait(10)
password = driver.find_element_by_name('callback_1')
password.send_keys(secret.password)