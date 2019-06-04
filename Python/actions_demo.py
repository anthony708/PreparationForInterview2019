from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/zhuduan/Documents/Projects/libs/chromedriver')
driver.get('https://google.com')

search_box = driver.find_element_by_name('q')

import time
time.sleep(5)

search_box.send_keys('seleniumhq' + Keys.RETURN)

time.sleep(10)
print(driver.title)

driver.quit()