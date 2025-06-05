from flask import Blueprint, jsonify

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"message": "Employee list endpoint", "status": "success"})

@employee_bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    return jsonify({"message": f"Employee {id} details", "status": "success"})