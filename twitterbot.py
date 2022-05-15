from speedtestbot import Speed
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Tweet:
    def __init__(self):
        path = "/development/chromedriver.exe"
        driver = webdriver.Chrome(path)
        speed =Speed()
        driver.get(url="https://twitter.com/")
        time.sleep(4)
        try:
         login = driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        except:
            driver.get(url="https://twitter.com/")
            time.sleep(8)
            login = driver.find_element(By.XPATH,
                                        value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')

        login.click()
        # base =driver.window_handles
        # print(base)
        # login =driver.window_handles[1]
        # driver.switch_to.window(login)
        time.sleep(3)
        phone = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        phone.send_keys("8904377382")
        next = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next.click()
        time.sleep(3)
        paasword = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        paasword.send_keys("7338210933")
        submit= driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        submit.click()
        time.sleep(3)
        post = driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        post.send_keys(f"download:{speed.down}and upload:{speed.up}")
        time.sleep(2)
        send = driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send.click()
        time.sleep(10)
        driver.quit()

tweet =Tweet()