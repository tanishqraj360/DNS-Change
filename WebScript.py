from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Update this path to point to your Chromium WebDriver
chromium_driver_path = "/usr/lib/chromium-browser/chromedriver"

service = Service(executable_path=chromium_driver_path)
option = Options()
option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=service, options=option)
driver.maximize_window()

def login(url, username_class, username, password_class, password, submit_button_class):
    driver.get(url)
    driver.find_element(By.CLASS_NAME, username_class).send_keys(username)
    driver.find_element(By.CLASS_NAME, password_class).send_keys(password)
    driver.find_element(By.CLASS_NAME, submit_button_class).click()

login("http://192.168.1.1", "username", "admin", "password", "admin", "btn_login")
driver.find_element(By.CLASS_NAME, "Menu_L2_Link").click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "label[for='view50_autoDNS1']").click() 
driver.find_element(By.ID, "view60_save").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "label[for='view50_autoDNS2']").click() 
driver.find_element(By.ID, "view60_save").click()
time.sleep(5)

driver.quit()
