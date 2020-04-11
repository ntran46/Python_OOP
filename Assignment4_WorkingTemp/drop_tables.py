from database import db
from Model.doctor import Doctor
from Model.department import Department
from Model.patient import Patient

"""This is to connect to database and drop tables"""

db.drop_tables([Department, Doctor, Patient])
