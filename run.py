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
        self.assertEqual(self.new_account.passtight, "qwe12pr")

    def test_save_details(self):
        self.new_credentials.save_details()
        self.assertEquals(len(User.User_list), 1)


    def test_save_account(self):
        self.new_account.save_account()
        self.assertEquals(len(Account.account_list), 1)
    
    def tearDown(self):
        Account.account_list = []
    
    def test_multiple_save(self):
        self.new_credentials.save_details()
        test_credential = User("Kraft" "facebook", "123456py")
        test_credential.save_details()
        self.assertEqual(len(User.User_list), 2)

    


    






if __name__ == '__main__':
    unittest.main()