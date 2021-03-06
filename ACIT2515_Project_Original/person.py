from abc import abstractmethod
from datetime import datetime


class Person:
    """Define a Person class"""

    def __init__(self, first_name: str, last_name: str, date_of_birth, address: str, id: int, is_released: bool):
        """Initialize a constructor of a Person instance"""
        self.validation(first_name, last_name, address, id)
        self._id = id
        self._firstName = first_name
        self._lastName = last_name
        self._date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self._address = address
        self._is_released = is_released

    def is_released(self):
        """Function to get the status of a Person object"""
        return self._is_released

    def get_id(self):
        """Function to get the ID of a Person object"""
        return self._id

    def get_firstName(self):
        """Function to get the first name of a Person object"""
        return self._firstName

    def get_lastName(self):
        """Function to get the last name of a Person object"""
        return self._lastName

    def get_date_of_birth(self) -> datetime:
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

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("This is an abstract method")

    @classmethod
    def validation(cls, first_name: str, last_name: str, address: str, id: int):
        """Function to validate type of all parameters"""
        if type(first_name) is not str:
            raise TypeError("First Name should be string.")
        if type(last_name) is not str:
            raise TypeError("Last Name should be string.")
        if type(address) is not str:
            raise TypeError("Address should be string.")
        if type(id) is not int:
            raise TypeError("Id should be integer.")
        if id <= 0:
            raise ValueError("Id should be more than 0.")