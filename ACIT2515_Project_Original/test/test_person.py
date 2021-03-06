from unittest import TestCase
from person import Person
from datetime import datetime


class TestPerson(TestCase):
    """This is a test class to test the Person class"""
    def setUp(self):
        """This method defines the object one time so that we won't have to create the object over and over. """
        self.person = Person("Mahsa", "Taer", "1995-06-15", "3432 Newtons, Richmond, BC", 1, False)

    def test_init(self):
        """This method tests the constructor of the Person class."""
        self.assertIsNotNone(self.person)
        self.assertIsInstance(self.person, Person)

    def test_invalid_init(self):
        """This method tests an invalid constructor of the Person class."""
        with self.assertRaises(TypeError):
            person_1 = Person(1, "Taer", "1995-06-15", "3432 Newtons, Richmond, BC", 1, False)

        with self.assertRaises(TypeError):
            person_2 = Person("Mahsa", 2, "1995-06-15", "3432 Newtons, Richmond, BC", 1, False)

        with self.assertRaises(TypeError):
            person_3 = Person("Mahsa", "Taer", "1995-06-15", True, 1, False)

        with self.assertRaises(TypeError):
            person_4 = Person("Mahsa", "Taer", "1995-06-15", "3432 Newtons, Richmond, BC", "1", False)

        with self.assertRaises(ValueError):
            person_5 = Person("Mahsa", "Taer", "1995-06-15", "3432 Newtons, Richmond, BC", 0, False)

    def test_is_released(self):
        """Checks if the released status returns a valid value. (True or False)"""
        self.assertEqual(self.person.is_released(), False)
        self.assertFalse(self.person.is_released())
        self.assertIsNotNone(self.person.is_released())

    def test_get_address(self):
        """This checks if the get_address() method works as it should."""
        self.assertEqual(self.person.get_address(), "3432 Newtons, Richmond, BC")
        self.assertIsNotNone(self.person.get_address())

    def test_get_id(self):
        """This checks if we can get the id of a person object."""
        self.assertEqual(self.person.get_id(), 1)
        self.assertIsNotNone(self.person.get_id())

    def test_get_firstName(self):
        """This checks if we can get the last name of a person object."""
        self.assertEqual(self.person.get_firstName(), "Mahsa")
        self.assertIsNotNone(self.person.get_firstName())

    def test_get_lastName(self):
        """This checks if we can get the last name of a person object."""
        self.assertEqual(self.person.get_lastName(), "Taer")
        self.assertIsNotNone(self.person.get_lastName())

    def test_get_date_of_birth(self):
        """Get the day of birth of a person object."""
        self.assertEqual(self.person.get_date_of_birth().strftime("%Y-%m-%d"), "1995-06-15")
        self.assertIsNotNone(self.person.get_date_of_birth())

    def test_get_type(self):
        """This method ensures that we coded correctly for get_type() method."""
        with self.assertRaises(NotImplementedError):
            self.person.get_type()

    def test_display_description(self):
        """This one ensures that this method works correctly."""
        with self.assertRaises(NotImplementedError):
            self.person.get_description()

    def test_to_dict(self):
        """This one ensures that the method to_dict works correctly"""
        with self.assertRaises(NotImplementedError):
            self.person.to_dict()