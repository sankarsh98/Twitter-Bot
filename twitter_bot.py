
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# path to chrome driver, download it from https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_driver = "/chromedriver"


class TwitterBot:

    def __init__(self,username,password,mobile):
        self.browser=webdriver.Chrome(chrome_driver)
        self.username=username
        self.password=password
        self.mobile=mobile

    # signin to the account
    def signIn(self):

        self.browser.get("https://www.twitter.com/login")
        time.sleep(5)
        usernameInput = self.browser.find_element(By.NAME,'text')
        usernameInput.send_keys(self.username)
        time.sleep(3)

        self.browser.maximize_window()

        nextButton1 = self.browser.find_element(By.XPATH,'//span[.="Next"]')
        nextButton1.click()
        time.sleep(3)

        try:
            middleInput = self.browser.find_element(By.NAME,'text')
            middleInput.send_keys(self.mobile)
            time.sleep(3)
            nextButton2 = self.browser.find_element(By.XPATH,'//span[.="Next"]')
            
            nextButton2.click()
            time.sleep(3)
        except NoSuchElementException as nsee:
            print ("exception : ",nsee)

        passwordInput = self.browser.find_element(By.XPATH,'//input[@name="password"]')
        passwordInput.send_keys(self.password)
        # passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        loginButton = self.browser.find_element(By.XPATH,'//span[.="Log in"]')
        loginButton.click()


    def TweetSomething(self, message):

        time.sleep(5)
        tweet_button = self.browser.find_element(By.XPATH,'//a[@aria-label="Tweet"]')
        tweet_button.click()

        tweet_text = self.browser.find_element(By.XPATH,'//div[@aria-label="Tweet text"]')
        tweet_text.send_keys(message)

        tweet = self.browser.find_element(By.XPATH,'//span[.="Tweet"]')
        tweet.click()
