import math
import random
import pyperclip

class User(object):
    User_list=[]

    def __init__(self, username, account, passwords):
        self.username = username
        self.passwords = passwords
        self.account = account


    def save_credential(self):
        User.User_list.append(self)

    def delete_credential(self):
        User.User_list.remove(self)

    

    

