from abc import *


class Person:
    """Define a Person class"""

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, address: str):
        """Initialize a constructor of a Person instance"""
        self.validate_attributes([first_name, last_name, address, date_of_birth], (str,))
        self._id = 0
        self._firstName = first_name
        self._lastName = last_name
        self._date_of_birth = date_of_birth
        self._address = address
        self._status = False
        self._is_released = False

    @property
    def is_released(self):
        """Function to get the status of a Person object"""
        return self._is_released

    def set_id(self, id):
        """Function to set the ID of a Person object"""
        self.validate_attributes([id], (int,))
        self._id = id

    def get_id(self):
        """Function to get the ID of a Person object"""
        return self._id

    def get_firstName(self):
        """Function to get the first name of a Person object"""
        return self._firstName

    def get_lastName(self):
        """Function to get the last name of a Person object"""
        return self._lastName

    def get_date_of_birth(self):
        """Function to get the DOB of a Person object"""
        return self._date_of_birth

    def get_address(self):
        """Function to get the address of a Person object"""
        return self._address

    @abstractmethod
    def get_description(self):
        """Abstract method to print a description of the Person object"""
        raise NotImplementedError("This is an abstract method")

    @abstractmethod
    def get_type(self):
        """Abstract method to print a type of the Person object"""
        raise NotImplementedError("This is an abstract method")

    @staticmethod
    def validate_attributes(val: list, type_check):
        """Function to validate type of all parameters"""
        for element in val:
            if type(element) not in type_check:
                raise TypeError("Invalid Type value for the attribute")