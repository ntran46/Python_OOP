from .database import db
from models.doctor import Doctor
from models.abstract_person import Person
from models.patient import Patient
"""This is to connect to database and drop tables"""


db.drop_tables([Person, Doctor, Patient])