from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://192.168.1.1"
chromium_driver_path = "/usr/bin/chromedriver"


service = Service(executable_path=chromium_driver_path)
option = Options()
option.add_argument("--ignore-certificate-errors")
option.add_argument("--headless")
option.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=option)
wait = WebDriverWait(driver, 10)

driver.get(url)
username = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
username.send_keys("admin")
password = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'password')))
password.send_keys("admin")
login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_login')))
login.click()
time.sleep(10)

menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'mobile-btn-menu-img')))
menu.click()

network = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="mobile_Menu_L2_Link" and @routerid="stat.stat2.stat21"]')))
network.click()

time.sleep(5)

lan = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@langid="NAVIGATION_ITEM_NET_LAN"]')))
lan.click()

time.sleep(10)

driver.execute_script("window.scrollBy(0, 1000);")

radio1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='view50_autoDNS1']")))
radio1.click()

save = wait.until(EC.element_to_be_clickable((By.ID, "view60_save")))
save.click()

time.sleep(5)

radio2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='view50_autoDNS2']")))
radio2.click()

save.click()
time.sleep(5)

driver.quit()

