#!/usr/bin/python3
import unittest
import os
from datetime import datetime
import models
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_instantiation(self):
        self.assertEqual(BaseModel, type(self.base_model))
        self.assertIn(self.base_model, models.storage.all().values())
        self.assertEqual(str, type(self.base_model.id))
        self.assertEqual(datetime, type(self.base_model.created_at))
        self.assertEqual(datetime, type(self.base_model.updated_at))
        self.assertNotEqual(BaseModel().id, BaseModel().id)
        self.assertLess(BaseModel().created_at, BaseModel().updated_at)
        self.assertEqual("[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__), str(
                self.base_model))

    def test_args_and_kwargs(self):
        time = datetime.today()
        time_iso = time.isoformat()
        base_model = BaseModel(
                "12", id="345", created_at=time_iso, updated_at=time_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, time)
        self.assertEqual(base_model.updated_at, time)

    def test_save(self):
        first_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertLess(first_updated_at, self.base_model.updated_at)

    def test_save_updates_file(self):
        self.base_model.save()
        base_model_id = "BaseModel." + self.base_model.id
        with open("file.json", "r") as f:
            self.assertIn(base_model_id, f.read())

    def test__dict(self):
        time = datetime.today()
        self.base_model.id = "68887"
        self.base_model.created_at = self.base_model.updated_at = time
        __dict = {
            'id': '68887',
            '__class__': 'BaseModel',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(self.base_model.to_dict(), __dict)


if __name__ == "__main__":
    unittest.main()
