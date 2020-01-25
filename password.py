import math
import random
import pyperclip

class User(object):
    User_list = []

    def __init__(self, username, account, passwords):
        self.username = username
        self.passwords = passwords
        self.account = account


    def save_details(self):
        User.User_list.append(self)

    def delete_credential(self):
        User.User_list.remove(self)

    """
    code to make the tests pass
    """
@classmethod
def find_account(cls, string):
    for credentials in cls.User_list:
        if credentials.account == string:
            return credentials
@classmethod
def credentials_exists(cls, string):
    for credentials in cls.User_list:
        if credentials.account == string:
            return True
    return False
@classmethod
def display_credentials(cls):
    return cls.User_list

@classmethod
def copy_passwords(cls, string):
    password_found = User.find_by_account(string)
    pyperclip.copy(password_found.passwords)

class Account(object):
    account_list = []

    def __init__(self, name, passright):
        self.name = name
        self.passrights = passright
    def save_account(self):
        Account.account_list.append(self)

    def delete_account(self):
        Account.account_list.remove(self)


    

    

