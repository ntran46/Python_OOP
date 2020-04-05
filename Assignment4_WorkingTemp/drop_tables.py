from database import db
from doctor import Doctor
from abstract_person import Person
from patient import Patient
"""This is to connect to database and drop tables"""


db.drop_tables([Person, Doctor, Patient])