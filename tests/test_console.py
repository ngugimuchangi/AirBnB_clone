#!/usr/bin/python3
""" Console test module
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
from os import path, remove
from models import storage
from console import HBNBCommand
from unittest import TestCase
from unittest.mock import patch
from re import search


class TestConsole(TestCase):
    """ Test class for Airbnb console
    """
    def setUp(self):
        """ Set up action at the beginning of each test
        """
        self.classes = ["BaseModel", "User", "State", "City", "Amenity",
                        "Place", "Review"]

    def tearDown(self):
        """ Clean up actions at the end of each test
        """
        if path.exists(storage._FileStorage__file_path):
            remove(storage._FileStorage__file_path)

    def test_quit(self):
        """ Test quit method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """ Test EOF method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_help(self):
        """ Test help method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = "{} {}".format("EOF  all  count  create",
                                    "destroy  help quit  show  update")
            self.assertTrue(output, f.getvalue())

    def test_empty_line(self):
        """ Test emptyline method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = HBNBCommand()
            cmd.emptyline()
            self.assertEqual("", f.getvalue())

    def test_create_show_destroy(self):
        """ Test create, show, and destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            for i in self.classes:
                HBNBCommand().onecmd(f"create {i}")
                output = search(r'.*-.*-.*-.*$', f.getvalue())
                self.assertEqual(f"{output.group()}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"show {i} {output.group()}")
                output = search(r'.*-.*-.*-.*$', f.getvalue())
                self.assertEqual(f"{output.group()}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"destroy {i} {output.group()}")
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show BaseModel {output.group()}")
                output = "** no instance found **\n"
                self.assertEqual(output, f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.create()")
                output = search(r'.*-.*-.*-.*$', f.getvalue())
                self.assertEqual(f"{output.group()}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.show({output.group()})")
                output = search(r'.*-.*-.*-.*$', f.getvalue())
                self.assertEqual(f"{output.group()}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.destroy({output.group()})")
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"{i}.show({output.group()})")
                output = "** no instance found **\n"
                self.assertEqual(output, f.getvalue())
                TestConsole.truncate_string_io(f)

    def test_all_count(self):
        """ Test all and count commands
        """
        output = {"BaseModel": [], "User": [], "State": [], "City": [],
                  "Amenity": [], "Place": [], "Review": []}
        with patch('sys.stdout', new=StringIO()) as f:
            for i in self.classes:
                HBNBCommand().onecmd(f"create {i}")
                obj_id = search(r'.*-.*-.*-.*$', f.getvalue()).group()
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show {i} {obj_id}")
                output[i].append(f.getvalue().strip("\n"))
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.all()")
                self.assertEqual(f"{str(output[i])}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"all {i}")
                self.assertEqual(f"{str(output[i])}\n", f.getvalue())
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.count()")
                self.assertTrue(len(output[i]) >= int(f.getvalue()))
                TestConsole.truncate_string_io(f)

            HBNBCommand().onecmd("all")
            all_objects = []
            for i in output.keys():
                all_objects += output[i]
            self.assertEqual(f"{str(all_objects)}\n", f.getvalue())
            TestConsole.truncate_string_io(f)

    def test_update(self):
        """ Test update command
        """
        update_dict = {"new_attr": "254"}
        with patch('sys.stdout', new=StringIO()) as f:
            for i in self.classes:
                HBNBCommand().onecmd(f"create {i}")
                obj_id = search(r'.*-.*-.*-.*$', f.getvalue()).group()
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show {i} {obj_id}")
                str_0 = f.getvalue()
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"update {i} {obj_id} name Nairobi")
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show {i} {obj_id}")
                str_1 = f.getvalue()
                self.assertNotEqual(str_1, str_0)
                self.assertTrue("name" in str_1)
                self.assertTrue("Nairobi" in str_1)
                self.assertFalse("name" in str_0)
                self.assertFalse("Nairobi" in str_0)
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.update({obj_id} {update_dict})")
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show {i} {obj_id}")
                str_2 = f.getvalue()
                self.assertNotEqual(str_2, str_1)
                self.assertTrue("new_attr" in str_2)
                self.assertTrue("254" in str_2)
                self.assertTrue("name" in str_2)
                self.assertTrue("Nairobi" in str_2)
                self.assertFalse("new_attr" in str_1)
                self.assertFalse("254" in str_1)
                TestConsole.truncate_string_io(f)

                HBNBCommand().onecmd(f"{i}.update({obj_id}, text, 'test')")
                TestConsole.truncate_string_io(f)
                HBNBCommand().onecmd(f"show {i} {obj_id}")
                str_3 = f.getvalue()
                self.assertNotEqual(str_2, str_3)
                self.assertTrue("new_attr" in str_3)
                self.assertTrue("254" in str_3)
                self.assertTrue("name" in str_3)
                self.assertTrue("Nairobi" in str_3)
                self.assertTrue("text" in str_3)
                self.assertTrue("test" in str_3)
                self.assertFalse("text" in str_2)
                self.assertFalse("test" in str_2)
                TestConsole.truncate_string_io(f)

    @staticmethod
    def truncate_string_io(str_io):
        """ Method to truncate string input output object
            and reset the read position to the beginining of the file
            Args:
                str_io (StringIO): string object to work on
            Return: nothing
        """
        str_io.truncate(0)
        str_io.seek(0)

    def commands_test_routines(self, command="", str_io=None):
        """ Method to execute routine test tasks to avoid code verbosity
            NB: setUp methods not feasbility in this case.
                let me know if you think, otheriwe :)
        """
        pass
