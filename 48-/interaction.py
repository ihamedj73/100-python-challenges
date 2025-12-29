from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

# article_count = driver.find_element(
#     By.CSS_SELECTOR, value="#articlecount a")

# # article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="fName")

first_name.send_keys("Hamed")
last_name.send_keys("Jahangiry")
email.send_keys("hamed@exampel.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
