from models.abstract_person import Person
from peewee import Model, IntegerField, CharField

class Patient(Person):
    """Define a Patient class"""

    PERSON_TYPE = 'Patient'

    # def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str, id: int, is_released: bool, room_num: int,
    #              bill=0.0):
    #     """Initialize a constructor of a Patient object"""
    #     self.validate(room_num)
    room_num = IntegerField()
    bill = IntegerField()
    # super().__init__(first_name, last_name, date_of_birth, address, id, is_released)

    def is_released(self):
        """Function to get the status of a Patient object"""
        return self._is_released

    def set_first_name(self, first_name):
        if not first_name or type(first_name) is not str:
            raise ValueError("Invalid first name")
        self._firstName = first_name

    def set_last_name(self, last_name):
        if not last_name or type(last_name) is not str:
            raise ValueError("Invalid last name")
        self._lastName = last_name

    def set_room_num(self, room_num):
        if not room_num or type(room_num) is not int:
            raise ValueError("Invalid room number")
        self._room_num = room_num

    @property
    def bill(self):
        """Function to get the bill for a patient"""
        return self._bill

    @bill.setter
    def bill(self, value):
        """Function to set the bill for a patient"""
        self._bill = value
        self._is_released = True

    def get_description(self):
        """Function to get the description of a Patient object"""
        if self._is_released:
            print(f"The patient {self._firstName} {self._lastName}, ID number {self._id}, "
               f"born in {self._date_of_birth:%Y-%m-%d}, is recovered. The total bill is ${self._bill:,}. ")
        else:
            print(f"The patient {self._firstName} {self._lastName}, ID number {self._id}, "
               f"born in {self._date_of_birth:%Y-%m-%d}, is being treated in the room {self._room_num}.")

    def get_type(self):
        """Function to get the type of a Patient object"""
        return Patient.PERSON_TYPE

    def get_room_num(self):
        """Function to get the room number of a Patient object"""
        return self._room_num

    def to_dict(self):
        output = dict()
        output["first_name"] = self._firstName
        output["last_name"] = self._lastName
        output["date_of_birth"] = self._date_of_birth
        output["address"] = self._address
        output["is_released"] = self._is_released
        output["id"] = self._id
        output["room_num"] = self._room_num
        output["bill"] = self._bill
        return output

    def __str__(self):
        return f"<Patient {self._firstName} {self._lastName} ({self._id})"

    @classmethod
    def validate(cls, room_num: int):
        """This is a class method that validates different possible type and value errors."""
        if room_num <= 0 or type(room_num) is not int:
            raise ValueError("Room Number should be more than 0. Room number is an integer number.")
