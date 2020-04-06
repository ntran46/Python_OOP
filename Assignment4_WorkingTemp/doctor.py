from peewee import Model, IntegerField, CharField, DateField, Check, ForeignKeyField
from abstract_person import Person
# from department import Department

class Doctor(Person):
    """Define a Doctor class"""

    PERSON_TYPE = 'Doctor'

    """Initialize a constructor of a Doctor object"""
    # validate(office_num, income)
    office_num = IntegerField()
    person_id = CharField(unique=True)
    income = IntegerField()
    # department = ForeignKeyField(Department, backref='doctors')

    def __str__(self):
        """Return information of a person object"""
        return f"<{self.PERSON_TYPE}: {self.firstName} {self.lastName}>"

    def get_type(self):
        """Function to get the type of a Doctor object"""
        return Doctor.PERSON_TYPE

    def to_dict(self):
        output = dict()
        output["first_name"] = self.first_name
        output["last_name"] = self.last_name
        output["date_of_birth"] = self.date_of_birth
        output["address"] = self.address
        output["id"] = self.id
        output["is_released"] = self.is_released
        output["office_num"] = self.office_num
        output["income"] = self.income
        return output

    @classmethod
    def validate(cls, office_num: int, income: int):
        """This is a class method that validates different possible type and value errors."""
        if office_num < 1 or type(office_num) is not int:
            raise ValueError("Office Number should be more than 0. Office number is an integer number.")
        if income < 100000 or type(income) is not int:
            raise ValueError("Income should not be less than $100000 and Income should be an integer.")



    # def is_released(self):
    #     """Function to get the status of a Doctor object"""
    #     return self._is_released
    #
    # def set_first_name(self, first_name):
    #     if not first_name or type(first_name) is not str:
    #         raise ValueError("Invalid first name")
    #     self._firstName = first_name
    #
    # def set_last_name(self, last_name):
    #     if not last_name or type(last_name) is not str:
    #         raise ValueError("Invalid last name")
    #     self._lastName = last_name
    #
    # def set_office_num(self, office_num):
    #     if not office_num or type(office_num) is not int:
    #         raise ValueError("Invalid office number")
    #     self._office_num = office_num
    #
    # def set_income(self, income):
    #     if not income or type(income) is not int:
    #         raise ValueError("Invalid income")
    #     self._income = income
    #
    # def get_description(self):
    #     """Function to get the description of a Doctor object"""
    #     print(f"The doctor {self._firstName} {self._lastName}, ID number {self._id}, "
    #           f"born in {self._date_of_birth:%Y-%m-%d}, works in office room {self._office_num}.")


    #
    # def get_office_num(self):
    #     """Function to get the office number of a Doctor object"""
    #     return self._office_num
    #
    # def get_income_amount(self):
    #     """Function to get the income amount of a Doctor object"""
    #     return self._income