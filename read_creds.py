from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()

config_object.read("config.ini")

#Get the password
userinfo = config_object["USERINFO"]

def get_username ():
    return userinfo["username"]

def get_password ():
    return userinfo["password"]

def get_mobile ():
    return  userinfo["mobile"]


# If you want to write to a config before reading from it

# config_object["USERINFO"] = {
#     "username": "",
#     "password": "",
#     "mobile": ""
# }
#
# with open('config.ini', 'w') as conf:
#     config_object.write(conf)