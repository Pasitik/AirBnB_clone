#!/usr/bin/python3
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests for the Place class."""

    def test_place_instance_creation(self):
        """Test Place instance creation."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_attributes(self):
        """Test Place attributes."""
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(isinstance(place.name, str))
        self.assertTrue(isinstance(place.city_id, str))
        self.assertTrue(isinstance(place.user_id, str))
        self.assertTrue(isinstance(place.description, str))
        self.assertTrue(isinstance(place.number_rooms, int))
        self.assertTrue(isinstance(place.number_bathrooms, int))
        self.assertTrue(isinstance(place.max_guest, int))
        self.assertTrue(isinstance(place.price_by_night, int))
        self.assertTrue(isinstance(place.latitude, float))
        self.assertTrue(isinstance(place.longitude, float))
        self.assertTrue(isinstance(place.amenity_ids, object))

    def test_place_attributes_assignment(self):
        """Test Place attributes assignment."""
        place = Place()
        place.name = "London"
        place.city_id = "1234"
        place.user_id = "5678"
        place.description = "San Francisco"
        place.number_rooms = 567
        place.number_bathrooms = 567
        place.max_guest = 567
        place.price_by_night = 567
        place.latitude = 56.7
        place.longitude = 56.7
        place.amenity_ids = ["56a7"]
        self.assertEqual(place.name, "London")
        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "5678")
        self.assertEqual(place.description, "San Francisco")
        self.assertEqual(place.number_rooms, 567)
        self.assertEqual(place.number_bathrooms, 567)
        self.assertEqual(place.max_guest, 567)
        self.assertEqual(place.price_by_night, 567)
        self.assertEqual(place.latitude, 56.7)
        self.assertEqual(place.longitude, 56.7)
        self.assertEqual(place.amenity_ids, ["56a7"])

    def test_place_to_dict(self):
        """Test Place to_dict method."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(
            place_dict["created_at"], place.created_at.isoformat()
        )
        self.assertEqual(
            place_dict["updated_at"], place.updated_at.isoformat()
        )

    def test_place_str_representation(self):
        """Test Place __str__ representation."""
        place = Place()
        str_repr = str(place)
        self.assertIn("[Place]", str_repr)
        self.assertIn(place.id, str_repr)
        self.assertIn(str(place.__dict__), str_repr)


if __name__ == "__main__":
    unittest.main()
