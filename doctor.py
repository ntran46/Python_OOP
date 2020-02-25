from person import Person


class Doctor(Person):
    """Define a Doctor class"""

    PERSON_TYPE = 'Doctor'

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str, id: int, office_num: int,
                 income: int):
        """Initialize a constructor of a Doctor object"""
        super().__init__(first_name, last_name, date_of_birth, address, id)
        # self.validate_attributes([office_num, income], (int))
        self._office_num = office_num
        self._income = income
        self._status = False
        self._is_released = False

    @property
    def is_released(self):
        """Function to get the status of a Doctor object"""
        return self._is_released

    def get_description(self):
        """Function to get the description of a Doctor object"""
        return f"The doctor {self._firstName} {self._lastName}, ID number {self._id}, "\
               f"born in {self._date_of_birth:%Y-%m-%d}, works in office room {self._office_num}."

    def get_type(self):
        """Function to get the type of a Doctor object"""
        return Doctor.PERSON_TYPE

    def get_office_num(self):
        """Function to get the office number of a Doctor object"""
        return self._office_num

    def get_income_amount(self):
        """Function to get the income amount of a Doctor object"""
        return self._income


