# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver

class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
