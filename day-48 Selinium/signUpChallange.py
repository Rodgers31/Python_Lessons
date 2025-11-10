from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Jonny')
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Test')
email = driver.find_element(By.NAME, 'email')
email.send_keys('jonnytest@yahoo.com')

submit = driver.find_element(By.CLASS_NAME, 'btn-block')
submit.click()







