#!/usr/bin/python3
""" unittests for models/engine/file_storage.py."""

import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_file_storage(unittest.TestCase):
    """Unittests for the file storage."""

    @classmethod
    def setUpClass(__class):
        __class.file_path = "file.json"
        __class.objects = FileStorage._FileStorage__objects

    @classmethod
    def tearDownClass(__class):
        try:
            os.remove(__class.file_path)
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(self.objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_save(self):
        models.storage.new(BaseModel())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel.", save_text)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_user(self):
        models.storage.new(User())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("User.", save_text)

    def test_save_state(self):
        models.storage.new(State())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("State.", save_text)

    def test_save_place(self):
        models.storage.new(Place())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("Place.", save_text)

    def test_save_city(self):
        models.storage.new(City())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("City", save_text)

    def test_save_amenity(self):
        models.storage.new(Amenity())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("Amenity.", save_text)

    def test_save_review(self):
        models.storage.new(Review())
        models.storage.save()
        with open(self.file_path, "r") as f:
            save_text = f.read()
            self.assertIn("Review.", save_text)


if __name__ == "__main__":
    unittest.main()
