from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

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
browswer.switch_to.frame(browswer.find_element_by_id("main-frame-if"))
# browser.find_element_by_value(" ダウンロード ").click()
# browswer.find_element_by_xpath("//input[@type='submit' and @value=' ダウンロード ']").click()
# browswer.find_element_by_id("rishuReferForm").click()
time.sleep(5)

ActionChains(browswer).click(browswer.find_element_by_xpath("//input[@type='submit' and @role='button' and @value=' ダウンロード ']")).perform()
print("success")

