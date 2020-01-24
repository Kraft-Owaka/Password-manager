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

def mail():
    print("Hello and to password locker, what is your namw?")
    user_name = input()

    print(f"Hi {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Select a short code : cc - create a new credentials, dc - display credentials, fc - find a credential, ex - exit the credential list, dlc - delete existing account, ca - create account")
        short_code = input().lower()
        if short_code == 'cc':
            print("new credentials")
            print("-" * 10)
            print("username")
            username = input()
            print("enter the account")
            account = input()
            print("To create or generate your passwerd?, if generate then select 'G' else select 'C' ?")
            unit = input().upper()
            if unit == 'G':
                print("Please, inputyour password")
                generated = input()
                length = int(generated)
                char = 'abcdefghijklmnopqrstuvwxyz1234567890'
                password = ''
                for c in range(length):
                    password += random.choice(char)
                print('\n')
                print(f"The password generated is: {password}")
            elif unit == 'C':
                print("Enter your password please")
                password = input()
                print('\n')
                print(f"The password created is: {password}")

            save_details(create_credentials(username, account, password))
            
            print('\n')
            print(f"New credentials from {account} is created")
            print('\n')

        elif short_code == 'ca':
            print("Enter your name")
            name = input()
            print("Enter your password")
            passrights = input()
            print(f"Account {name} is created")
            print('\n')
            save_account(created_account(name, passrights))# for saving accounts
            print('\n')
            print("To log into account, input your username")
            lname = input()
            print("Enter password")
            pword = input()
            if lname == name and pword == passrights:
                print(f"Welcome home {name}")
            elif lname != name and pword != passrights:
                print('\n')
                print("Invalid Name or Password. Make an entry")
                break

            elif short_code == 'dc':
                if display_credentials():
                    print("here is a list og the credentials")
                    print('\n')

                    for credentials in display_credentials():
                        print(f"{credentials.username} {credentials.account} {credentials.passwords}")
                    print('\n')
                else:
                    print('\n')
                    print("you do not have an account saved")
                    print('\n')
                
            elif short_code == 'dlc':
                print("Enter account to be Deleated")
                del_account = input()
                if credential_exists(del_account):
                    del_account = find_by_account(del_account)
                    delete_credential(del_account)
                    print("credentials have been deleted")
                    print('\n')
                else:
                    print("credentials don't exist")
            elif short_code == 'fc':
                print("enter the accountto to be searched")
                credentials_search = input()
                if find_by_account(credentials_search):
                    search_credentials = find_by_account(credentials_search)
                    print(f"{search_credentials.username} {search_credentials.account} {search_credentials.passwords}")
                    print('_' * 20)

                else: 
                    print ()