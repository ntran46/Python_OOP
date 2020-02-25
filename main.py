from department import *
from doctor import Doctor
from patient import Patient


if __name__ == "__main__":
    """Main function"""

    doctor1 = Doctor("Johnny", "Kenedy", "Jan-30-1984", "1444 Oakway, North Vancouver, Vancouver, BC", 123, 150000)
    doctor2 = Doctor("George", "Bush", "Feb-28-1982", "97334 Oak Bridge , Vancouver, Vancouver, BC", 125, 190000)
    patient1 = Patient("Jose", "McDonald", "Dec-12-1970", "3432 Newtons, Richmond, BC", 589)
    patient2 = Patient("Bill", "Stark", "Nov-21-1960", "1111 Columbia, New Westminster, BC", 589, 54600)
    patient3 = Patient("Jame", "O'Conner", "Oct-1-1966", "433 Bigbang, New Westminster, BC", 610, 7500)

    doctor1.set_id(13)
    doctor2.set_id(15)
    patient1.set_id(100009)
    patient2.set_id(100010)
    patient3.set_id(100011)
    print(doctor1.get_description())
    print(doctor1.get_type())
    print(doctor2.get_description())
    print(patient1.get_description())
    print(patient1.get_type())
    print(patient2.get_description())
    patient1.bill = 10000
    print(patient1.get_description())
