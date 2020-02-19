

class AccountingStats:

    """"""
    def __init__(self, released_patient: int, not_released_patient: int, total_bill):
        """"""
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

