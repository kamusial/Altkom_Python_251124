from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    file_name = teraz.strftime('screenshot%d-%M-%S.png')
    driver.get_screenshot_as_file(file_name)

driver = webdriver.Chrome()
driver.get('https://google.com')
print(f'Nazwa strony {driver.title}')
time.sleep(2)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
time.sleep(2)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Dokad noca tupta jeż?')
time.sleep(2)
search_field.send_keys(Keys.ENTER)
# search_button = driver.find_element('name', 'btnK')
# search_button.click()
time.sleep(2)
driver.quit()