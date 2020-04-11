from Model.accounting_stats import AccountingStats
from Model.doctor import Doctor
from Model.patient import Patient

from database import db
from peewee import Model, CharField

"""This is the Department class which contains information all doctors and patients"""


class Department(Model):
    """Define a Department class"""

    """Initialize a constructor of a Department instance"""
    name = CharField()
    department = []

    class Meta:
        database = db

    def __str__(self):
        """ Print department information"""
        return f"<Department: {self.name}>"

    def update_entities(self):
        """Create entity from data loaded from database"""
        self.department = []
        doctor_list = Doctor.select()
        patient_list = Patient.select()

        for doctor in doctor_list:
            data = dict()
            data["id"] = doctor.person_id
            data["first_name"] = doctor.firstName
            data["last_name"] = doctor.lastName
            data["date_of_birth"] = doctor.date_of_birth.strftime("%d-%b-%Y")
            data["address"] = doctor.address
            data["is_released"] = doctor.is_released
            data["office_num"] = doctor.office_num
            data["income"] = doctor.income
            self.department.append(data)

        for patient in patient_list:
            data = dict()
            data["id"] = patient.person_id
            data["first_name"] = patient.firstName
            data["last_name"] = patient.lastName
            data["date_of_birth"] = patient.date_of_birth.strftime("%d-%b-%Y")
            data["address"] = patient.address
            data["is_released"] = patient.is_released
            data["room_num"] = patient.room_num
            data["bill"] = patient.bill
            self.department.append(data)

    def add_person(self, person: db):
        """Function to add a person to a department list"""
        person.save()
        self.department.append(person.to_dict())

    def remove_person_by_id(self, ID: str):
        """Function to remove a person out of a department list and database"""
        if not self.get_person_by_id(ID):
            raise ValueError("Person not found")
        else:
            if ID[0:1] == 'D':
                person = Doctor.select().where(Doctor.person_id == ID).get()
                person.delete_instance()
            if ID[0:1] == 'P':
                person = Patient.select().where(Patient.person_id == ID).get()
                person.delete_instance()
            self.update_entities()

    def get_person_by_id(self, ID: str):
        """Function to get an ID of a person in the list"""
        if type(ID) != str:
            return None
        elif ID[0:1] == 'D':
            person = Doctor.select().where(Doctor.person_id == ID)
            if person.exists():
                return Doctor.select().where(Doctor.person_id == ID).get()
            else:
                return None
        elif ID[0:1] == 'P':
            person = Patient.select().where(Patient.person_id == ID)
            if person.exists():
                return Patient.select().where(Patient.person_id == ID).get()
            else:
                return None

    def get_person_by_type(self, person_type: str):
        """Function is to give a description all people with a given type"""
        person_type_list = []
        if type(person_type) is not str:
            raise TypeError("The type input is not a string")

        for person in self.department:
            if person['id'][0:1] == person_type[0:1]:
                person_type_list.append(person)
        return person_type_list

    def get_all_current_people(self):
        """Function is return all people in a department"""
        for person in self.department:
            print(person)

    def person_exist(self, ID: str):
        """Function to check if a person belongs to the department"""
        if ID[0:1] == 'D':
            person = Doctor.select().where(Doctor.person_id == ID)
            if person.exists():
                return True
            else:
                return False
        if ID[0:1] == 'P':
            person = Patient.select().where(Patient.person_id == ID)
            if person.exists():
                return True
            else:
                return False

    def get_name(self):
        """Function to get name of a department"""
        return self.name

    def get_statistics(self):
        """Function to get statistics information from all patients"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_released_patients = 0

        for obj in self.department:
            if obj['id'][0:1] == 'P':
                if obj['is_released'] == 'True':
                    _released_num += 1
                    _total_bill_released_patients += obj['bill']
                else:
                    _remaining_num += 1
        return AccountingStats(_released_num, _remaining_num, _total_bill_released_patients)

    def to_dict(self):
        """ Return department instance state as dictionary """
        output = dict()
        output["name"] = self.name
        output["Patient"] = list()
        output["Doctor"] = list()
        for person in self.department:
            if person['id'][0:1] == 'P':
                output["Patient"].append(person)

            elif person['id'][0:1] == 'D':
                output["Doctor"].append(person)

        return output

    def update_person(self, person_id, first_name, last_name, office_room_num, bill_income, address):
        """ Updates information for the person with person_id
            Raises Exception if the student does not exist (or values are not correct) """

        person = self.get_person_by_id(person_id)
        if not person:
            raise ValueError("Person not in department")

        person.firstName = first_name
        person.lastName = last_name
        person.address = address

        if person.get_type() == 'Patient':
            person.room_num = office_room_num
            if bill_income > 0:
                person.bill = bill_income
                person.is_released = 'True'
            elif bill_income == 0:
                person.bill = 0
                person.is_released = 'False'
        if person.get_type() == 'Doctor':
            person.office_num = office_room_num
            person.income = bill_income
        person.save()
        self.update_entities()

    # def save(self, *args, **kwargs):
    #     """ Validate input value before saving data """
    #     if not self.income or type(self.income) != int or self.income < 0:
    #         raise ValueError("Invalid value! Income must be greater than or equal 0, and income is an integer")
    #     elif not self.office_num or type(self.office_num) != int or self.office_num <= 0:
    #         raise ValueError("Invalid value! Office number must be greater than 0, and office number is an integer")
    #     elif not re.match(ID_REGEXP, self.person_id):
    #         raise ValueError(f"Invalid ID {self.person_id}")
    #     return super(Doctor, self).save(*args, **kwargs)
