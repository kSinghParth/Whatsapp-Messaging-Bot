from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path=r'/Users/parthsingh/Developer@blackbitch_48/chromedriver')

driver.get('https://web.whatsapp.com')
#time.sleep(20)
input("Input when logged in")
print("Starting search")
inp_xpath_search = '///*[@id="site-content"]/div[4]/div/div/div'
search=driver.find_element(by=By.XPATH, value=inp_xpath_search)
time.sleep(3)
search.click()
time.sleep(3)
print("waiting done")

text="Hey, this is Parth. I got your contact from the USC CS Spring 2020 admits group. I am an incoming Spring 2022 USC student looking for off-campus housing. Please let us know if you or any of your friends are leasing/subleasing an apartment/room. Would really appreciate the help."
with open('numbers', 'r') as numbers:
    nums= numbers.readlines()
    for n in nums:
        contact=n.strip()[1:-2].strip()
        #contact='Gandarhv'
        #print(n.strip()[1:-1])
        search.send_keys(contact)
        time.sleep(3)
        driver.find_element(By.XPATH,'//span[@class="_3q9s6"]/span[@title="'+contact+'"]/span[@class="matched-text i0jNr"]').click()
        time.sleep(3)
        message = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        time.sleep(3)
        message.send_keys(text +Keys.ENTER)
        #driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div[2]').click()
        time.sleep(3)
        search.clear()
print("Ending...")
