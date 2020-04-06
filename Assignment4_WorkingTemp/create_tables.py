from abstract_person import Person
from department import Department
from doctor import Doctor
from patient import Patient
from database import db

"""This is to connect to database and create 3 tables"""
db.create_tables([Department])
db.create_tables([Patient])
db.create_tables([Doctor])


# Create initial data
Surrey = Department(name="Surrey")
Surrey.save()

doctor1 = Doctor(person_id='D001', firstName="Johnny", lastName="Kenedy", date_of_birth="1984-1-30",
                 address="1444 Oakway, North Vancouver, Vancouver, BC", is_released=0, office_num=123,
                 income=150000)
doctor1.save()
doctor2 = Doctor(person_id='D002', firstName="George", lastName="Bush", date_of_birth="1982-2-28",
                 address="97334 Oak Bridge , Vancouver, Vancouver, BC", is_released=0, office_num=125,
                 income=190000)
doctor2.save()
patient1 = Patient(person_id='P001', firstName="Jose", lastName="McDonald", date_of_birth="1970-12-12",
                   address="3432 Newtons, Richmond, BC", is_released=0, room_num=590)
patient1.save()
patient2 = Patient(person_id='P002', firstName="Bill", lastName="Stark", date_of_birth="1960-9-2",
                   address="1111 Columbia, New Westminster, BC", is_released=0, room_num=589)
patient2.save()
patient3 = Patient(person_id='P003', firstName="Jame", lastName="O'Conner", date_of_birth="1966-8-1",
                   address="433 Bigbang, New Westminster, BC", is_released=0, room_num=610)
patient3.save()
patient4 = Patient(person_id='P004', firstName="Bond", lastName="Start", date_of_birth="1959-9-23",
                   address="131 Columbia, Burnaby, BC", is_released=0, room_num=599)
patient4.save()
patient5 = Patient(person_id='P005', firstName="Micheal", lastName="Conner", date_of_birth="1969-8-1",
                   address="693 Bigbang, Surrey, BC", is_released=0, room_num=610)
patient5.save()
