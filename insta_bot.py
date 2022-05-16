from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
path = "/development/chromedriver.exe"
driver = webdriver.Chrome(path)
target ="rock"
phone="your insta id"
password="7338210933"
class Follower:
    def __init__(self):
        driver.get(url="https://www.instagram.com/")
        time.sleep(3)
    def login(self):

        name = driver.find_element(By.NAME,"username")
        name.send_keys(phone)
        passcode =driver.find_element(By.NAME,"password")
        passcode.send_keys(password)
        login = driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(4)
    def findtarget(self):

        search = driver.find_element(By.XPATH,value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(target)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            tap = driver.find_element(By.XPATH,value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
            tap.click()
            time.sleep(3)
        except:
            tap = driver.find_element(By.XPATH,
                                      value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
            tap.click()
            time.sleep(3)
    def follow(self):
        followers=driver.find_element(By.XPATH,value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        # tab =driver.window_handles[1]
        # driver.switch_to.window(tab)
    def loop(self):
        time.sleep(2)
        following = driver.find_elements(By.CSS_SELECTOR, 'li button')

        for n in range(100):
            following = driver.find_elements(By.CSS_SELECTOR, 'li button')
            for i in following:

                try:
                    i.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                    cancel_button.click()
        self.loop()
follow=Follower()
follow.login()
follow.findtarget()
follow.follow()
follow.loop()
#driver.quit()