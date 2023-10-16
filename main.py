from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = INSTA_ACCOUNT
EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD
USERNAME = YOUR_USERNAME
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        log_in.click()
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(EMAIL)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(10)

    def follow(self):
        for i in range(1,50):
            all_buttons = self.driver.find_element(By.XPATH, f'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button/div')
            try:
                all_buttons.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '')
                cancel_button.click()


insta_follower = InstaFollower()
insta_follower.login()
time.sleep(20)
insta_follower.find_followers()
insta_follower.follow()
