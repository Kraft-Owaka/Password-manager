import string
import random
from password import User
from password import Account

def create_credentials(username, account, passwords):
    """
    used to create credential account
    """
    new_credentials = User(username, account, passwords)
    return new_credentials

def create_account(name, passrights):
    new_account = Account(name, passrights)
    return new_account

def save_account(account):
    account.save_account()

def delete_account(account):
    account.delete_account()

def save_details(credentials):
    credentials.save_details()

def delete_credential(credentials):
    credentials.delete_credentials()

def display_credentials():
    return User.display_credentials()

def credential_exists(string):
    return User.credentials_exists(string)

def find_by_account(string):
    return User.find_by_account(string)
