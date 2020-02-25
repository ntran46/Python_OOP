from unittest import TestCase
from accounting_stats import AccountingStats

class TestAccountingStats(TestCase):
    def setUp(self) -> None:
        self.stats = AccountingStats(5, 100, 150000)

    def test_constructor(self):
        self.assertIsNotNone(self.stats)
        self.assertIsInstance(self.stats, AccountingStats)

        with self.assertRaises(TypeError):
            stats_1 = AccountingStats("5", 100, 150000)

        with self.assertRaises(TypeError):
            stats_2 = AccountingStats(5, "100", 150000)

        with self.assertRaises(TypeError):
            stats_3 = AccountingStats(5, 100, "150000")

        with self.assertRaises(ValueError):
            stats_4 = AccountingStats(5, 100, 200000)

        with self.assertRaises(ValueError):
            stats_4 = AccountingStats(0, 100, 150000)

        with self.assertRaises(ValueError):
            stats_4 = AccountingStats(5, 0, 150000)

    def test_get_released_patient_num(self):
        self.assertEqual(self.stats.get_released_patient_num(), 5)
        self.assertIsNotNone(self.stats.get_released_patient_num())

    def test_get_not_released_patient_num(self):
        self.assertEqual(self.stats.get_not_released_patient_num(), 100)
        self.assertIsNotNone(self.stats.get_not_released_patient_num())

    def test_get_total_bill_amount_each_person(self):
        self.assertEqual(self.stats.get_total_bill_amount_each_person(), 150000)
        self.assertIsNotNone(self.stats.get_total_bill_amount_each_person())