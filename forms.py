import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
path = "/development/chromedriver.exe"
driver = webdriver.Chrome(path)
forms = "https://docs.google.com/forms/d/e/1FAIpQLSdx_CUL-9m3qSRKkXypA6dMK4YcfN880KsYjQ2sENSHorf-rg/viewform?usp=sf_link"

class Forms:
    def upload(self,a,b,c):
        driver.get(url=forms)
        for i in range(len(a)):
            try:
                address = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                address.click()
                time.sleep(1)
                address.send_keys(a[i])
            except ElementClickInterceptedException:
                address = driver.find_element(By.XPATH,
                                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                address.send_keys(a[i])
            price= driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(b[i])
            link = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(c[i])
            submit= driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.click()
            time.sleep(2)
            another = driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another.click()
            time.sleep(2)
        driver.quit()



