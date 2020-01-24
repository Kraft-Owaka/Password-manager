import unittest
from password import User 
import pyperclip
from password import Account

class TeatUser(unittest.TestCase):#create subclass to inherit from unittest.TestCase

    def setup(self):
        self.new_credentials = User("Owaka", "twitter", "pass@987ko")# create contact object
        self.new_account = Account("Kraft", "qwe12pr")

    def test_init(self):
        self.assertEqual(self.new_credentials.username, "Owaka")
        self.assertEqual(self.new_credentials.account, "twitter")
        self.assertEqual(self.new_credentials.password, "pass@987ko")
        self.assertEqual(self.new_account.name, "Kraft")
        self.assertEqual(self.new_account.passrights, "qwe12pr")

    def test_save_details(self):
        self.new_credentials.save_details()
        self.assertEquals(len(User.User_list), 1)


    def test_save_account(self):
        self.new_account.save_account()
        self.assertEquals(len(Account.account_list), 1)
    
    def tearDown(self):
        Account.account_list = []
    
    def test_multiple_saves(self):
        self.new_credentials.save_details()
        test_credential = User("Kraft" "facebook", "123456py")
        test_credential.save_details()
        self.assertEqual(len(User.User_list), 2)

    def test_multiple_saves(self):
        self.new_account.save_account()
        test_account = Account("Femi", "1234kly")
        test_account.test_save_account()
        self.assertEqual(len(Account.account_list), 2)

    def test_delete_credentials(self):
        self.new_credentials.save_details()
        test_credential = User("Kraft","wichat","wiwichch12")
        test_credentials.save_cetails()
        self.new_accounts.test_delete_credential()
        self.assertEquals(len(User.User_list), 1)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("Noah", "yu67yu")
        test_account.save_account()
        self.new_account.test_delete_acount()
        self.assertEquals(len(Account.account_list), 1)

    def test_find_credentials_by_account(self):
        self.new_credentials.save_details()
        test_credentials = User("Joy", "g-mail","hj12345")
        test_credentials.save_details()
        found_account = User.find_by_account("g-mail")
        self.assertEqual(found_account.password, test_credentials.passwords)
        
    def test_credentials_exists(self):
        self.new_credentials.save_details()
        test_credentials = User("Kevin", "Pintrest", "pin@123")
        test_credentials.save_details()
        credentials_exists = User.delete_credentials_exists("pintrest")
        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        self.assertEqual(User.display_credentials(), User.User_list)


    def test_copy_passwords(self):
        self.new_credentials.save_details()
        User.copy_passwords("pintrest")
        self.assertEqual(self.new_credentials.passwords, pyperclip.paste())
    


    

    if __name__ == '__main__':
        unittest.main()