from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators import WikipediaHomepage,WikipediaArticle
import time
driver = webdriver.Chrome('/Users/zhuduan/Documents/Projects/libs/chromedriver')
driver.get('https://en.wikipedia.org')

random_link = driver.find_element(*WikipediaHomepage.Ramdom_Link)
random_link.click()

time.sleep(5)

first_heading = driver.find_element(*WikipediaArticle.First_Heading)
print(first_heading.text)

page_info = driver.find_element(*WikipediaArticle.Page_Info)
page_info.click()
time.sleep(5)

search_box = driver.find_element(*WikipediaArticle.Search_Box)
search_box.send_keys('Selenium (software)' + Keys.RETURN)
time.sleep(5)

logo = driver.find_element(*WikipediaArticle.Logo)
logo.click()
time.sleep(5)

driver.quit()