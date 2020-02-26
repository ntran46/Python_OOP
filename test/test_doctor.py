from unittest import TestCase
from doctor import Doctor

class TestDoctor(TestCase):
    """This is a test class to test the House class"""
    def setUp(self):
        """This method defines the object one time so that we won't have to create the object over and over. """
        self.doctor = Doctor("Maria", "Tran", "1980-09-12", "1444 Oakway, North Vancouver, Vancouver, BC",
                             1, False, 123, 145000)

    def test_constructor(self):
        """This method tests the constructor of the House class."""
        self.assertIsNotNone(self.doctor)
        self.assertIsInstance(self.doctor, Doctor)

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
        """Checks if the selling status returns a valid value. (True or False)"""
        self.assertEqual(self.doctor.is_released(), False)
        self.assertFalse(self.doctor.is_released())
        self.assertIsNotNone(self.doctor.is_released())

    def test_get_office_num(self):
        """This checks if the get_address() method works as it should."""
        self.assertEqual(self.doctor.get_office_num(), 123)
        self.assertIsNotNone(self.doctor.get_office_num())

    def test_get_income_amount(self):
        """Checks if the selling status returns a valid value. (True or False)"""
        self.assertEqual(self.doctor.get_income_amount(), 145000)
        self.assertIsNotNone(self.doctor.get_income_amount())

    def test_get_type(self):
        """This method ensures that we coded correctly for get_type() method."""
        self.assertEqual(self.doctor.PERSON_TYPE, 'Doctor')
        self.assertIsNotNone(self.doctor.get_type())

    def test_display_description(self):
        """This one ensures that this method works correctly."""
        self.assertEqual(self.doctor.get_description(), None)

        self.doctor_1 = Doctor("Daniel", "Ta", "1980-09-12", "433 Bigbang, New Westminster, BC",
                             1, False, 123, 800000)
        self.assertEqual(self.doctor_1.get_description(), None)