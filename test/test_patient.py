from unittest import TestCase
from patient import Patient

class TestDoctor(TestCase):
    """This is a test class to test the House class"""
    def setUp(self):
        """This method defines the object one time so that we won't have to create the object over and over. """
        self.patient = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, 300, 200000)

    def test_constructor(self):
        """This method tests the constructor of the House class."""
        self.assertIsNotNone(self.patient)
        self.assertIsInstance(self.patient, Patient)

    def test_invalid_constructor(self):

        with self.assertRaises(TypeError):
            patient_1 = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, "300", 200000)

        with self.assertRaises(ValueError):
            patient_2 = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, 0, 200000)

    def test_is_released(self):
        """Checks if the selling status returns a valid value. (True or False)"""
        self.assertEqual(self.patient.is_released(), True)
        self.assertTrue(self.patient.is_released())
        self.assertIsNotNone(self.patient.is_released())

    def test_bill(self):
        """This checks if the get_address() method works as it should."""
        self.assertEqual(self.patient.bill, 200000)
        self.assertIsNotNone(self.patient.bill)

    def test_set_bill(self):
        """Checks if we can set the asked price correctly."""
        self.patient.set_bill(200000)
        self.assertEqual(self.patient.bill, 200000)
        self.assertIsNotNone(self.patient.bill)

    def test_get_type(self):
        """This method ensures that we coded correctly for get_type() method."""
        self.assertEqual(self.patient.PERSON_TYPE, 'Patient')
        self.assertIsNotNone(self.patient.get_type())

    def test_get_description(self):
        """This one ensures that this method works correctly."""
        self.assertTrue(self.patient.is_released())
        self.assertEqual(self.patient.get_description(), None)

        self.patient_1 = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, 300, 200000)
        self.assertEqual(self.patient_1.get_description(), None)

    def test_get_room_num(self):
        """Checks that the commission value is correct."""
        self.assertEqual(self.patient.get_room_num(), 300)
        self.assertIsNotNone(self.patient.get_room_num())

    def test_get_bill_amount(self):
        """Checks that the commission value is correct."""
        self.assertEqual(self.patient.get_bill_amount(), 200000)
        self.assertIsNotNone(self.patient.get_bill_amount())