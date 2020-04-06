from accounting_stats import AccountingStats
from doctor import Doctor
from patient import Patient

from database import db
from peewee import Model, IntegerField, CharField

"""This is the Department class which contains information all doctors and patients"""


class Department(Model):
    """Define a Department class"""

    """Initialize a constructor of a Department instance"""
    # self.validation(name)
    name = CharField()
    department = []
    # output = {"name": name, "Doctor": [], "Patient": []}

    class Meta:
        database = db

    # it works
    def update_entities(self):
        """Create entity from data loaded from database"""
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

    # it works
    def add_person(self, person: dict):
        """Function to add a person to a department list"""
        person.save()
        self.department.append(person)

    # it works
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

    # it works
    def get_person_by_id(self, ID: str):
        """Function to get an ID of a person in the list"""
        # try:
        if ID[0:1] == 'D':
            person = Doctor.select().where(Doctor.person_id == ID)
            if person.exists():
                return Doctor.select().where(Doctor.person_id == ID).get()
            else:
                return None
        if ID[0:1] == 'P':
            person = Patient.select().where(Patient.person_id == ID)
            if person.exists():
                return Patient.select().where(Patient.person_id == ID).get()
            else:
                return None

    # I think it should work, since this does not touch db
    def get_person_by_type(self, person_type: str):
        """Function is to give a description all people with a given type"""
        person_type_list = []
        if type(person_type) is not str:
            raise TypeError("The type input is not a string")

        for person in self.department:
            if person.get_type() == person_type:
                person_type_list.append(person.to_dict())
                person.get_description()
        return person_type_list

    # it works
    def get_all_current_people(self):
        """Function is return all people in a department"""
        for person in self.department:
            print(person)

    # it works
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

    # it works
    def get_name(self):
        """Function to get name of a department"""
        return self.name

    def get_statistics(self):
        """Function to get statistics information from all patients"""
        _released_num = 0
        _remaining_num = 0
        _total_bill_released_patients = 0

        for obj in self.department:
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
        output["name"] = self.name
        output["Patient"] = list()
        output["Doctor"] = list()
        for person in self.department:
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

    # @staticmethod
    # def validation(name):
    #     """ Validate input parameter"""
    #     if not name:
    #         raise ValueError("A department's name must be defined!")
    #     if type(name) is not str:
    #         raise TypeError("Name of the department should be a string.")

# For testing
if __name__ == "__main__":
    """Main function"""
    department = Department(name="Surrey")
    department.update_entities()
    # department.get_all_current_people()
    department.get_person_by_id('D001')
    # department.remove_person_by_id('D001')
    # department.get_person_by_id('D001')
    print(department.person_exist('D002'))
    print(department.person_exist('D001'))

    # This line below will return a peewee error due to UNIQUE constraint on person_id
    # when trying to save a record with the same person_id value
    # doctor1 = Doctor(person_id='D001', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
    #                  address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=0, office_num=123,
    #                  income=150000)
    # doctor1.save()
