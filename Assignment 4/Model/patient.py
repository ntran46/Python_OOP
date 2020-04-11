from Model.abstract_person import Person
from peewee import IntegerField
import re

ID_REGEXP = r"^P\d+$"


class Patient(Person):
    """Define a Patient class"""

    PERSON_TYPE = 'Patient'

    room_num = IntegerField()
    bill = IntegerField(default=0)

    def save(self, *args, **kwargs):
        """ Validate input value before saving data """
        if self.bill is None:
            self.bill = 0
        elif self.bill is not None and self.bill >0:
            self.is_released = True
        elif type(self.bill) != int or self.bill < 0:
            raise ValueError("Invalid value! Bill payment must be greater than or equal 0, "
                             "and bill payment is an integer")
        if not self.room_num or type(self.room_num) != int or self.room_num <= 0 :
            raise ValueError("Invalid value! Room number must be greater than 0, and Room number is an integer")
        elif not re.match(ID_REGEXP, self.person_id):
            raise ValueError(f"Invalid ID {self.person_id}")
        return super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        """Return information of a person object"""
        return f"<{self.PERSON_TYPE}: {self.firstName} {self.lastName}>"

    def get_type(self):
        """Function to get the type of a Patient object"""
        return Patient.PERSON_TYPE

    def to_dict(self):
        output = dict()
        output["first_name"] = self.firstName
        output["last_name"] = self.lastName
        output["date_of_birth"] = self.date_of_birth
        output["address"] = self.address
        output["is_released"] = self.is_released
        output["id"] = self.person_id
        output["room_num"] = self.room_num
        output["bill"] = self.bill
        return output

    def get_description(self):
        """Function to get the description of a Patient object"""
        if self.is_released == 'True':
            print(f"The patient {self.firstName} {self.lastName}, ID number {self.id}, "
               f"born in {self.date_of_birth:%Y-%m-%d}, is recovered. The total bill is ${self.bill:,}. ")
        elif self.is_released == 'False':
            print(f"The patient {self.firstName} {self.lastName}, ID number {self.id}, "
               f"born in {self.date_of_birth:%Y-%m-%d}, is being treated in the room {self.room_num}.")
