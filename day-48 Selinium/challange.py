from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

# this will create a nested object counting from zero for each event
user_event = {i: {'Date': time.text, 'Name': name.text}for i, (time, name) in enumerate(zip(event_time, event_name))}

# simpler version
events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text,
    }

print(user_event)
print(events)

# Quite all browser
driver.quit()