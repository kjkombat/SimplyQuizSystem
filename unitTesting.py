import unittest
from login import logIn

class TestingSqlMethods(unittest.TestCase):
    def testlogin(self):
        test = logIn()
        test.checkEntry()