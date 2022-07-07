import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

url = input("Enter LinkedIn job url: ")

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.get(url)

signin_btn = driver.find_element("link text", "Sign in")
signin_btn.click()

time.sleep(3)

email = driver.find_element("css selector", "#username")
email.send_keys(MY_EMAIL)
password = driver.find_element("css selector", "#password")
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(10)

get_all_jobs = driver.find_elements("css selector", ".job-card-container--clickable time")

for job in get_all_jobs:
    job.click()
    time.sleep(3)
    try:
        save_button = driver.find_element("css selector", ".jobs-unified-top-card .jobs-save-button")
    except NoSuchElementException:
        continue
    except StaleElementReferenceException:
        continue
    else:
        save_button.click()
    finally:
        time.sleep(2)
        close = driver.find_element("css selector", ".artdeco-toasts_toasts button")
        close.click()
    time.sleep(2)

time.sleep(5)
driver.quit()
