from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1?crid=1WRRLLTREJY6H&dib=eyJ2IjoiMSJ9.fEl4JgiOQvhlWqehbRqySBr7znlnOlG-oPcuuMlHad8GAnMD6WUgpxGrVVI5Eo9wtzhy4t1LAYXNrk15zbxzYcsYFZ39aE_D4zTmIoDizhrScC9IMMcGhCPCG310mmo0fidt43m8pE9NG7k9Y2dLv-ioVd9vqsr1fpz34oP9O_w-NOCbqjy8NeNu_2VRMnWuuwcRLZ6AokxfhOnPbHJm-NATSuC1n3yvya5yNAva5rw.cUdt5OgoPvdidrk2MsbRrdXuBKlBAKhDPg7Qncimj1c&dib_tag=se&keywords=instant%2Bpot&qid=1762641420&sprefix=insta%2Caps%2C96&sr=8-1&th=1")
driver.get("https://www.python.org/")
# price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# price_cent = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
# print(f"The price is {price_dollar}.{price_cent}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, 'submit')
print(button.size)
# find and link nested
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f'Link is: ', bug_link.text)
# Close a single browser
# driver.close()

# Quite all browser
driver.quit()