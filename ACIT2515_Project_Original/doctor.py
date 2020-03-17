from person import Person
from datetime import datetime


class Doctor(Person):
    """Define a Doctor class"""

    PERSON_TYPE = 'Doctor'

    def __init__(self, first_name: str, last_name: str, date_of_birth, address: str, id: int, is_released: bool, office_num: int,
                 income: int):
        """Initialize a constructor of a Doctor object"""
        self.validate(office_num, income)
        self._office_num = office_num
        self._income = income
        super().__init__(first_name, last_name, date_of_birth, address, id, is_released)

    def is_released(self):
        """Function to get the status of a Doctor object"""
        return self._is_released

    def get_description(self):
        """Function to get the description of a Doctor object"""
        print(f"The doctor {self._firstName} {self._lastName}, ID number {self._id}, "
              f"born in {self._date_of_birth:%Y-%m-%d}, works in office room {self._office_num}.")

    def get_type(self):
        """Function to get the type of a Doctor object"""
        return Doctor.PERSON_TYPE

    def get_office_num(self):
        """Function to get the office number of a Doctor object"""
        return self._office_num

    def get_income_amount(self):
        """Function to get the income amount of a Doctor object"""
        return self._income

    def to_dict(self):
        output = dict()
        output["first_name"] = self._firstName
        output["last_name"] = self._lastName
        output["date_of_birth"] = self._date_of_birth
        output["address"] = self._address
        output["id"] = self._id
        output["is_released"] = self._is_released
        output["office_num"] = self._office_num
        output["income"] = self._income
        return output

    @classmethod
    def validate(cls, office_num: int, income: int):
        """This is a class method that validates different possible type and value errors."""
        if office_num < 1 or type(office_num) is not int:
            raise ValueError("Office Number should be more than 0. Office number is an integer number.")
        if income < 100000 or type(income) is not int:
            raise ValueError("Income should not be less than $100000. Income should be an integer.")

