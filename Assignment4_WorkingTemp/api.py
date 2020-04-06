from flask import Flask, jsonify, request, make_response

from department import Department
from patient import Patient
from doctor import Doctor
from database import db
import re

PATIENT_ID_REGEXP = r"^P\d+$"
DOCTOR_ID_REGEXP = r"^D\d+$"

app = Flask(__name__)
department = Department("Surgery")


@app.route("/department/<person_type>", methods=["POST"])
def add_person(person_type):
    data = request.json

# ==>> I'm not sure this line should be here or in GUI validation. In my opinion, I prefer in GUI
    if not re.match(DOCTOR_ID_REGEXP, data["id"]) or not re.match(PATIENT_ID_REGEXP, data["id"]):
        raise ValueError("Invalid ID " + data["id"])

    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        if person_type == 'Patient':
            person = Patient(data["first_name"], data["last_name"],
                              data["date_of_birth"], data["address"], data["id"],
                              data["is_released"], data["room_num"], data["bill"])
            department.add_person(person)

        elif person_type == 'Doctor':
            person = Doctor(data["first_name"], data["last_name"],
                            data["date_of_birth"], data["address"], data["id"],
                            data["is_released"], data["office_num"], data["income"])
            department.add_person(person)

        else:
            return make_response("Type not found", 400)

        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

# ==>> Need to catch error which says UNIQUE constraint in person_id



@app.route("/department/person/all", methods=["GET"])
def list_persons():
    return make_response(jsonify(department.to_dict()), 200)


@app.route("/department/persons/all/<person_type>", methods=["GET"])
def get_book_by_type(person_type):
    person = department.get_person_by_type(person_type)
    if not person:
        return make_response("Person Not Found.", 400)

    return make_response(jsonify(department.get_person_by_type(person_type)), 200)


@app.route("/department/person/<int:person_id>", methods=["GET"])
def get_person(person_id):
    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)
    try:
        return make_response(jsonify(department.get_person_by_id(person_id).to_dict()), 200)
    except AttributeError as e:
        return make_response(str(e), 404)


@app.route("/department/persons/stats", methods=["GET"])
def get_stats():
    return make_response(jsonify(department.get_statistics().to_dict()), 200)


@app.route("/department/person/<person_type>/<int:person_id>", methods=["PUT"])
def update_patient(person_id, person_type):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 404)

    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)

    if "first_name" not in data.keys():
        return make_response("Invalid JSON: missing first name", 404)
    if "last_name" not in data.keys():
        return make_response("Invalid JSON: missing last name", 404)

    if person_type == 'Patient':
        if "room_num" not in data.keys():
            return make_response("Invalid JSON: missing room number", 404)
        if "is_released" not in data.keys():
            return make_response("Invalid JSON: missing released status", 404)

    if person_type == 'Doctor':
        if "office_num" not in data.keys():
            return make_response("Invalid JSON: missing office number", 404)
    try:
        if person_type == 'Patient':
            department.update_person(person_id, data["first_name"], data["last_name"], data["room_num"], data["bill"])
        elif person_type == 'Doctor':
            department.update_person(person_id, data["first_name"], data["last_name"], data["office_num"], data["income"])

        return make_response("OK", 200)
    except ValueError as e:
        return make_response(str(e), 404)


@app.route("/department/person/<int:person_id>", methods=["DELETE"])
def delete_person(person_id):
    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)
    department.remove_person_by_id(person_id)
    return make_response("OK", 200)
# ==>> Need to revise the return result from get_person_by_id

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
    app.run(debug=True)
