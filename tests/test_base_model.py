#!/usr/bin/python3
"""a test module for a base model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestingBase(unittest.TestCase):
    """a unittest class for base model"""

    def test_no_arguments(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_base_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)


if __name__ == "__main__":
    unittest.main()
