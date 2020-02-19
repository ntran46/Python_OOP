from abc import *


class Person():
    """ """

    def __int__(self, firstname: str, lastname: str, dateOfBirth: str, address: str, status: bool):
        """"""

        self._id = 0
        self._firstname = firstname
        self._lastname  = lastname
        self._date_of_birth = dateOfBirth
        self._address = address
        self._status = status
        self._is_released = False

    @property
    def is_released(self):
        """"""
        return self._is_released

    @property
    def set_id(self, id):
        """"""
        self._id = id

    @property
    def get_id(self):
        """"""
        return self._id

    @property
    def get_firstname(self):
        """"""
        return self._firstname

    @property
    def get_lastname(self):
        """"""
        return self._lastname

    @property
    def get_date_of_birth(self):
        """"""
        return self._date_of_birth

    @property
    def get_address(self):
        """"""
        return self._address

    @abstractmethod
    def get_description(self):
        """"""
        raise NotImplementedError("")

    def  get_type(self):
        """"""
        raise NotImplementedError("")

