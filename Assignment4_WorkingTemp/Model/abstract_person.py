from abc import abstractmethod
from peewee import DateField, CharField, IntegerField, Model
from database import db


class Person(Model):
    """Define a Person class"""

    """Initialize a constructor of a Person instance"""
    firstName = CharField()
    lastName = CharField()
    person_id = CharField(unique=True)
    date_of_birth = DateField()
    address = CharField()
    is_released = CharField(default=False)

    class Meta:
        """Declare the database variable"""
        database = db

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

    def __str__(self):
        """Return information of a person object"""
        return f"<Person: {self.firstName} {self.lastName})>"
