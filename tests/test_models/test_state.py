#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_state_instance_creation(self):
        """Test State instance creation."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_state_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(isinstance(state.name, str))

    def test_state_attributes_assignment(self):
        """Test State attributes assignment."""
        state = State()
        state.name = "San Francisco"
        self.assertEqual(state.name, "San Francisco")

    def test_state_to_dict(self):
        """Test State to_dict method."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(
                state_dict["created_at"], state.created_at.isoformat()
        )
        self.assertEqual(
                state_dict["updated_at"], state.updated_at.isoformat()
        )

    def test_state_str_representation(self):
        """Test State __str__ representation."""
        state = State()
        str_repr = str(state)
        self.assertIn("[State]", str_repr)
        self.assertIn(state.id, str_repr)
        self.assertIn(str(state.__dict__), str_repr)


if __name__ == "__main__":
    unittest.main()
