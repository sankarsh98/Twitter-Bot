# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Find reference for this project from https://towardsdatascience.com/how-i-built-a-twitter-bot-using-python-and-selenium-c036bfff6af8

# /Users/sanky/Downloads/chromedriver


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitterBot():
    def __init__(self,username,password):
        self.browser=webdriver.Chrome("/Users/sanky/Downloads/chromedriver")
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.twitter.com/login")
        time.sleep(5)
        # usernameInput=self.browser.find_element_by_name("session[username_or_email]")
        usernameInput = self.browser.find_element_by_name('text')
        # passwordInput=self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        # nextButton = self.browser.find_element_by_xpath ('//div[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
        # nextButton = self.browser.findElement(By.)
        time.sleep(3)
        # nextButton = self.browser.find_element_by_xpath ('//div[@class ="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
        # nextButton = self.browser.find_element_by_xpath('//div[@role="button"][2]')

        nextButton1 = self.browser.find_element_by_xpath('//span[.="Next"]')
        nextButton1.click()
        time.sleep(3)
        middleInput = self.browser.find_element_by_name('text')
        middleInput.send_keys("7842685254")
        time.sleep(3)
        nextButton2 = self.browser.find_element_by_xpath('//span[.="Next"]')
        nextButton2.click()
        time.sleep(3)

        # passwordInput.send_keys(self.password)
        # passwordInput = self.browser.find_element_by_name('password')
        passwordInput = self.browser.find_element_by_xpath('//input[@name="password"]')
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        loginButton = self.browser.find_element_by_xpath('//span[.="Log in"]')
        loginButton.click()

    def TweetSomething(self):
        # tweet = self.browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
        #                                               /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
        #                                               /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
        #                                               /div/div/div''')

        tweet = self.browser.find_element_by_xpath('//div[@class="DraftEditor - editorContainer"]')
        tweet.send_keys("""Hello World!""")
        tweet.send_keys(Keys.COMMAND, Keys.ENTER)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    t = TwitterBot(username, password)
    t.signIn()
    t.TweetSomething()
    # hello



