import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/zhuduan/Documents/Projects/libs/chromedriver')
driver.get('http://www.google.com')
time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('seleniumhq')
search_box.submit()
print(driver.title)
time.sleep(20)

driver.quit()