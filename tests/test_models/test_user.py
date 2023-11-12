#!/usr/bin/python3
"""tests for user.py"""
import os
import models
import unittest
from datetime import datetime, timedelta
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """unittest for user"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())

    def test_to_dict_datetime_attributes_are_strs(self):
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
            }
        self.assertEqual(us.to_dict()['id'], tdict['id'])
        self.assertEqual(us.to_dict()['__class__'], tdict['__class__'])
        self.assertAlmostEqual(
                datetime.strptime(
                    us.to_dict()['created_at'], '%Y-%m-%dT%H:%M:%S.%f'),
                datetime.strptime(tdict['created_at'], '%Y-%m-%dT%H:%M:%S.%f'),
                delta=timedelta(milliseconds=1)
                )
        self.assertAlmostEqual(
                datetime.strptime(
                    us.to_dict()['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'),
                datetime.strptime(tdict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'),
                delta=timedelta(milliseconds=1)
                )


if __name__ == "__main__":
    unittest.main()
