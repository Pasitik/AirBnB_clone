#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import models
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_city_instance_creation(self):
        """Test City instance creation."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_city_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_assignment(self):
        """Test City attributes assignment."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict(self):
        """Test City to_dict method."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(
                city_dict["created_at"], city.created_at.isoformat()
        )
        self.assertEqual(
                city_dict["updated_at"], city.updated_at.isoformat()
        )

    def test_city_str_representation(self):
        """Test City __str__ representation."""
        city = City()
        str_repr = str(city)
        self.assertIn("[City]", str_repr)
        self.assertIn(city.id, str_repr)
        self.assertIn(str(city.__dict__), str_repr)


class TestCityPlus(unittest.TestCase):
    """Test City class"""

    def test_attribut_state_id(self):
        """ Test with state id"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(type(city.state_id) == str)

    def test_attribut_name(self):
        """ Test with state name"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(type(city.name) == str)

    def test_class_doc(self):
        """ ``City`` documentation"""
        self.assertIsNotNone(City.__doc__)

    def test_module_doc(self):
        """ Test the city_model module's documentation"""
        self.assertIsNotNone(models.city.__doc__)


if __name__ == "__main__":
    unittest.main()
