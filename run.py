import unittest
from password import User 
import pyperclip
from password import Account

class TeatUser(unittest.TestCase):#create subclass to inherit from unittest.TestCase

    def setup(self):
        self.new_credentials = User("Owaka", "twitter", "pass@987ko")# create contact object
        self.new_account = Account("Kraft", "qwe12pr")

    def test_init(self):
        self.assertEqual(self.new)


    






if __name__ == '__main__':
    unittest.mail())