from accounting_stats import AccountingStats

"""This is the Department class which contains information all doctors and patients"""


class Department:
    """Define a Department class"""

    def __init__(self, name: str):
        """Initialize a constructor of a Department instance"""
        self.validation(name)
        self._name = name
        self._department = []

    def add_person(self, person: object):
        """Function to add a person to a department list"""
        self._department.append(person)

    def remove_person_by_id(self, id: str):
        """Function to remove a person out of a department list"""
        for obj in self._department:
            if obj.get_id == id:
                self._department.remove(obj)

    def get_person_by_id(self, id: str):
        """Function to get an ID of a person in the list"""
        for obj in self._department:
            if obj.get_id == id:
                return obj

    def person_exist(self, id: str):
        """Function to check if a person belongs to the department"""
        for obj in self._department:
            if obj.get_id == id:
                return obj.is_released()

    def get_name(self):
        """Function to get name of a department"""
        return self._department

    def get_statistics(self):
        """Function to get statistics information from all patients"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_released_patients = 0

        for obj in self._department:
            if obj.is_released:
                _released_num += 1
                _total_bill_released_patients += obj.get_bill_amount
            else:
                _remaining_num += 1
        return AccountingStats(_released_num, _remaining_num, _total_bill_released_patients)

    @staticmethod
    def validation(name):
        if type(name) is not str:
            raise TypeError("Name of the department should be a string.")
