
"""This is the AccountingStats class which shows the statistics of the accounting department of the hospital"""
class AccountingStats:

    """"""
    def __init__(self, released_patient: int, not_released_patient: int, total_bill):
        """"""
        self.validation(released_patient, not_released_patient, total_bill)
        self._released_patient_num = released_patient
        self._not_released_patient_num = not_released_patient
        self._total_bill_amount_each_person = total_bill

    def get_released_patient_num(self):
        """"""
        return self._released_patient_num

    def get_not_released_patient_num(self):
        """"""
        return self._not_released_patient_num

    def get_total_bill_amount_each_person(self):
        """"""
        return self._total_bill_amount_each_person

    @classmethod
    def validation(cls, released_patient: int, not_released_patient: int, total_bill: int):
        if released_patient < 1 or type(released_patient) is not int:
            raise ValueError("Released patient numbers cannot be 0. It should be "
                             "more than 0. Released patient numbers should be an "
                             "integer.")
        if not_released_patient < 1 or type(not_released_patient) is not int:
            raise ValueError("Patients who are not released yet cannot be 0. "
                             "They should be more than 0. Number of patients who "
                             "are not released yet should be an integer.")
        if total_bill >= 200000 or type(total_bill) is not int:
            raise ValueError("Total bill of a patient cannot be more than $200000."
                             " Total bill of patients should be an integer.")
