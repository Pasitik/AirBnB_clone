#!/usr/bin/python3
"""Defines test for models/review."""

import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests for the Review class."""

    def test_review_instance_creation(self):
        """Test Review instance creation."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_review_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(isinstance(review.place_id, str))
        self.assertTrue(isinstance(review.user_id, str))
        self.assertTrue(isinstance(review.text, str))

    def test_review_attributes_assignment(self):
        """Test Review attributes assignment."""
        review = Review()
        review.text = "London"
        review.place_id = "1234"
        review.user_id = "5678"
        self.assertEqual(review.text, "London")
        self.assertEqual(review.place_id, "1234")
        self.assertEqual(review.user_id, "5678")

    def test_review_to_dict(self):
        """Test Review to_dict method."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["id"], review.id)
        self.assertEqual(
            review_dict["created_at"], review.created_at.isoformat()
        )
        self.assertEqual(
            review_dict["updated_at"], review.updated_at.isoformat()
        )

    def test_review_str_representation(self):
        """Test Review __str__ representation."""
        review = Review()
        str_repr = str(review)
        self.assertIn("[Review]", str_repr)
        self.assertIn(review.id, str_repr)
        self.assertIn(str(review.__dict__), str_repr)


if __name__ == "__main__":
    unittest.main()
