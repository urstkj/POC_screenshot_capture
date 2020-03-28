from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui,time
driver = webdriver.Firefox()
fh = open('urls.txt')
n=1
driver.get('https://google.com')
for line in fh:
    driver.maximize_window()
    driver.get(line)
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    time.sleep(3)
    pyautogui.screenshot().save("screenshot_"+str(n)+ ".png")
    driver.switch_to_alert().accept()
    time.sleep(3)
    n=n+1
fh.close()
driver.close()