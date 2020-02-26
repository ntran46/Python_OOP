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

    def remove_person_by_id(self, id: int):
        """Function to remove a person out of a department list"""
        check = False
        for obj in self._department:
            if obj.get_id() == id:
                self._department.remove(obj)
                check = True
        if not check:
            raise ValueError(f"The id {id} does not exist.")

    def get_person_by_id(self, id: int):
        """Function to get an ID of a person in the list"""
        check = False
        for obj in self._department:
            if obj.get_id() == id:
                return obj
        if not check:
            raise ValueError(f"The id {id} does not exist.")

    def person_exist(self, id: int):
        """Function to check if a person belongs to the department"""
        for obj in self._department:
            if obj.get_id() == id:
                return True
            else:
                return False

    def get_name(self):
        """Function to get name of a department"""
        return self._name

    def get_statistics(self):
        """Function to get statistics information from all patients"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_released_patients = 0

        for obj in self._department:
            if obj.get_type() == 'Patient':
                if obj.is_released():
                    _released_num += 1
                    _total_bill_released_patients += obj.bill
                else:
                    _remaining_num += 1
        return AccountingStats(_released_num, _remaining_num, _total_bill_released_patients)

    @staticmethod
    def validation(name):
        if type(name) is not str:
            raise TypeError("Name of the department should be a string.")
