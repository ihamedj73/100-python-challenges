
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By


# click on the cookie
# select language
# check every 5 sec  right-hand pane see which upgrades  affordable  purchase the most expensive.
# After 5 min stop the bot and print the "cookies/second

driver = webdriver.Firefox()
# driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.get("https://ozh.github.io/cookieclicker/")


time.sleep(2)
browser_cookie_link = driver.find_element(
    By.CLASS_NAME, value="cc_btn_accept_all")
browser_cookie_link.click()

time.sleep(2)
select_en = driver.find_element(By.ID, value="langSelect-EN")
select_en.click()

time.sleep(2)
browser_cookie_link = driver.find_element(
    By.CLASS_NAME, value="cc_btn_accept_all")
browser_cookie_link.click()

# there is 20 product from 0 to 19
# active products list last one is the most value one

time.sleep(1)

products = []
for i in range(20):
    product = driver.find_element(By.ID, value=f"product{i}")
    products.append(product)
    # print(product.get_attribute("class"))
cookie_button = driver.find_element(By.ID, value="bigCookie")


def check_for_upgrades():
    active_products = []
    for product in products:
        product_classes = product.get_attribute("class")
        if "enabled" in product_classes:
            active_products.append(product)
    if len(active_products) > 0:
        active_products[-1].click()
        print(len(active_products))


start_time = datetime.now()
end_time = start_time + timedelta(minutes=5)
start_check = start_time + timedelta(seconds=5)
while datetime.now() <= end_time:
    cookie_button.click()
    if datetime.now() >= start_check:
        check_for_upgrades()
        start_check = datetime.now() + timedelta(seconds=5)

cookie_per_second = driver.find_element(By.ID, value="cookiesPerSecond")
print(f"cookies/second: {cookie_per_second.text.split()[-1]}")

# driver.quit()
