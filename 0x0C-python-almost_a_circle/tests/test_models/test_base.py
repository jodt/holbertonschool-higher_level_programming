#!/usr/bin/python3
"""
Unittest for "base.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import pycodestyle
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """
    class that test the max integer function
    Task 1:
        you can assume id is an integer and you don’t need to test the
            type of it
    Tests:
        test_many_created (working test):
            no arguments when created Base
            None arguments when created Base
            Random integer argument when created Base
            negative integer when creating Base
            double same id when creating Base
        test_too_many_arguments (no-working test):
            too many arguments given
    """

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        module = len(base.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(Base.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.to_json_string.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.save_to_file.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.from_json_string.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.create.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.load_from_file.__doc__)
        self.assertGreater(module_class, 0)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_many_created(self):
        """fuction that test for good assignment of differents id value"""
        b1 = Base()
        b2 = Base(None)
        b3 = Base(12)
        b4 = Base()
        b5 = Base(-3)
        b6 = Base(2)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, -3)
        self.assertEqual(b6.id, 2)

    def test_too_many_arguments(self):
        """
        fuction that test for TypeError
        """
        with self.assertRaises(TypeError):
            Base(1, 2)
# ---------------------------------------------------------------

    def test_base_to_json_string(self):
        """
        This function test if the method to_json_string returns
        the JSON string representation ofdictionaries list
        """
        dict_test = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        self.assertTrue(type(Base.to_json_string(dict_test)), str)
        self.assertEqual(Base.to_json_string(
            dict_test), '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

# --------------------------------------------------------------
    def test_base_from_json_string(self):
        """
        This function test if the method from_json_string returns
        the list of the JSON string representation
        """
        json_str = '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]'
        self.assertTrue(type(Base.from_json_string(json_str)), list)
        self.assertTrue(
            all(type(elt) is dict for elt in Base.from_json_string(
                json_str)), dict)
        self.assertEqual(Base.from_json_string(json_str), [
                         {"a": 1, "b": 2}, {"c": 3, "d": 4}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

#
