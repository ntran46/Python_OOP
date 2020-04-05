from abstract_person import Person
from doctor import Doctor
from patient import Patient
from database import db

"""This is to connect to database and create 3 tables"""

db.create_tables([Person])
db.create_tables([Patient])
db.create_tables([Doctor])
