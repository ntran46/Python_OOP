from person import Person


class Patient(Person):
    """Define a Patient class"""

    PERSON_TYPE = 'Patient'

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str, room_num: int,
                 bill=0.0):
        """Initialize a constructor of a Patient object"""
        super().__init__(first_name, last_name, date_of_birth, address)
        self.validate_attributes([room_num, bill], (int, float))
        self._room_num = room_num
        self._bill = bill
        self._status = False
        self._is_released = False
        self._id = 0
        self._is_released = False

    @property
    def is_released(self):
        """Function to get the status of a Patient object"""
        return self._is_released

    @property
    def bill(self):
        """"""
        return self._bill

    @bill.setter
    def bill(self, bill):
        """"""
        self._bill = bill
        self._is_released = True

    def get_description(self):
        """Function to get the description of a Patient object"""
        if self._is_released:
            return f"The patient {self._firstName} {self._lastName}, ID number {self._id}, "\
               f"born in {self._date_of_birth}, is recovered. The total bill is ${self._bill:,}. "
        else:
            return f"The patient {self._firstName} {self._lastName}, ID number {self._id}, "\
               f"born in {self._date_of_birth}, is being treated in the room {self._room_num}."

    def get_type(self):
        """Function to get the type of a Patient object"""
        return Patient.PERSON_TYPE

    def get_room_num(self):
        """Function to get the room number of a Patient object"""
        return self._room_num

    def get_bill_amount(self):
        """Function to get the bill amount of a Patient object"""
        return self._bill


