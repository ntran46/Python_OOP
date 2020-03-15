from accounting_stats import AccountingStats

"""This is the Department class which contains information all doctors and patients"""


class Department:
    """Define a Department class"""

    def __init__(self, name: str):
        """Initialize a constructor of a Department instance"""
        self.validation(name)
        self._name = name
        self._department = []
        # self._patient = dict()

    def add_person(self, person: object):
        """Function to add a person to a department list"""
        self._department.append(person)

    def remove_person_by_id(self, id: int):
        """Function to remove a person out of a department list"""
        check = False
        for obj in self._department:
            if obj.get_id() == id:
                self._department.remove(obj)
                check = True
        if not check:
            raise ValueError(f"The id {id} does not exist.")

    def get_person_by_id(self, id: int):
        """Function to get an ID of a person in the list"""
        check = False
        for obj in self._department:
            if obj.get_id() == id:
                return obj
        if not check:
            raise ValueError(f"The id {id} does not exist.")

    def get_person_by_type(self, person_type: str):
        """Function is to give a description all people with a given type"""
        type_flat = 0
        if type(person_type) is not str:
            raise TypeError("The type input is not a string")

        for person in self._department:
            if person.get_type() == person_type:
                person.get_description()
                type_flat += 1

        if type_flat == 0:
            return f"There is no type \"{person_type}\" of person in the department {self._name}."

    def get_all_current_people(self):
        """Function is return all people in a department"""
        for person in self._department:
            person.get_description()

    def person_exist(self, id: int):
        """Function to check if a person belongs to the department"""
        for obj in self._department:
            if obj.get_id() == id:
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
        output = dict()
        output["name"] = self._name
        output["patient"] = list()
        for patient in self._department:
            output["patient"].append(patient.to_dict())
        return output

    def update_patient(self, patient_id, first_name):
        """ Updates name for the student <student_id>
            Raises Exception if the student does not exist (or values are not correct) """

        patient = self.get_person_by_id(patient_id)
        if not patient:
            raise ValueError("Patient not in department")

        patient.set_first_name(first_name)

    @staticmethod
    def validation(name):
        if type(name) is not str:
            raise TypeError("Name of the department should be a string.")
