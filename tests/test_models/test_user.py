#!/usr/bin/python3
"""
We test the User now
"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ Test the user in this class"""

    test = User()
    test.first_name = "Betty"
    test.last_name = "Bar"
    test.email = "airbnb@email.com"
    test.password = "root"

    def test_email(self):
        self.assertEqual(test.email, "airbnb@email.com")

    def test_password(self):
        self.assertEqual(test.password, "root")

    def test_first_name(self):
        self.assertEqual(test.first_name, "Betty")

    def test_last_name(self):
        self.assertEqual(test.last_name, "Bar")
