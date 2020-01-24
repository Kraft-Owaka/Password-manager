import math
import random
import pyperclip

class User(object):
    User_list=[]

    def __init__(self, username, account, passwords):
        self.username = username
        self.passwords = passwords
        self.account = account


    def save_details(self):
        User.User_list.append(self)

    def delete_credential(self):
        User.User_list.remove(self)
 

    

    

    class Account(object):
        account_list = []
        def __init__(self, name, passrights)
            self.name = NameError
            self.passrights = passrights

        def save_account(self):
            Account.account_list.append(self)

        def delete_account(self):
            Account.account_list.remove(self)



    

