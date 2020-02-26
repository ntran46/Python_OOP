from unittest import TestCase
from accounting_stats import AccountingStats


class TestAccountingStats(TestCase):

    """This is a test class to test the AccountingStats class"""

    def setUp(self) -> None:
        """Initialize setup object"""
        self.stats = AccountingStats(5, 100, 150000)

    def test_valid_constructor(self):
        """Test an object is created correctly"""
        self.assertIsNotNone(self.stats)
        self.assertIsInstance(self.stats, AccountingStats)

    def test_invalid_constructor(self):
        """Test an object with invalid parameters"""
        with self.assertRaises(TypeError):
            stats_1 = AccountingStats("5", 100, 150000)

        with self.assertRaises(TypeError):
            stats_2 = AccountingStats(5, "100", 150000)

        with self.assertRaises(TypeError):
            stats_3 = AccountingStats(5, 100, "150000")

        with self.assertRaises(ValueError):
            stats_4 = AccountingStats(5, 100, 200000)

        with self.assertRaises(ValueError):
            stats_5 = AccountingStats(0, 100, 150000)

        with self.assertRaises(ValueError):
            stats_6 = AccountingStats(5, 0, 150000)

    def test_get_released_patient_num(self):
        """Test to get the total number of released patients"""
        self.assertEqual(self.stats.get_released_patient_num(), 5)
        self.assertIsNotNone(self.stats.get_released_patient_num())

    def test_get_not_released_patient_num(self):
        """Test to get the total number of current patients"""
        self.assertEqual(self.stats.get_not_released_patient_num(), 100)
        self.assertIsNotNone(self.stats.get_not_released_patient_num())

    def test_get_total_bill_amount_released_patients(self):
        """Test to get the total amount of all released patients"""
        self.assertEqual(self.stats.get_total_bill_amount_released_patients(), 150000)
        self.assertIsNotNone(self.stats.get_total_bill_amount_released_patients())