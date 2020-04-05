from accounting_stats import AccountingStats
from doctor import Doctor
from patient import Patient
import json

"""This is the Department class which contains information all doctors and patients"""


class Department:
    """Define a Department class"""

    def __init__(self, name: str):
        """Initialize a constructor of a Department instance"""
        self.validation(name)
        self._name = name
        self._department = []
        self._filepath = "people.json"
        self.output = {"name": self._name, "Doctor": [], "Patient": []}

    def create_entities(self, person_list, person_type):
        """Create entity from data loaded from file"""
        for data in person_list:
            datetime_object = data["date_of_birth"][0:-9]
            if person_type == 'Patient':
                person = Patient(data["first_name"], data["last_name"],
                                 datetime_object, data["address"], data["id"],
                                 data["is_released"], data["room_num"], data["bill"])
                self._department.append(person)
            elif person_type == 'Doctor':
                person = Doctor(data["first_name"], data["last_name"],
                                datetime_object, data["address"], data["id"],
                                data["is_released"], data["office_num"], data["income"])
                self._department.append(person)

    def add_person(self, person: object):
        """Function to add a person to a department list"""
        person_id = person.get_id()
        result = self.get_person_by_id(person_id)
        if result is not None:
            raise ValueError("This person is already added in the department list")
        else:
            self._department.append(person)

    def remove_person_by_id(self, ID: int):
        """Function to remove a person out of a department list"""
        check = False
        for obj in self._department:
            if obj.get_id() == ID:
                self._department.remove(obj)
                check = True
        if not check:
            raise ValueError(f"The id {ID} does not exist.")

    def get_person_by_id(self, ID: int):
        """Function to get an ID of a person in the list"""
        for obj in self._department:
            if obj.get_id() == ID:
                return obj

    def get_person_by_type(self, person_type: str):
        """Function is to give a description all people with a given type"""
        person_type_list = []
        if type(person_type) is not str:
            raise TypeError("The type input is not a string")

        for person in self._department:
            if person.get_type() == person_type:
                person_type_list.append(person.to_dict())
                person.get_description()
        return person_type_list

    def get_all_current_people(self):
        """Function is return all people in a department"""
        for person in self._department:
            person.get_description()

    def person_exist(self, ID: int):
        """Function to check if a person belongs to the department"""
        for obj in self._department:
            if obj.get_id() == ID:
                return True
            else:
                return False

    def get_name(self):
        """Function to get name of a department"""
        return self._name

    def get_statistics(self):
        """Function to get statistics information from all patients"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_released_patients = 0

        for obj in self._department:
            if obj.get_type() == 'Patient':
                if obj.is_released():
                    _released_num += 1
                    _total_bill_released_patients += obj.bill
                else:
                    _remaining_num += 1
        return AccountingStats(_released_num, _remaining_num, _total_bill_released_patients)

    def to_dict(self):
        """ Return department instance state as dictionary """
        output = dict()
        output["name"] = self._name
        output["Patient"] = list()
        output["Doctor"] = list()
        for person in self._department:
            if person.get_type() == 'Patient':
                output["Patient"].append(person.to_dict())

            elif person.get_type() == 'Doctor':
                output["Doctor"].append(person.to_dict())

        return output

    def update_person(self, person_id, first_name, last_name, office_room_num, bill_income):
        """ Updates name for the person <student_id>
            Raises Exception if the student does not exist (or values are not correct) """

        person = self.get_person_by_id(person_id)
        if not person:
            raise ValueError("Patient not in department")

        if person.get_type() == 'Patient':
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_room_num(office_room_num)
            person.bill = bill_income
        if person.get_type() == 'Doctor':
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_office_num(office_room_num)
            person.set_income(bill_income)

    @staticmethod
    def validation(name):
        """ Validate input parameter"""
        if not name:
            raise ValueError("A department's name must be defined!")
        if type(name) is not str:
            raise TypeError("Name of the department should be a string.")


    # def _read_from_file(self, filePath=""):
    #     """Read content from a file as a JSON and create entities accordingly"""
    #     if filePath == "":
    #         filePath = self._filepath
    #
    #     with open(filePath) as file:
    #         data = json.load(file)
    #         for person1 in data["Doctor"]:
    #             self.output["Doctor"].append(person1)
    #         for person2 in data["Patient"]:
    #             self.output["Patient"].append(person2)
    #
    #     self.create_entities(self.output["Patient"], "Patient")
    #     self.create_entities(self.output["Doctor"], "Doctor")
    #     return self.output

    #
    # def _write_to_file(self):
    #     """Export the entities as a JSON serialized list in the file"""
    #     temp = self.to_dict()
    #     with open(self._filepath, "w") as file:
    #         json.dump(temp, file, default=str)
