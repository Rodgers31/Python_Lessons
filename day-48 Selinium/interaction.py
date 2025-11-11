from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
wiki = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
wiki.click()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
# Find elements by link text
wiki_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
wiki_portals.click()

#Find the "Search" <input> name
search = driver.find_element(By.NAME, 'search')
# Sending Keyboard input to selenium
search.send_keys("Python")
search.send_keys(Keys.ENTER)