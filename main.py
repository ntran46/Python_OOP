from department import *
from doctor import Doctor
from patient import Patient


def print_report(department):
    """Print a report of a Department"""
    try:
        depart = department.get_statistics()

        print(f"Report for {department.get_name()} department:")
        print(f"  # of released patient: {depart.get_released_patient_num():d}")
        print(f"  # of current patient: {depart.get_not_released_patient_num():d}")
        print(f"  Total bill amount of all released patients: ${depart.get_total_bill_amount_released_patients():,.2f}\n")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    """Main function"""

    doctor1 = Doctor("Johnny", "Kenedy", "1984-1-30", "1444 Oakway, North Vancouver, Vancouver, BC", 1, False, 123, 150000)
    doctor2 = Doctor("George", "Bush", "1982-2-28", "97334 Oak Bridge , Vancouver, Vancouver, BC", 2, False, 125, 190000)
    patient1 = Patient("Jose", "McDonald", "1970-12-12", "3432 Newtons, Richmond, BC", 1,  False, 589, 3)
    patient2 = Patient("Bill", "Stark", "1960-9-2", "1111 Columbia, New Westminster, BC", 2, False, 589, 54600)
    patient3 = Patient("Jame", "O'Conner", "1966-8-1", "433 Bigbang, New Westminster, BC", 3, False, 610, 7500)
    patient4 = Patient("Bond", "Start", "1959-9-23", "131 Columbia, Burnaby, BC", 4,  False, 599, 5500)
    patient5 = Patient("Micheal", "Conner", "1969-8-1", "693 Bigbang, Surrey, BC", 5,  False, 610, 75000)

    print(doctor1.get_description())
    print(doctor1.get_type())

    print(patient1.get_description())
    print(patient1.get_type())

    print(patient2.get_description())

    patient1.bill = 10000
    print(patient1.get_description())

    department1 = Department("Surgery")
    department1.add_person(patient1)
    department1.add_person(patient2)
    department1.add_person(doctor2)
    department1.add_person(patient3)
    department1.add_person(patient4)
    department1.add_person(patient5)

    print_report(department1)










