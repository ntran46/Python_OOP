from unittest import TestCase
from department import Department

class TestDepartment(TestCase):
    def setUp(self) -> None:
        self.department = Department("Emergency")

    def test_constructor(self):
        self.assertIsNotNone(self.department)
        self.assertIsInstance(self.department, Department)

        with self.assertRaises(TypeError):
            department_1 = Department("Surgery")

    def test_add_person(self, person: object):
        self.assertIn(self.department.add_person(person), self._department)
        self.assertIsNotNone(self.department.add_person(person))

    def test_get_not_released_patient_num(self):
        self.assertEqual(self.department.get_not_released_patient_num(), 100)
        self.assertIsNotNone(self.department.get_not_released_patient_num())

    def test_get_total_bill_amount_each_person(self):
        self.assertEqual(self.department.get_total_bill_amount_each_person(), 150000)
        self.assertIsNotNone(self.department.get_total_bill_amount_each_person())