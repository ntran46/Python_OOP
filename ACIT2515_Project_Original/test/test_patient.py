from datetime import datetime
from unittest import TestCase
from patient import Patient

class TestPatient(TestCase):
    """This is a test class to test the Patient class"""
    def setUp(self):
        """This method defines the object one time so that we won't have to create the object over and over. """
        self.patient = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, 300, 200000)

    def test_constructor(self):
        """This method tests the constructor of the Patient class."""
        self.assertIsNotNone(self.patient)
        self.assertIsInstance(self.patient, Patient)

    def test_invalid_constructor(self):
        """This method tests invalid constructors of the Patient class."""
        with self.assertRaises(TypeError):
            patient_1 = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, "300", 200000)

        with self.assertRaises(ValueError):
            patient_2 = Patient("Uy", "Tran", "1990-11-20", "1111 Columbia, New Westminster, BC",
                               2, True, 0, 200000)

    def test_is_released(self):
        """Checks if the released status returns a valid value. (True or False)"""
        self.assertEqual(self.patient.is_released(), True)
        self.assertTrue(self.patient.is_released())
        self.assertIsNotNone(self.patient.is_released())

    def test_bill(self):
        """This checks if the method return the correct bill number's value."""
        self.assertEqual(self.patient.bill, 200000)
        self.assertIsNotNone(self.patient.bill)

    def test_set_bill(self):
        """Checks if we can set the bill amount correctly."""
        self.patient.bill= 200000
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
                               2, False, 300, 200000)
        self.assertEqual(self.patient_1.get_description(), None)

    def test_get_room_num(self):
        """This checks if the method return the correct room number's value."""
        self.assertEqual(self.patient.get_room_num(), 300)
        self.assertIsNotNone(self.patient.get_room_num())

    def test_to_dict(self):
        """Test to get the dictionary as json format """
        self.D1 = self.patient.to_dict()
        self.D2 = {'address': '1111 Columbia, New Westminster, BC',
                   'bill': 200000,
                   'date_of_birth': datetime(1990, 11, 20, 0, 0),
                   'first_name': 'Uy',
                   'id': 2,
                   'is_released': True,
                   'last_name': 'Tran',
                   'room_num': 300}
        self.assertDictEqual(self.D1, self.D2)

    def test_set_first_name(self):
        with self.assertRaises(ValueError):
            self.patient.set_first_name(34)
        self.patient.set_first_name("Mahsa")
        self.assertEqual(self.patient.get_firstName(), "Mahsa")
        self.assertIsNotNone(self.patient.get_firstName())

    def test_set_last_name(self):
        with self.assertRaises(ValueError):
            self.patient.set_last_name(34)
        self.patient.set_last_name("Taer")
        self.assertEqual(self.patient.get_lastName(), "Taer")
        self.assertIsNotNone(self.patient.get_lastName())

    def test_set_room_num(self):
        with self.assertRaises(ValueError):
            self.patient.set_room_num("34")
        self.patient.set_room_num(586)
        self.assertEqual(self.patient.get_room_num(), 586)
        self.assertIsNotNone(self.patient.get_room_num())

    def test_str_(self):
        self.patient.__str__()
        self.assertEqual(self.patient.__str__(), "<Patient Uy Tran (2)")
        self.assertIsNotNone(self.patient.__str__())

