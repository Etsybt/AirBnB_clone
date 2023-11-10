#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
from models.engine.file_storage import FileStorage
import os
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unittests for console.py."""

    @classmethod
    def setUpClass(cls):
        cls.file_path = "file.json"
        cls.objects = FileStorage._FileStorage__objects

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit_and_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertIn(
                    "Documented commands (type help <topic>):", output.getvalue
                    ().strip())

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(test_key, storage.all().keys())

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertEqual("[]", output.getvalue().strip())

    def test_update(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "update BaseModel 1 name John"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
