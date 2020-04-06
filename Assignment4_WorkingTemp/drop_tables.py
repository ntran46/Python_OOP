from database import db
from doctor import Doctor
from abstract_person import Person
from department import Department
from patient import Patient

"""This is to connect to database and drop tables"""

db.drop_tables([Department, Doctor, Patient])
