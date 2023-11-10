#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from console import HBNBCommand
import os
import sys
from io import StringIO
from unittest.mock import patch


class prompt_test(unittest.TestCase):
    def prompt_display(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def empty_line_display(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def capture_output(self):
        self.held_output = StringIO()
        self.held_output_context = patch("sys.stdout", self.held_output)
        self.held_output_context.start()

    def release_output(self):
        self.held_output_context.stop()
        output = self.held_output.getvalue().strip()
        self.held_output.close()
        return output

    def test_create_command(self):
        with patch("sys.stdin", StringIO("create BaseModel\n")):
            self.capture_output()
            self.console.cmdloop()
            output = self.release_output()
        self.assertIn("BaseModel", output)
        self.assertIn("13e854e3-9f1b-4c39-837e-3710086490ad", output)


if __name__ == "__main__":
    unittest.main()
