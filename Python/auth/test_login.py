from selenium import webdriver
from pages.login import LoginPage
import time

import unittest

class LoginTestCase(unittest.TestCase):
    
    def test_userLogin(self):
        self.login_page = LoginPage()
        user = 'registeredUser'
        password = '1234'
        self.login_page.log_in_as(user, password)

        welcome_message = self.login_page.get_auth_message()
        self.assertIn('Welcome back', welcome_message.text)

        self.login_page.quit()

    def test_loginFail(self):
        self.login_page = LoginPage()

        user = 'otherUser'
        password = 'asdf'
        self.login_page.log_in_as(user, password)

        message = self.login_page.get_auth_message()
        self.assertIn('Account not found', message.text)

        self.login_page.click_register_link()
        header = self.login_page.get_page_header()
        self.assertIn('Create an Account', header.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)