from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import module_locator
import time

MY_PATH = module_locator.module_path()
CHROMEDRIVER_PATH = MY_PATH + "/lib/chromedriver"

username = input("USERNAME: ")
password = input("PASSWORD: ")

print("Logging into TWINS as %s to download course registrations..." %username)

options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")

browswer = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
browswer.get("https://twins.tsukuba.ac.jp/")

current_url = browswer.current_url
usernameInput = browswer.find_element_by_name("userName")
usernameInput.send_keys(username)
passwordInput = browswer.find_element_by_name("password")
passwordInput.send_keys(password)
passwordInput.submit()
# time.sleep(5)
WebDriverWait(browswer, 15).until(EC.url_changes(current_url))
current_url = browswer.current_url
browswer.find_element_by_xpath("//img[@src='/campusweb/theme/default/newportal/image/icon/note.png']").click()
WebDriverWait(browswer, 15).until(EC.url_changes(current_url))
# browswer.find_element_by_xpath("//input[@class='ui-button ui-widget ui-state-default ui-corner-all']")
