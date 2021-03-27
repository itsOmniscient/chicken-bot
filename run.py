from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import re
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
firefox_path = os.getenv("FIREFOX")

print("https://golden-farm.biz/, Automation tool")
email_input = input("Email: ")
password_input = input("Password: ")

options = Options()
options.add_argument("--headless")
print("Starting the webdriver, please wait...")
fp = webdriver.FirefoxProfile(firefox_path)
driver = webdriver.Firefox(fp, options=options)

def wait():
    WebDriverWait(driver, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

def check_silver():
    driver.find_element_by_xpath('//*[@id="m1"]/div[4]/a').click()
    wait()
    silver_element = driver.find_element_by_xpath('//*[@id="content_s"]/div[2]/table/tbody/tr[5]/td[2]/font')
    silver_element_text = silver_element.text
    reg = re.compile('[0-9]+\S[0-9]+')
    reg_list = reg.findall(silver_element_text)
    global silver
    silver = int(float(reg_list[0]))
    driver.find_element_by_xpath('//*[@id="a1"]').click()

driver.get("https://golden-farm.biz")
wait()
print("Logging in, please wait...")
email = driver.find_element_by_name("log_email")
email.send_keys(email_input)
password = driver.find_element_by_name("pass")
password.send_keys(password_input)
time.sleep(1)
driver.find_element_by_id("btn_login").click()
wait()
try:
    driver.find_element_by_id("a2").click()
    print("Login successful.")
except:
    print("Wrong username/password OR captcha detected, exiting...")
    driver.quit()
    sys.exit()
wait()
driver.find_element_by_name("collect").click()
print("Eggs collected.")
wait()
driver.find_element_by_id("a3").click()
wait()
driver.find_element_by_name("sell").click()
print("Eggs sold.")
wait()
driver.find_element_by_xpath('//*[@id="m2"]/div[5]/a').click()
wait()
try:
    driver.find_element_by_name('bonus').click()
    print("Daily bonus collected.")
except:
    hours = driver.find_element_by_xpath('//*[@id="content_s"]/div[2]/center/div/div/span[1]')
    minutes = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/center/div/div/span[2]')
    seconds = driver.find_element_by_xpath('//*[@id="content_s"]/div[2]/center/div/div/span[3]')
    msg = f'Daily bonus already collected. You can collect your bonus again in {hours.text} hours {minutes.text} minutes {seconds.text} seconds.'
    print(msg)
wait()
check_silver()
print("You have " +str(silver) +" silver coins.")
if silver < 150:
    print("Not enough points to buy any birds, exiting...")
    driver.quit()
    sys.exit()
print("Buying birds, please wait...")
while silver >= 150:
    if silver >= 375000:
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[7]/form/div[2]/input[2]').clear()
        king_bird_pcs = driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[7]/form/div[2]/input[2]')
        king_bird_pcs.send_keys(int(silver/375000))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[7]/form/div[2]/button').click()
        wait()
    elif silver >= 150000:
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[6]/form/div[2]/input[2]').clear()
        red_bird_pcs = driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[6]/form/div[2]/input[2]')
        red_bird_pcs.send_keys(int(silver/150000))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[6]/form/div[2]/button').click()
        wait()
    elif silver >= 37500:
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[5]/form/div[2]/input[2]').clear()
        blue_bird_pcs = driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[5]/form/div[2]/input[2]')
        blue_bird_pcs.send_keys(int(silver/37500))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[5]/form/div[2]/button').click()
        wait()
    elif silver >= 7500:
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[4]/form/div[2]/input[2]').clear()
        brown_bird_pcs = driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[4]/form/div[2]/input[2]')
        brown_bird_pcs.send_keys(int(silver/7500))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[4]/form/div[2]/button').click()
        wait()
    elif silver >= 1500:
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[3]/form/div[2]/input[2]').clear()
        yellow_bird_pcs = driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[3]/form/div[2]/input[2]')
        yellow_bird_pcs.send_keys(int(silver/1500))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[3]/form/div[2]/button').click()
        wait()
    else:
        driver.find_element_by_xpath('//*[@id="t_amount_a"]').clear()
        green_bird_pcs = driver.find_element_by_xpath('//*[@id="t_amount_a"]')
        green_bird_pcs.send_keys(int(silver/150))
        driver.find_element_by_xpath('//*[@id="content_s"]/div[3]/div[2]/form/div[2]/button').click()
        wait()
    check_silver()
wait()
print("Successfully bought birds, exiting...")
time.sleep(1)
driver.quit()
