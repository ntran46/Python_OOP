from unittest import TestCase, mock

from department import Department
from patient import Patient
from doctor import Doctor
from datetime import datetime

class TestDepartment(TestCase):

    """This is a test class to test the Department class"""

    def setUp(self) -> None:
        """Initialize setup object"""
        self.department = Department("Emergency")
        self.department1 = Department("Surgery")
        self.doctor1 = Doctor("George", "Bush", "1982-2-28", "97334 Oak Bridge , Vancouver, Vancouver, BC", 2, False,
                              125, 190000)
        self.patient1 = Patient("Jose", "McDonald", "1970-12-12", "3432 Newtons, Richmond, BC", 1, False, 589)
        self.doctor2 = Doctor("Johnny", "Kenedy", "1984-1-30", "1444 Oakway, North Vancouver, Vancouver, BC", 1, False,
                              123, 150000)
        self.patient2 = Patient("Bill", "Stark", "1960-9-2", "1111 Columbia, New Westminster, BC", 2, False, 589)

        self.patient3 = Patient("Tony", "Stark", "1960-9-2", "1111 Columbia, New Westminster, BC", 12, False, 589)

        self.department.add_person(self.patient1)
        self.department.add_person(self.patient2)
        self.department.add_person(self.doctor1)
        self.department.add_person(self.doctor2)


    def test_valid_constructor(self):
        """Test an object is created correctly"""
        self.assertIsNotNone(self.department)
        self.assertIsInstance(self.department, Department)


    def test_invalid_constructor(self):
        """Test an object with invalid parameters"""
        with self.assertRaises(TypeError):
            department_1 = Department(1)


    def test_add_person(self):
        """Test to add an object (person) to the department"""
        test_case = self.department.get_statistics()
        self.assertEqual(test_case.get_not_released_patient_num(), 2)


    def test_remove_person(self):
        """Test to remove an object (person) out of the department"""
        test_id = self.patient1.get_id()
        self.department.remove_person_by_id(test_id)
        test_case = self.department.get_statistics()
        self.assertEqual(test_case.get_not_released_patient_num(), 1)

        with self.assertRaises(ValueError):
            self.department.remove_person_by_id(100)
            self.test_write_data_to_file()

    def test_check_existing_person(self):
        """Test to check if an object (person) is in the department"""
        test_id = self.patient3.get_id()
        self.assertEqual(self.department.person_exist(test_id), False)

        test_id_1 = self.doctor2.get_id()
        self.assertEqual(self.department.person_exist(test_id_1), True)

    def test_get_person_by_type(self):
        """Test to get all people with a given type"""
        with self.assertRaises(TypeError):
            self.department.get_person_by_type(1)

        return_text = "There is no type \"Teacher\" of person in the department Emergency."
        self.assertEqual(self.department.get_person_by_type("Teacher"), return_text)
        self.department.get_person_by_type("Patient")

    def test_get_all_people(self):
        """Test to get all people in a department"""
        self.department.get_all_current_people()

    def test_get_existing_person(self):
        """Test to get an object (person) from the department"""
        test_id = self.patient2.get_id()
        self.assertEqual(self.department.get_person_by_id(test_id), self.patient2)

        with self.assertRaises(ValueError):
            self.department.get_person_by_id(100)


    def test_get_department_name(self):
        """Test to get the name of the department"""
        self.assertEqual(self.department.get_name(), "Emergency")


    def test_get_get_statistics(self):
        """Test to get statistics of the department"""
        self.patient1.bill = 10000
        test_case = self.department.get_statistics()
        self.assertEqual(test_case.get_not_released_patient_num(), 1)
        self.assertEqual(test_case.get_released_patient_num(), 1)
        self.assertEqual(test_case.get_total_bill_amount_released_patients(), 10000)

    @mock.patch('department.Department._write_to_file')
    def test_write_data_to_file(self, mock_save_func):
        """Test to see if a file is opened and gotten data"""
        self.department.add_person(self.patient3)
        self.assertTrue(mock_save_func.called)
        if mock_save_func.called:
            print("Write function is called")

    @mock.patch('department.Department._read_from_file')
    def test_read_data_to_file(self, mock_read_func):
        """Test to see if a file is opened and data is written on"""
        self.department._read_from_file()
        self.assertTrue(mock_read_func.called)

    @mock.patch('department.Department._read_from_file')
    def test_get_created_entities(self, mock_read_func):
        """Test to check a valid object is created correctly and add to the department list"""
        output = self.department1._read_from_file()
        if mock_read_func.called:
            print("Read function is called")
            for obj in output:
                self.assertIsNotNone(obj)
                self.assertIsInstance(obj, (Doctor, Patient))

    def test_to_dict(self):
        """Test to get the dictionary as json format """
        self.department1.add_person(self.doctor1)
        self.department1.add_person(self.patient1)
        self.D1 = self.department1.to_dict()
        self.D2 = {'name': 'Surgery',
                   'doctor': [
                       {'first_name': 'George',
                        'last_name': 'Bush',
                        'date_of_birth': datetime(1982, 2, 28, 0, 0),
                        'address': '97334 Oak Bridge , Vancouver, Vancouver, BC',
                        'id': 2,
                        'is_released': False,
                        'office_num': 125,
                        'income': 190000}
                   ],
                   'patient': [
                       {'first_name': 'Jose',
                        'last_name': 'McDonald',
                        'date_of_birth': datetime(1970, 12, 12, 0, 0),
                        'address': '3432 Newtons, Richmond, BC',
                        'is_released': False,
                        'id': 1,
                        'room_num': 589,
                        'bill': 0.0}
                   ]}
        self.assertDictEqual(self.D1, self.D2)