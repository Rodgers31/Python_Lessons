import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# Global flag to control the main loop
running = True


def count_down(seconds):
    global running
    for i in range(seconds, 0, -1):
        print(f'Time left: {i}s')
        time.sleep(1)
    cookies_per_sec = driver.find_element(By.CSS_SELECTOR, '#cookiesPerSecond')
    cookies_per_sec = cookies_per_sec.text.split(" ", 2)[-1]
    print(f'cookies/second: {cookies_per_sec}')
    running = False  # Stop the main loop after countdown


def check_help():
    print('Checking for upgrades...')
    cursor = driver.find_element(By.CSS_SELECTOR, '#productPrice0')
    grandma = driver.find_element(By.CSS_SELECTOR, '#productPrice1')
    farm = driver.find_element(By.XPATH, '//*[@id="productPrice2"]')

    find_cookies = driver.find_element(By.CSS_SELECTOR, '#cookies')
    num_cookies = find_cookies.text.split(" ")[0].replace(',', '')

    cursor_div = driver.find_element(By.CSS_SELECTOR, '#product0')
    grandma_div = driver.find_element(By.CSS_SELECTOR, '#product1')
    farm_div = driver.find_element(By.CSS_SELECTOR, '#product2')
    farm_value = farm.text.replace(',', '').strip()

    print(f'Cookies: {int(num_cookies)}')
    if int(num_cookies) > 15:
        if farm_value and int(num_cookies) >= int(farm_value):
            farm_div.click()
        elif grandma.text and int(num_cookies) >= int(grandma.text.replace(',', '')):
            grandma_div.click()
        elif cursor.text and int(num_cookies) >= int(cursor.text.replace(',', '')):
            cursor_div.click()


driver.get('https://ozh.github.io/cookieclicker/')

driver.implicitly_wait(4)
select_lan = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
hover = ActionChains(driver).move_to_element(select_lan)
hover.perform()
select_lan.click()
driver.implicitly_wait(2)
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
cookie_hover = ActionChains(driver).move_to_element(cookie)
driver.implicitly_wait(1)
cookie_hover.perform()

# Start countdown timer (5 minutes)
countdown_thread = threading.Thread(target=count_down, args=(60 * 5,), daemon=True)
countdown_thread.start()

last_check_time = time.time()
while running:
    click_co = driver.find_element(By.CSS_SELECTOR, 'div #cookieAnchor button')
    click_co.click()
    time.sleep(.05)

    # Check for upgrades every 5 seconds
    if time.time() - last_check_time >= 5:
        check_help()
        last_check_time = time.time()

# driver.quit()
