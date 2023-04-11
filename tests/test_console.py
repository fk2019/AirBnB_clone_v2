#!/usr/bin/python3
"""
   Test the console
"""
import unittest
import os
import sys
import models
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Unit tests for the console
    """
    @classmethod
    def setUpClass(cls):
        """Set up instance of the HBNBCommand for the tests
        """
        cls.HBNB = HBNBCommand()

    def setUp(self):
        """Set up a temporary file storage and set its objects to empty
        """
        FileStorage._FileStorage__objects = {}

    def test_create(self):
        """Test create command with various inputs. Here, I used
           self.subTest to loop through each test instead of copying
           the same code for each input
        """
        with patch("sys.stdout", return_value=StringIO()) as f:
            com = ["create Place", "create State", "create Review",
                   "create User", "create City", "create Amenity"]
            for n in com:
                with self.subTest(n=n):
                    self.HBNB.onecmd(n)
                    f.getvalue().strip()

    def test_all(self):
        """Test all command based on stdout and objects in storage
        """
        with patch("sys.stdout", return_value=StringIO()) as f:
            create = ["create Place", "create State", "create Review",
                      "create User", "create City", "create Amenity"]
            for n in create:
                with self.subTest(n=n):
                    self.HBNB.onecmd(n)
                    f.getvalue()
        all_ = ["all Place", "all State", "all Review", "all User",
                "all City"]
        m = []
        for n in all_:
            with self.subTest(n=n):
                out = StringIO()
                sys.stdout = out
                self.HBNB.onecmd(n)
                sys.stdout = sys.__stdout__
                obj = out.getvalue()[2:-3]
                m.append(obj)
        val = []
        for v in FileStorage._FileStorage__objects.values():
            x = v
            val.append(str(x))
        for n in m:
            with self.subTest(n=n):
                self.assertIn(n, val)

    def test_count(self):
        """Test count command
        """
        with patch("sys.stdout", return_value=StringIO()) as f:
            com = ["create Place", "create State", "create Review",
                   "create User", "create City", "create Amenity"]
            for n in com:
                with self.subTest(n=n):
                    self.HBNB.onecmd(n)
                    f.getvalue().strip()
        count = ["count Place", "count State", "count Review",
                 "count User", "count City", "count Amenity"]
        for v in count:
            self.subTest(n=v)
            out = StringIO()
            sys.stdout = out
            self.HBNB.onecmd(v)
            sys.stdout = sys. __stdout__
            self.assertEqual('1', out.getvalue().strip())

    def test_show(self):
        """Test show bad command
        """
        res = []
        com = ["show", "show world", "show Review",
               "show User 234235"]
        for n in com:
            with self.subTest(n=n):
                out = StringIO()
                sys.stdout = out
                self.HBNB.onecmd(n)
                sys.stdout = sys.__stdout__
                res.append(out.getvalue().strip())
        errors = ["** class name missing **",
                  "** class doesn't exist **",
                  "** instance id missing **",
                  "** no instance found **"]
        for e in errors:
            self.assertIn(e, res)

    def test_destroy(self):
        """Test destroy bad command
        """
        res = []
        com = ["destroy", "destroy world", "destroy Review",
               "destroy User 234235"]
        for n in com:
            with self.subTest(n=n):
                out = StringIO()
                sys.stdout = out
                self.HBNB.onecmd(n)
                sys.stdout = sys.__stdout__
                res.append(out.getvalue().strip())
        errors = ["** class name missing **",
                  "** class doesn't exist **",
                  "** instance id missing **",
                  "** no instance found **"]
        for e in errors:
            self.assertIn(e, res)

    def test_count_bad(self):
        """Test count returns 0 on errors
        """
        count = ["count", "count 2354d", "count place"]
        for v in count:
            self.subTest(n=v)
            out = StringIO()
            sys.stdout = out
            self.HBNB.onecmd(v)
            sys.stdout = sys. __stdout__
            self.assertEqual('0', out.getvalue().strip())

    def test_create_bad(self):
        """Test create command with errors
        """
        create = ["create", "create place", "create 234ffdv"]
        errors = ["** class name missing **", "** class doesn't exist **"]
        for c in create:
            with self.subTest(n=c):
                out = StringIO()
                sys.stdout = out
                self.HBNB.onecmd(c)
                sys.stdout = sys.__stdout__
                r = out.getvalue().strip()
                self.assertIn(r, errors)

    def test_all_bad(self):
        """Test all command based on stdout with bad/errors
        """
        all_ = ["all Places", "all state", "all pirates",
                "all members", "all 23524"]
        for n in all_:
            with self.subTest(n=n):
                out = StringIO()
                sys.stdout = out
                self.HBNB.onecmd(n)
                sys.stdout = sys.__stdout__
                t = out.getvalue().strip()
                self.assertEqual("** class doesn't exist **", t)

    def tearDown(self):
        """Remove temporary file storage
        """
        FileStorage._Filestorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Remove the set up instance of HBNB console
        """
        del cls.HBNB


if __name__ == "__main__":
    unittest.main()
