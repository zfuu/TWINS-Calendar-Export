from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys


import module_locator
import time


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)



MY_PATH = module_locator.module_path()
CHROMEDRIVER_PATH = MY_PATH + "/lib/chromedriver"
DOWNLOAD_PATH = MY_PATH + "/data"

username = input("USERNAME: ")
password = input("PASSWORD: ")

print("Logging into TWINS as %s to download course registrations..." %username)

options = Options()
# options.add_argument("download.default_directory=" + DOWNLOAD_PATH)

prefs = {'download.default_directory' : DOWNLOAD_PATH}
options.add_experimental_option('prefs', prefs)

# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-startup-window")

browswer = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
browswer.get("https://twins.tsukuba.ac.jp/")

current_url = browswer.current_url
usernameInput = browswer.find_element_by_name("userName")
usernameInput.send_keys(username)
passwordInput = browswer.find_element_by_name("password")
passwordInput.send_keys(password)
passwordInput.submit()
# time.sleep(5)
WebDriverWait(browswer, 5).until(EC.url_changes(current_url))
# current_url = browswer.current_url
browswer.find_element_by_xpath("//img[@src='/campusweb/theme/default/newportal/image/icon/note.png']").click()
# WebDriverWait(browswer, 5).until(EC.url_changes(current_url))
browswer.switch_to.frame(browswer.find_element_by_id("main-frame-if"))
# browser.find_element_by_value(" ダウンロード ").click()
# browswer.find_element_by_xpath("//input[@type='submit' and @value=' ダウンロード ']").click()
# browswer.find_element_by_id("rishuReferForm").click()
# time.sleep(5)
button = browswer.find_element_by_xpath("//input[@type='submit' and @role='button' and @value=' ダウンロード ']")
# ActionChains(browswer).click(button).perform()
# highlight(button)
button.send_keys(Keys.ENTER)
# browswer.switch_to.frame(browswer.find_element_by_id("main-frame-if"))
downloadButton = browswer.find_element_by_xpath("//input[@id='button1' and @type='button']")
# highlight(downloadButton)
downloadButton.send_keys(Keys.ENTER)
print("success")



