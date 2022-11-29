#!/usr/bin/python3
"""Test suit for the models"""

import unittest
import os
import re
import uuid
from time import sleep
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """This is just an example TestCase"""

    def test_save(self):
        """First test baby"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """This tests the to_dict method"""
        pass

    def test_id(self):
        """This tests the id"""
        pass
    def test_created_at(self):
        """This tests the format of time"""
        pass
    def test___str__(self):
        """This is to test __str__"""
        pass
    def test___init__(self):
        """This is to test __init__"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

if __name__ == '__main__':
    """not sure"""
    unittest.main()
