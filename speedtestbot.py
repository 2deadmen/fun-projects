from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Speed:
        def __init__(self):
            path = "/development/chromedriver.exe"
            driver = webdriver.Chrome(path)

            driver.get(url="https://www.speedtest.net/")
            go = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a[@role = "button"]')
            go.click()
            time.sleep(60)
            self.down = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            self.down = self.down.text
            print(self.down)
            self.up = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            self.up = self.up.text
            print(self.up)
            driver.quit()
