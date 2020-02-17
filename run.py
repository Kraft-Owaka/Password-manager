#!/usr/bin/env python3.7

import string
import random
from password import User
from password import Account


def create_credentials(username, account, passwords):
    """
    this will help create new credentials
    """
    new_credentials = User(username, account, passwords)
    return new_credentials


def create_account(name, passright):
    """
    creating new account
    """
    new_account = Account(name, passright)
    return new_account


def save_account(account):
    """
    helps us save the account details
    """
    account.save_account()


def delete_account(account):
    account.delete_account()


def save_details(credentials):
    """
    function to save the credentials created
    """
    credentials.save_details()


def delete_credential(credentials):
    credentials.delete_credential()


def find_by_account(string):
    return User.find_by_account(string)


def credential_exists(string):
    return User.credentials_exists(string)


def display_credential():
    return User.display_credentials()


def main():
    print("hello welcome to your password locker account, what is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a "
              "credentials, "
              "ex -exit the credentials list, dlc-delete existing account ,ca-create account")
        short_code = input().lower()
        if short_code == 'cc':
            print("new credentials")
            print("-" * 10)
            print("username")
            username = input()
            print("enter the account")
            account = input()
            print("how would you wish to create your password, if generate then select 'g' else select 'c' ?")
            unit = input().upper()
            if unit == 'G':
                print("input your password length required ")
                generated = input()
                length = int(generated)
                char = 'abcdefghijklmnopqrstuvwxyz1234567890'
                password = ''
                for C in range(length):
                    password += random.choice(char)
                print('\n')
                print(f"the password generated is: {password}")
            elif unit == 'C':
                print("enter your password please")
                password = input()
                print('\n')
                print(f"the password created is: {password}")

            save_details(create_credentials(username, account, password))  # creating new credentials

            print('\n')
            print(f"new credentials for {account} is created")
            print('\n')
        elif short_code == 'ca':
            print("enter your name")
            name = input()
            print("enter your password")
            passright = input()
            print(f"account  {name} is created")
            print('\n')
            save_account(create_account(name, passright))  # saves account
            print('\n')
            print("log in to your account, enter your username")
            lname = input()
            print("enter your password")
            pword = input()
            if lname == name and pword == passright:
                print(f"welcome to your account {name}")
            elif lname != name and pword != passright:
                print('\n')
                print("invalid name or password please try again")
                break

        elif short_code == 'dc':
            if display_credential():
                print("here is a list of all your credentials")
                print('\n')

                for credentials in display_credential():
                    print(f"{credentials.username} {credentials.account} {credentials.passwords}")
                print('\n')
            else:
                print('\n')
                print("you don't seem to have any account saved yet")
                print('\n')

        elif short_code == 'dlc':
            print("enter the account you'd love to delete")
            del_account = input()
            if credential_exists(del_account):
                del_account = find_by_account(del_account)
                delete_credential(del_account)
                print("your credentials has been deleted")
                print('\n')
            else:
                print("credentials doesnt exist")

        elif short_code == 'fc':
            print("enter the account you want to search for")
            credentials_search = input()
            if find_by_account(credentials_search):
                search_credentials = find_by_account(credentials_search)
                print(f"{search_credentials.username} {search_credentials.account} {search_credentials.passwords}")
                print('_' * 20)

            else:
                print("credentials doesnt exist")

        elif short_code == 'ex':
            print("bye....")

            break
        else:
            print("I didn't quite catch that please use the short codes provided")


if __name__ == '__main__':
    main()