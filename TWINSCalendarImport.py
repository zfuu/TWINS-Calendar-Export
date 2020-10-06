from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys

import csv

import time
import module_locator
import os


MY_PATH = module_locator.module_path()
CHROMEDRIVER_PATH = MY_PATH + "/lib/chromedriver"
DOWNLOAD_PATH = MY_PATH + "/data"

# username = input("USERNAME: ")
# password = input("PASSWORD: ")

def ImportCalendarFromTWINS(usrname, psw):
    username = usrname
    password = psw
    print("Logging into TWINS as %s to download course registrations..." %username)

    options = Options()
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
    WebDriverWait(browswer, 5).until(EC.url_changes(current_url))
    browswer.find_element_by_xpath("//img[@src='/campusweb/theme/default/newportal/image/icon/note.png']").click()
    browswer.switch_to.frame(browswer.find_element_by_id("main-frame-if"))
    button = browswer.find_element_by_xpath("//input[@type='submit' and @role='button' and @value=' ダウンロード ']")
    button.send_keys(Keys.ENTER)
    downloadButton = browswer.find_element_by_xpath("//input[@id='button1' and @type='button']")
    downloadButton.send_keys(Keys.ENTER)

    # print(len([f for f in os.listdir(DOWNLOAD_PATH) if not f.startswith('.')]))
    #Make sure there is a downloaded file under the directory (exclude hidden sys files)
    while len([f for f in os.listdir(DOWNLOAD_PATH) if not f.startswith('.')]) == 0:
        time.sleep(1)


    print("Successfully downloaded course registration information")


def ParseCSVData():
    CSVFile = [f for f in os.listdir(DOWNLOAD_PATH) if not f.startswith('.')][0]
    CSV_PATH = os.path.join(DOWNLOAD_PATH, CSVFile)

    with open(CSV_PATH, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = [i for sublist in data for i in sublist]

    print("Here are the courses you registered: " + ", ".join(data))
    return data










