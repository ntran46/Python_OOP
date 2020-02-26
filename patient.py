from person import Person


class Patient(Person):
    """Define a Patient class"""

    PERSON_TYPE = 'Patient'

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str, id: int, is_released: bool, room_num: int,
                 bill: int):
        """Initialize a constructor of a Patient object"""
        self.validate(room_num, bill)
        self._room_num = room_num
        self._bill = bill
        super().__init__(first_name, last_name, date_of_birth, address, id, is_released)

    def is_released(self):
        """Function to get the status of a Patient object"""
        return self._is_released

    def get_bill(self):
        """"""
        return self._bill

    def set_bill(self, bill):
        """"""
        if type(bill) is not int:
            raise TypeError("Bill should be an integer.")
        if bill > 200000:
            raise ValueError("Bill should not be more than $200000.")
        self._bill = bill

    def get_description(self) -> None:
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
    def validate(cls, room_num: int, bill: int):
        """This is a class method that validates different possible type and value errors."""
        if room_num < 1:
            raise ValueError("Room Number should be more than 0.")
        if type(room_num) is not int:
            raise TypeError("Room number is an integer number.")
        if bill > 200000:
            raise ValueError("Bill should not be more than $200000.")
        if type(bill) is not int:
            raise TypeError("Bill should be an integer.")


