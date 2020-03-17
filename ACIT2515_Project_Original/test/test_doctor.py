from datetime import datetime
from unittest import TestCase
from doctor import Doctor

class TestDoctor(TestCase):
    """This is a test class to test the Doctor class"""
    def setUp(self):
        """This method defines the object one time so that we won't have to create the object over and over. """
        self.doctor = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, 123, 145000)

    def test_constructor(self):
        """This method tests the constructor of the Doctor class."""
        self.assertIsNotNone(self.doctor)
        self.assertIsInstance(self.doctor, Doctor)

    def test_invalid_constructor(self):
        """This method tests invalid constructors of the Doctor class."""
        with self.assertRaises(TypeError):
            doctor_1 = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, "123", 145000)

        with self.assertRaises(ValueError):
            doctor_2 = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, 0, 145000)

        with self.assertRaises(TypeError):
            doctor_3 = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, 123, "145000")

        with self.assertRaises(ValueError):
            doctor_4 = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, 123, 90000)

    def test_is_released(self):
        """Checks if the released status returns a valid value. (True or False)"""
        self.assertEqual(self.doctor.is_released(), False)
        self.assertFalse(self.doctor.is_released())
        self.assertIsNotNone(self.doctor.is_released())

    def test_get_office_num(self):
        """This checks if the method return the correct office number's value."""
        self.assertEqual(self.doctor.get_office_num(), 123)
        self.assertIsNotNone(self.doctor.get_office_num())

    def test_get_income_amount(self):
        """This checks if the method return the correct income value."""
        self.assertEqual(self.doctor.get_income_amount(), 145000)
        self.assertIsNotNone(self.doctor.get_income_amount())

    def test_get_type(self):
        """This method ensures that we coded correctly for get_type() method."""
        self.assertEqual(self.doctor.PERSON_TYPE, 'Doctor')
        self.assertIsNotNone(self.doctor.get_type())

    def test_get_description(self):
        """This one ensures that this method works correctly."""
        self.assertEqual(self.doctor.get_description(), None)

        self.doctor_1 = Doctor("Daniel", "Ta", "1980-09-12", "433 Bigbang, New Westminster, BC",
                             1, False, 123, 800000)
        self.assertEqual(self.doctor_1.get_description(), None)

    def test_to_dict(self):
        """Test to get the dictionary as json format """
        self.D1 = self.doctor.to_dict()
        self.D2 = {'first_name': 'Maria',
                   'last_name': 'Tran',
                   'date_of_birth': datetime(1980, 9, 12, 0, 0),
                   'address': '1444 Oakway, North Vancouver, Vancouver, BC',
                   'id': 1,
                   'is_released': False,
                   'office_num': 123,
                   'income': 145000}

        self.assertDictEqual(self.D1, self.D2)