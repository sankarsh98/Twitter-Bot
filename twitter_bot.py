
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# path to chrome driver, download it from https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_driver = "/Users/sanky/Downloads/chromedriver"


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
        usernameInput = self.browser.find_element_by_name('text')
        usernameInput.send_keys(self.username)
        time.sleep(3)

        self.browser.maximize_window()

        nextButton1 = self.browser.find_element_by_xpath('//span[.="Next"]')
        nextButton1.click()
        time.sleep(3)

        try:
            middleInput = self.browser.find_element_by_name('text')
            middleInput.send_keys(self.mobile)
            time.sleep(3)
            nextButton2 = self.browser.find_element_by_xpath('//span[.="Next"]')
            nextButton2.click()
            time.sleep(3)
        except NoSuchElementException:
            print ("exception")

        passwordInput = self.browser.find_element_by_xpath('//input[@name="password"]')
        passwordInput.send_keys(self.password)
        # passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        loginButton = self.browser.find_element_by_xpath('//span[.="Log in"]')
        loginButton.click()


    def TweetSomething(self, message):

        time.sleep(5)
        tweet_button = self.browser.find_element_by_xpath('//span[.="Tweet"]')
        tweet_button.click()

        tweet = self.browser.find_element_by_xpath('//div[@aria-label="Tweet text"]')
        tweet.send_keys(message)
        tweet.send_keys(Keys.COMMAND, Keys.ENTER)
