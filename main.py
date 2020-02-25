from department import *
from doctor import Doctor
from patient import Patient


if __name__ == "__main__":
    """Main function"""

    doctor1 = Doctor("Johnny", "Kenedy", "1984-1-30", "1444 Oakway, North Vancouver, Vancouver, BC", 123, 150000, 1)
    doctor2 = Doctor("George", "Bush", "1982-2-28", "97334 Oak Bridge , Vancouver, Vancouver, BC", 125, 190000, 2)
    patient1 = Patient("Jose", "McDonald", "1970-12-12", "3432 Newtons, Richmond, BC", 589, 3, 1)
    patient2 = Patient("Bill", "Stark", "1960-9-2", "1111 Columbia, New Westminster, BC", 589, 54600, 2)
    patient3 = Patient("Jame", "O'Conner", "1966-8-1", "433 Bigbang, New Westminster, BC", 610, 7500, 3)

    # try:
    #     doctor1.set_id(13)
    #     # doctor2.set_id(15)
    #     # patient1.set_id(100009)
    #     # patient2.set_id(100010)
    #     # patient3.set_id(100011)
    # except TypeError:
    #     print("Id should be an integer.")
    print(doctor1.get_description())
    print(doctor1.get_type())
    print(doctor2.get_description())
    print(patient1.get_description())
    print(patient1.get_type())
    print(patient2.get_description())
    patient1.bill = 10000
    print(patient1.get_description())
