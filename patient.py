from person import Person


class Patient(Person):
    """Define a Patient class"""

    PERSON_TYPE = 'Patient'

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str, id: int, is_released: bool, room_num: int,
                 bill=0.0):
        """Initialize a constructor of a Patient object"""
        self.validate(room_num)
        self._room_num = room_num
        self._bill = bill
        super().__init__(first_name, last_name, date_of_birth, address, id, is_released)

    def is_released(self):
        """Function to get the status of a Patient object"""
        return self._is_released

    @property
    def bill(self):
        """"""
        return self._bill

    def set_bill(self, bill):
        """"""
        self._bill = bill

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

    def get_bill_amount(self):
        """Function to get the bill amount of a Patient object"""
        return self._bill

    @classmethod
    def validate(cls, room_num: int):
        """This is a class method that validates different possible type and value errors."""
        if room_num < 1 or type(room_num) is not int:
            raise ValueError("Room Number should be more than 0. Room number is an integer number.")

