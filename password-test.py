import unittest
from password import User
import pyperclip
from password import Account


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_credentials = User("Rovet", "facebook", "wwww45")
        self.new_account = Account("clent", "iurt45")

    def tearDown(self):
        User.User_list = []
        Account.account_list = []

    def test_init(self):
        """
        test init help test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.username, "rovel")
        self.assertEqual(self.new_credentials.account, "facebook")
        self.assertEqual(self.new_credentials.passwords, "wwww45")
        self.assertEqual(self.new_account.name, "clent")
        self.assertEqual(self.new_account.passright, "iurt45")

    def test_save_details(self):
        self.new_credentials.save_details()
        self.assertEqual(len(User.User_list), 1)

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list), 1)

    def test_multiple_saves(self):
        self.new_credentials.save_details()
        test_credential = User("kent", "twitter", "1234ae")
        test_credential.save_details()
        self.assertEqual(len(User.User_list), 2)

    def test_multiple_saves(self):
        self.new_account.save_account()
        test_account = Account("Dan", "12jt3er")
        test_account.save_account()
        self.assertEqual(len(Account.account_list), 2)

    def test_delete_credentials(self):
        self.new_credentials.save_details()
        test_credential = User("ken", "intagram", "iii111")
        test_credential.save_details()
        self.new_credentials.delete_credential()
        self.assertEqual(len(User.User_list), 1)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("joice", "@12rews")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list), 1)

    def test_find_credentials_by_account(self):
        self.new_credentials.save_details()
        test_credentials = User("joz", "whatsapp", "1234567@")
        test_credentials.save_details()
        found_account = User.find_by_account("whatsapp")
        self.assertEqual(found_account.passwords, test_credentials.passwords)

    def test_credentials_exists(self):
        self.new_credentials.save_details()
        test_credentials = User("me", "linkedIn", "12@12")
        test_credentials.save_details()
        credentials_exists = User.credentials_exists("linkedIn")
        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        self.assertEqual(User.display_credentials(), User.User_list)

    def test_copy_passwords(self):
        """
        this method tests coping the password to clip board
        """
        self.new_credentials.save_details()
        User.copy_passwords("facebook")
        self.assertEqual(self.new_credentials.passwords, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()