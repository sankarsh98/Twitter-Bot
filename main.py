
# Find reference for this project from https://towardsdatascience.com/how-i-built-a-twitter-bot-using-python-and-selenium-c036bfff6af8

import read_creds as creds
from twitter_bot import TwitterBot as bot


if __name__ == '__main__':

    # get credentials from config.ini file
    username = creds.get_username()
    password = creds.get_password()
    mobile = creds.get_mobile()

    tweet = input("What do you want to tweet today?")

    #create a twitter_bot object
    tb = bot(username, password,mobile)

    #signing in to twitter
    tb.signIn()

    #tweeting the message
    tb.TweetSomething(tweet)



