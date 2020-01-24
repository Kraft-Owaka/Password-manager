import math
import random
class User(object):
    list=[]

    def __init__(self,username,email,password):
        self.username=username
        self.email=email


    def save_credential(self):
        User.list.append(self)

    

