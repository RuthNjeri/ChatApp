# test_chat_app.py

import unittest

#import local files
from users.py import Userclass

class UserTestCase(unittest.TestCase):
    """
    Class for testing users
    """
    def setUp(self):
        """
        store data for tests
        """
        pass

    def test_user_can_register(self):
        """
        Test if a user can register
        """
        pass

    def test_user_can_login(self):
        """
        Test if a user can login on the app
        """

    def test_user_can_log_out(self):
        """
        Test if a user can logout when logged in
        """

    def test_user_can_create_comment(self):
        """
        Test if a user can create a comment
        """

if __name__=='__main__':
    unittest.main()
    