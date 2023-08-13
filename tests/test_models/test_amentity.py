#!/usr/bin/python3
"""Defines alternative unittests for models/amenity.py.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityInstantiation(unittest.TestCase):
    """Test Amenity class instantiation and basic attributes."""

    def test_create_instance(self):
        """Create instance test """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_instance_stored_in_objects(self):
        """test instance stored in objects"""
        amenity = Amenity()
        self.assertIn(amenity, models.storage.all().values())

    def test_id_is_str(self):
        """test if id is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
    
    def test_created_at_is_datetime(self):
        """test created at is datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """test updated at is datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_name_not_in_instance_dict(self):
        """test name not in instance"""
        amenity = Amenity()
        self.assertNotIn("name", amenity.__dict__)

    def test_two_amenities_unique_ids(self):
        """test two amenities have unique ids"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_amenities_created_at_order(self):
        """test amenities created at"""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_amenities_updated_at_order(self):
        """test amenities updated at order"""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        """test str representation"""
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        am_str = str(amenity)
        self.assertIn("[Amenity] (123456)", am_str)
        self.assertIn("'id': '123456'", am_str)
        self.assertIn("'created_at': " + repr(dt), am_str)
        self.assertIn("'updated_at': " + repr(dt), am_str)

    def test_args_unused(self):
        """test args unused"""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """test instantiation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertAlmostEqual(amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """test instantiation with none kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Test save method of the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """setup calss"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """test one save"""
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_two_saves(self):
        """test two save"""
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity.save()
        self.assertLess(second_updated_at, amenity.updated_at)

    def test_save_with_arg(self):
        """test save with"""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        """test save update file"""
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Test to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """ test to dict"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """test to dict contains correct keys"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_to_dict_contains_added_attributes(self):
        """test dict contains added attributes"""
        amenity = Amenity()
        amenity.middle_name = "Holberton"
        amenity.my_number = 98
        amenity_dict = amenity.to_dict()
        self.assertEqual("Holberton", amenity.middle_name)
        self.assertIn("my_number", amenity_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """test to dict datime"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict["id"], str)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_to_dict_output(self):
        """test to dict output"""
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        amenity_dict = amenity.to_dict()
        self.assertDictEqual(amenity_dict, expected_dict)

    def test_to_dict_dunder_dict(self):
        """" """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertNotEqual(amenity_dict, amenity.__dict__)

    def test_to_dict_with_arg(self):
        """test_to_dict_with_arg"""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


class Test_Amenity(unittest.TestCase):
    """Tests for the User class."""

    def test_amenity_instance_creation(self):
        """Test amenity instance creation."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_review_attributes(self):
        """Test amenity attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(isinstance(amenity.name, str))
        self.assertTrue(type(amenity.name) is str)

    def test_amenity_attributes_assignment(self):
        """Test amenity attributes assignment."""
        amenity = Amenity()
        amenity.name = "London"
        self.assertEqual(amenity.name, "London")

    def test_amenity_to_dict(self):
        """Test amenity to_dict method."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["id"], amenity.id)
        self.assertEqual(
            amenity_dict["created_at"], amenity.created_at.isoformat()
        )
        self.assertEqual(
            amenity_dict["updated_at"], amenity.updated_at.isoformat()
        )

    def test_amenity_str_representation(self):
        """Test amenity __str__ representation."""
        amenity = Amenity()
        str_repr = str(amenity)
        self.assertIn("[Amenity]", str_repr)
        self.assertIn(amenity.id, str_repr)
        self.assertIn(str(amenity.__dict__), str_repr)


if __name__ == "__main__":
    unittest.main()
