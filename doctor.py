from person import Person

""""""


class Doctor(Person):
    """"""

    def __init__(self, firstname: str, lastname: str, dateOfBirth: str, address: str, status: bool, office_num: int,
                 income: float):
        """"""
        super().__init__(firstname, lastname, dateOfBirth, address, status)
        self._office_num = office_num
        self._income = income

    def get_description(self):
        """"""
        return

    def get_type(self):
        """"""
        return

    def get_office_num(self):
        """"""
        return self._office_num

    def get_income_amount(self):
        """"""
        return self._income


