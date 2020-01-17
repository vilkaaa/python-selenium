import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Python38\\Lib\\site-packages\\chromedriver\\chromedriver.exe')
driver.get("")#our working site
driver.maximize_window()
time.sleep(1)
elem = driver.find_element_by_class_name("loginBtn").click()
time.sleep(1)
elem = driver.find_element_by_name("user_login").send_keys("") #can't say it
elem = driver.find_element_by_name("user_password").send_keys("") #top secret
elem = driver.find_element_by_name("form-auth").submit()
time.sleep(5)
driver.close()
