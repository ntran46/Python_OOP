from flask import Flask, jsonify, request, make_response

from department import Department
from patient import Patient
from doctor import Doctor

app = Flask(__name__)
department = Department("Surgery")
doctor1 = Doctor("Johnny", "Kenedy", "1984-1-30", "1444 Oakway, North Vancouver, Vancouver, BC", 1, False, 123,
                 150000)
doctor2 = Doctor("George", "Bush", "1982-2-28", "97334 Oak Bridge , Vancouver, Vancouver, BC", 2, False, 125,
                 190000)
patient1 = Patient("Jose", "McDonald", "1970-12-12", "3432 Newtons, Richmond, BC", 1, False, 590)
patient2 = Patient("Bill", "Stark", "1960-9-2", "1111 Columbia, New Westminster, BC", 2, False, 589)
patient3 = Patient("Jame", "O'Conner", "1966-8-1", "433 Bigbang, New Westminster, BC", 3, False, 610)
patient4 = Patient("Bond", "Start", "1959-9-23", "131 Columbia, Burnaby, BC", 4, False, 599)
patient5 = Patient("Micheal", "Conner", "1969-8-1", "693 Bigbang, Surrey, BC", 5, False, 610)





@app.route("/department/person", methods=["POST"])
def add_patient():
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        # if Patient.PERSON_TYPE == 'Patient':
        patient = Patient(data["first_name"], data["last_name"],
                          data["date_of_birth"], data["address"], data["id"],
                          data["is_released"], data["room_num"], data["bill"])
        department.add_person(patient)
        return make_response(str(data["id"]), 200)
        # elif Patient.PERSON_TYPE == 'Doctor':
        #     doctor = Patient(data["first_name"], data["last_name"],
        #                       data["date_of_birth"], data["address"], data["id"],
        #                       data["is_released"], data["office_num"], data["income"])
        #     department.add_person(doctor)
        #     return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route("/department", methods=["GET"])
def list_employees():
    return jsonify(department.to_dict())


@app.route("/department/patient", methods=["GET"])
def list_patient():
    return jsonify(department.to_dict("","patient"))


@app.route("/department/doctor", methods=["GET"])
def list_doctor():
    return jsonify(department.to_dict("doctor"))


@app.route("/department/patient/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    return jsonify(department.get_person_by_id(patient_id).to_dict())


@app.route("/department/patient/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)

    patient = department.get_person_by_id(patient_id)
    if not patient:
        return make_response("Patient not found.", 400)

    if "first_name" not in data.keys():
        return make_response("Invalid JSON: missing first name", 400)

    try:
        department.update_patient(patient_id, data["first_name"])
        return make_response("OK", 200)
    except ValueError as e:
        return make_response(str(e), 404)

# @app.route("/school/student/<int:student_id>", methods=["DELETE"])
# def delete_student(student_id):
#     try:
#         school.remove_student(student_id)
#     except ValueError as e:
#         return make_response(str(e), 400)
#     else:
#         return make_response("", 204)


@app.route("/validate", methods=["GET", "POST", "PUT", "DELETE"])
def validate_setup():
    return jsonify(
        {
            "method": request.method,
            "Content-Type header": request.headers.get("Content-Type"),
            "data": request.data.decode(),
        }
    )


if __name__ == "__main__":
    department.add_person(patient1)

    department.add_person(patient2)
    department.add_person(doctor2)
    department.add_person(patient3)
    department.add_person(patient4)
    department.add_person(patient5)

    app.run(debug=True)
