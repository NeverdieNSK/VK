from selenium import webdriver
import secret

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

Search = id ts_input


