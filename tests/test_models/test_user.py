#!/usr/bin/python3
"""Defines  unittests for models/state"""

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def test_user_instance_creation(self):
        """Test User instance creation."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_review_attributes(self):
        """Test User attributes."""
        user = User()
        self.assertEqual(user.password, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertTrue(isinstance(user.password, str))
        self.assertTrue(isinstance(user.email, str))
        self.assertTrue(isinstance(user.first_name, str))
        self.assertTrue(isinstance(user.last_name, str))

    def test_user_attributes_assignment(self):
        """Test User attributes assignment."""
        user = User()
        user.email = "j@alx.com"
        user.password = "5678"
        user.first_name = "john"
        user.last_name = "Freeman"
        self.assertEqual(user.email, "j@alx.com")
        self.assertEqual(user.password, "5678")
        self.assertEqual(user.first_name, "john")
        self.assertEqual(user.last_name, "Freeman")

    def test_user_to_dict(self):
        """Test User to_dict method."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(
            user_dict["created_at"], user.created_at.isoformat()
        )
        self.assertEqual(
            user_dict["updated_at"], user.updated_at.isoformat()
        )

    def test_user_str_representation(self):
        """Test User __str__ representation."""
        user = User()
        str_repr = str(user)
        self.assertIn("[User]", str_repr)
        self.assertIn(user.id, str_repr)
        self.assertIn(str(user.__dict__), str_repr)


if __name__ == "__main__":
    unittest.main()
