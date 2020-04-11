from unittest import TestCase
from Model.department import Department
from Model.patient import Patient
from Model.doctor import Doctor
from datetime import datetime
from peewee import SqliteDatabase
import peewee


class TestDepartment(TestCase):
    """This is a test class to test the Department class"""

    @classmethod
    def setUpClass(cls):
        """ Initialize setup object"""
        cls.test_db = SqliteDatabase("testing.db", pragmas={'ignore_check_constraints': 0})
        with cls.test_db.bind_ctx([Department, Doctor, Patient]):
            cls.test_db.create_tables([Department, Doctor, Patient])
            cls.department = Department(name="Emergency")
            cls.department.save()
            cls.doctor1 = Doctor(person_id='D005', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
                                 address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=False,
                                 office_num=123,
                                 income=10000)
            cls.doctor1.save()
            cls.doctor2 = Doctor(person_id='D006', firstName="George", lastName="Bush", date_of_birth="1982-2-28",
                                 address="97334 Oak Bridge , Vancouver, Vancouver, BC", is_released=False,
                                 office_num=125,
                                 income=190000)
            cls.doctor2.save()
            cls.patient1 = Patient(person_id='P006', firstName="Jose", lastName="McDonald", date_of_birth="1970-12-12",
                                   address="3432 Newtons, Richmond, BC", is_released=False, room_num=590)
            cls.patient1.save()
            cls.patient2 = Patient(person_id='P007', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                   address="1111 Columbia, New Westminster, BC", is_released=True, room_num=589, bill=500)
            cls.patient2.save()

    def test_valid_object(self):
        """ Test an object is created and save correctly"""
        self.assertIsNotNone(self.department)
        self.assertIsNotNone(self.doctor1)
        self.assertIsNotNone(self.patient2)

        self.assertIsInstance(self.department, Department)
        self.assertIsInstance(self.doctor1, Doctor)
        self.assertIsInstance(self.patient2, Patient)

    def test_invalid_object(self):
        """ Test an object with invalid parameters"""
        with self.assertRaises(Exception):
            # Invalid room_num
            self.patient3 = Patient(person_id='P002', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                    address="1111 Columbia, New Westminster, BC", is_released=False, room_num="589")
            self.patient3.save()
            # Invalid person_id
            self.patient4 = Patient(person_id='EE002', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                    address="1111 Columbia, New Westminster, BC", is_released=False, room_num="589")
            self.patient4.save()
            # Invalid bill
            self.patient5 = Patient(person_id='EE002', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                    address="1111 Columbia, New Westminster, BC", is_released=False, room_num="589",
                                    bill="3434")
            self.patient5.save()
            # Invalid office_num
            self.doctor3 = Doctor(person_id='D001', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
                                  address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=False,
                                  office_num=-123, income=10000)
            self.doctor3.save()
            # Invalid person_id
            self.doctor4 = Doctor(person_id='addsad', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
                                  address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=False,
                                  office_num=-123, income=10000)
            self.doctor4.save()
            # Invalid income
            self.doctor5 = Doctor(person_id='D001', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
                                  address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=False,
                                  office_num=-123, income=-10000)
            self.doctor5.save()

    def test_add_person(self):
        """Test to add an object (person) to the department"""
        self.patient3 = Patient(person_id='P006', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                address="1111 Columbia, New Westminster, BC", is_released=False, room_num=589)
        self.patient4 = Patient(person_id='P004', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                                address="1111 Columbia, New Westminster, BC", is_released=False, room_num=589)

        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            with self.assertRaises(peewee.IntegrityError):
                self.department.add_person(self.patient3)
            self.department.add_person(self.patient4)
            person = Patient.select().where(Patient.person_id == self.patient4.person_id)
            self.assertEqual(person.exists(), True)

    def test_remove_person(self):
        """Test to remove an object (person) out of the department"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            self.department.remove_person_by_id('D005')
            person = Patient.select().where(Patient.person_id == 'D005')
            self.assertEqual(person.exists(), False)

            # This is to test exception value error of remove method
            with self.assertRaises(ValueError):
                self.department.remove_person_by_id('D001')

    def test_check_existing_person(self):
        """Test to check if an object (person) is in the department"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            test_id = self.patient2.person_id
            self.assertEqual(self.department.person_exist(test_id), True)
            test_id_1 = 'P122'
            self.assertEqual(self.department.person_exist(test_id_1), False)

    def test_get_person_by_type(self):
        """Test to get all people with a given type"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            obj = self.department.get_person_by_type("Teacher")
            self.assertEqual(len(obj), 0)
            self.department.get_all_current_people()
            obj1 = self.department.get_person_by_type("Patient")
            self.assertEqual(len(obj1), 3)
            with self.assertRaises(TypeError):
                obj3 = self.department.get_person_by_type(12)

    def test_get_all_people(self):
        """Test to get all people in a department"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            self.department.get_all_current_people()

    def test_get_existing_person_by_id(self):
        """Test to get an object (person) from the department"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            test_id = self.patient2.person_id
            obj1 = self.department.get_person_by_id(test_id)
            D1 = obj1.to_dict()
            temp = str(D1['date_of_birth'].year) + "-" + \
                   str(D1['date_of_birth'].month) + "-" + \
                   str(D1['date_of_birth'].day)
            D1['date_of_birth'] = temp
            if D1['is_released'] == 'True':
                D1['is_released'] = True
            elif D1['is_released'] == 'False':
                D1['is_released'] = False
            self.assertEqual(D1, self.patient2.to_dict())

            obj2 = self.department.get_person_by_id(100)
            self.assertEqual(obj2, None)

    def test_get_department_name(self):
        """Test to get the name of the department"""
        self.assertEqual(self.department.get_name(), "Emergency")
        print(self.department)

    def test_get_get_statistics(self):
        """Test to get statistics of the department"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            self.department.update_entities()
            test_case = self.department.get_statistics()
            self.assertEqual(test_case.get_not_released_patient_num(), 2)
            self.assertEqual(test_case.get_released_patient_num(), 1)
            self.assertEqual(test_case.get_total_bill_amount_released_patients(), 500)

    def test_get_updated_entities(self):
        """Test to check a valid object is created correctly"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            self.department.update_entities()
            obj1 = self.department.get_person_by_type("Patient")
            obj2 = self.department.get_person_by_type("Doctor")
            self.assertEqual(len(obj1) + len(obj2), 5)

    def test_update_person(self):
        """Test update information of a person"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            with self.assertRaises(ValueError):
                self.department.update_person("P004", "Uy", "Tran", 600, 0, '3432 Newtons, Richmond, BC')
                self.department.update_person("P005", "Uy", "Tran", 600, 10000, '3432 Newtons, Richmond, BC')

    def test_to_dict(self):
        """Test to check to_dict() return an expected value"""
        with self.test_db.bind_ctx([Department, Doctor, Patient]):
            # self.department.remove_person_by_id('D005')
            self.D1 = self.department.to_dict()
            print(self.D1)
            self.D2 = {'name': 'Emergency',
                       'Patient': [
                           {'id': 'P006', 'first_name': 'Jose', 'last_name': 'McDonald',
                            'date_of_birth': '12-Dec-1970', 'address': '3432 Newtons, Richmond, BC',
                            'is_released': 'False', 'room_num': 590, 'bill': 0},
                           {'id': 'P007', 'first_name': 'Bill', 'last_name': 'Stark',
                            'date_of_birth': '02-Sep-1960', 'address': '1111 Columbia, New Westminster, BC',
                            'is_released': 'True', 'room_num': 589, 'bill': 500},
                           {'id': 'P004', 'first_name': 'Bill', 'last_name': 'Stark',
                            'date_of_birth': '02-Sep-1960', 'address': '1111 Columbia, New Westminster, BC',
                            'is_released': 'False', 'room_num': 589, 'bill': 0}
                       ],
                       'Doctor': [
                           {'id': 'D006', 'first_name': 'George', 'last_name': 'Bush',
                            'date_of_birth': '28-Feb-1982', 'address': '97334 Oak Bridge , Vancouver, Vancouver, BC',
                            'is_released': 'False', 'office_num': 125, 'income': 190000}
                       ]}
            self.assertDictEqual(self.D1, self.D2)

    @classmethod
    def tearDownClass(cls):
        """ Delete tables and Close connection """
        cls.test_db = SqliteDatabase("testing.db", pragmas={'ignore_check_constraints': 0})
        with cls.test_db.bind_ctx([Department, Doctor, Patient]):
            cls.test_db.drop_tables([Department, Doctor, Patient])
        cls.test_db.close()
