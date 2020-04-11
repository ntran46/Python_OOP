from datetime import datetime

from flask import Flask, jsonify, request, make_response

from Model.department import Department
from Model.patient import Patient
from Model.doctor import Doctor

app = Flask(__name__)
department = Department(name="Surgery")
department.save()
department.update_entities()


@app.route("/department/<person_type>", methods=["POST"])
def add_person(person_type):
    data = request.json
    _dateObj = data["date_of_birth"]
    _strObj = datetime.strptime(_dateObj, "%d-%b-%Y")
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    print(data["date_of_birth"])
    person = department.get_person_by_id(data['id'])
    if person:
        return make_response("Invalid record! Person ID already exists.", 404)

    try:
        if data['id'][0:1] == 'P' and person_type == 'Patient':
            person = Patient(firstName=data["first_name"], lastName=data["last_name"],
                             date_of_birth=_strObj, address=data["address"], person_id=data["id"],
                             is_released=data["is_released"], room_num=data["room_num"], bill=data["bill"])
            department.add_person(person)

        elif data['id'][0:1] == 'D' and person_type == 'Doctor':
            person = Doctor(firstName=data["first_name"], lastName=data["last_name"],
                            date_of_birth=_strObj, address=data["address"], person_id=data["id"],
                            is_released=data["is_released"], office_num=data["office_num"], income=data["income"])
            department.add_person(person)
        else:
            return make_response(f"Invalid ID {data['id']} for {person_type} type", 404)
        return make_response(f"Person record (ID: {str(data['id'])}) has been added successfully.", 200)
    except Exception as err:
        return make_response("Cannot add a person record to the department due to: " + str(err), 400)


# it works
@app.route("/department/person/all", methods=["GET"])
def list_persons():
    department.update_entities()
    return make_response(jsonify(department.to_dict()), 200)


# it works
@app.route("/department/persons/all/<string:person_type>", methods=["GET"])
def get_person_by_type(person_type):
    person = department.get_person_by_type(person_type)
    if not person:
        return make_response("Person Not Found.", 400)

    return make_response(jsonify(department.get_person_by_type(person_type)), 200)

# it works
@app.route("/department/person/<string:person_id>", methods=["GET"])
def get_person(person_id):
    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)
    try:
        return make_response(jsonify(department.get_person_by_id(person_id).to_dict()), 200)
    except AttributeError as err:
        return make_response(f"Cannot get a person (ID: {str(person_id)}) record in the department due to: " + str(err), 404)

# it works
@app.route("/department/persons/stats", methods=["GET"])
def get_stats():
    return make_response(jsonify(department.get_statistics().to_dict()), 200)

# it works
@app.route("/department/person/<person_type>/<string:person_id>", methods=["PUT"])
def update_person(person_id, person_type):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 404)

    update_key = ["first_name", "last_name", "office_room_num", "bill_income", "address"]

    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)

    for key in update_key:
        if key not in data.keys():
            return make_response("Invalid value! There is an empty attribute's value.", 404)

    try:
        if person_type == 'Patient':
            department.update_person(person_id, data["first_name"], data["last_name"],
                                     data["office_room_num"], data["bill_income"], data["address"])
            return make_response(f"Patient record (ID: {str(person_id)}) has been updated successfully.", 200)
        elif person_type == 'Doctor':
            department.update_person(person_id, data["first_name"], data["last_name"],
                                     data["office_room_num"], data["bill_income"], data["address"])
            return make_response(f"Doctor record (ID: {str(person_id)}) has been updated successfully.", 200)
    except Exception as err:
        return make_response("Update record error due to: " + str(err), 404)


@app.route("/department/person/<string:person_id>", methods=["DELETE"])
def delete_person(person_id):
    person = department.get_person_by_id(person_id)
    if not person:
        return make_response("Person not found.", 404)
    department.remove_person_by_id(person_id)
    return make_response(f"Person record (ID: {str(person_id)}) has been removed successfully.", 200)


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
