from accounting_stats import *


class Department():
    """"""

    def __init__(self, name: str, department: str):
        """"""
        self._name = name
        self._department = []

    def add_person(self, person: object):
        """"""
        self._department.append(person)

    def remove_person_by_id(self, id: str):
        """"""
        for obj in self._department:
            if obj.get_id == id:
                self._department.remove(obj)
            break

    def get_person_by_id(self, person: object):
        """"""
        for obj in self._department:
            if obj.get_id == id:
                return obj

    def person_exist(self, person: object):
        """"""
        for obj in self._department:
            if obj.get_id == id:
                return obj.is_released()

    def get_name(self):
        """"""
        return self._department

    def get_statistics(self):
        """"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_each_patient = []

        for obj in self._department:
            temp = []
            if obj.is_released:
                temp.extend([obj.get_id, obj.get_bill_amount])
                _released_num += 1
                _total_bill_each_patient.append(temp)
            else:
                _remaining_num += 1
        return AccountingStats(_released_num, _remaining_num, _total_bill_each_patient)
