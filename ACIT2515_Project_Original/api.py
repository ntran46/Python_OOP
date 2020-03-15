from flask import Flask, jsonify, request, make_response
from department import Department
from patient import Patient

app = Flask(__name__)

department = Department("Emergency")

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
def list_patients():
    return jsonify(department.to_dict())

#
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
    app.run(debug=True)
