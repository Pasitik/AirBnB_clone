#!/usr/bin/python3

""" Test module for base_model module """


from models.city import City
import unittest
from datetime import datetime
import io
import sys
import models
import inspect
import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """ A TestCase class that tests the City class """

    def test_initialization(self):
        """ test the initialization of the City class """

        model = City()
        self.assertIsInstance(model, City)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.name, str)
        self.assertIsInstance(model.state_id, str)
        self.assertEqual(model.name, "")
        self.assertEqual(model.state_id, "")

        model = City("name")
        self.assertIsInstance(model, City)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model.name = "John"
        model_dict = model.to_dict()
        model1 = City(**model_dict)
        self.assertIsInstance(model1, City)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)
        self.assertEqual(model.id, model1.id)
        self.assertEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertEqual(model.updated_at, model1.updated_at)
        self.assertFalse(isinstance(getattr(model, "__class__", None), str))

        model1 = City(
            id=model_dict["id"], name="James",
            created_at=model_dict["created_at"])
        self.assertIsInstance(model1, City)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertEqual(model.id, model1.id)
        self.assertNotEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)

        with self.assertRaises(ValueError) as ctx:
            model1 = City(
                id=model_dict["id"], name="James",
                created_at=model_dict["created_at"],
                updated_at="this is a bad date string")

    def test_save_instance_method(self):
        """ test the save instance method of the City class """

        model = City()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at
        self.assertNotEqual(date1, date2)

    def test_to_dict_instance_method(self):
        """ test the to_dict instance method of the City Class """

        model = City()
        m_dict = model.to_dict()
        m_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["id"], str)
        self.assertIsInstance(m_dict["created_at"], str)
        self.assertIsInstance(m_dict["updated_at"], str)

        model = City()
        model.name = "John"
        model.age = 50
        m_dict = model.to_dict()
        m_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["name"], str)
        self.assertIsInstance(m_dict["age"], int)

        with self.assertRaises(TypeError):
            m_dict = model.to_dict("argument")

    def test_str_representation(self):
        """ test the __str__ function of the City """

        model = City()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(model)

        m_str = new_stdout.getvalue()
        self.assertIn("[City]", m_str)
        self.assertIn("'id': ", m_str)
        self.assertIn("'created_at': datetime.datetime", m_str)
        self.assertIn("'updated_at': datetime.datetime", m_str)
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}\n",
            m_str)
        sys.stdout = sys.__stdout__


class TestCity(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.c = City()

    def test_doc_city(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(City.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.city.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(City, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_city(self):
        """ test instantiation of class """
        self.assertEqual(type(self.c.id), str)
        self.assertEqual(type(self.c.updated_at), datetime.datetime)
        self.assertEqual(type(self.c.created_at), datetime.datetime)

    def test_save_city(self):
        """ test State.save() """
        current_updatedAt = self.c.updated_at
        self.c.save()
        self.assertNotEqual(current_updatedAt, self.c.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.save(13)

    def test_to_dict_city(self):
        """ test City.to_dict() """
        self.c.name = "NYC"
        dict1 = self.c.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "City")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.to_dict('str')


if __name__ == '__main__':
    unittest.main()
