from peewee import IntegerField
from Model.abstract_person import Person
import re

ID_REGEXP = r"^D\d+$"


class Doctor(Person):
    """Define a Doctor class"""

    PERSON_TYPE = 'Doctor'

    office_num = IntegerField()
    income = IntegerField()

    def save(self, *args, **kwargs):
        """ Validate input value before saving data """
        if not self.income or type(self.income) != int or self.income < 0:
            raise ValueError("Invalid value! Income must be greater than or equal 0, and income is an integer")
        elif not self.office_num or type(self.office_num) != int or self.office_num <= 0:
            raise ValueError("Invalid value! Office number must be greater than 0, and office number is an integer")
        elif not re.match(ID_REGEXP, self.person_id):
            raise ValueError(f"Invalid ID {self.person_id}")
        return super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        """Return information of a person object"""
        return f"<{self.PERSON_TYPE}: {self.firstName} {self.lastName}>"

    def get_type(self):
        """Function to get the type of a Doctor object"""
        return Doctor.PERSON_TYPE

    def to_dict(self):
        output = dict()
        output["first_name"] = self.firstName
        output["last_name"] = self.lastName
        output["date_of_birth"] = self.date_of_birth
        output["address"] = self.address
        output["id"] = self.person_id
        output["is_released"] = self.is_released
        output["office_num"] = self.office_num
        output["income"] = self.income
        return output

    def get_description(self):
        """Function to get the description of a Doctor object"""
        print(f"The doctor {self.firstName} {self.lastName}, ID number {self.id}, "
              f"born in {self.date_of_birth:%Y-%m-%d}, works in office room {self.office_num}.")
