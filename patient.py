from person import Person

""""""

class Patient(Person):
    """"""

    def __init__(self, firstname: str, lastname: str, dateOfBirth: str, address: str, status: bool, room_num: int, bill: float):
        """"""
        super().__init__(firstname, lastname, dateOfBirth, address, status)
        self._room_num = room_num
        self._bill = bill

    def get_description(self):
        """"""
        return

    def get_type(self):
        """"""
        return

    def get_room_num(self):
        """"""
        return self._room_num

    def get_bill_amount(self):
        """"""
        return self._bill


