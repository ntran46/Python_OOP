
"""This is the AccountingStats class which shows the statistics of the accounting department of the hospital"""

class AccountingStats:

    """Define the AccountingStats class"""

    def __init__(self, released_patient: int, not_released_patient: int, total_bill):
        """Initialize a constructor of a AccountingStats object"""
        self.validation(released_patient, not_released_patient, total_bill)
        self._released_patient_num = released_patient
        self._not_released_patient_num = not_released_patient
        self._total_bill_amount_released_patients = total_bill

    def get_released_patient_num(self):
        """Function to get the total number of patient that is being treated"""
        return self._released_patient_num

    def get_not_released_patient_num(self):
        """Function to get the total number of patient that is covered"""
        return self._not_released_patient_num

    def get_total_bill_amount_released_patients(self):
        """Function to get the total bill amount of all released patient"""
        return self._total_bill_amount_released_patients

    def to_dict(self):
        """ Return department instance state as dictionary """
        output = dict()
        output["released_patient"] = self._released_patient_num
        output["not_released_patient"] = self._not_released_patient_num
        output["total_bill"] = self._total_bill_amount_released_patients
        return output

    @classmethod
    def validation(cls, released_patient: int, not_released_patient: int, total_bill: int):
        """Function to validate all attributes"""
        if type(released_patient) is not int:
            raise TypeError("Released patient numbers should be an "
                             "integer.")
        if released_patient < 0:
            raise ValueError("Released patient numbers cannot be smaller than 0. It should be "
                             "at least 0.")
        if type(not_released_patient) is not int:
            raise TypeError("Number of patients who "
                             "are not released yet should be an integer.")
        if not_released_patient < 0:
            raise ValueError("Patients who are not released yet cannot be smaller than 0. "
                             "They should be at least 0.")
        if total_bill >= 200000 or type(total_bill) is not int:
            raise ValueError("Total bill of a patient cannot be more than $200000."
                             " Total bill of patients should be an integer.")
