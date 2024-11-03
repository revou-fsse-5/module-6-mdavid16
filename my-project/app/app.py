from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Path to the JSON file
DATA_FILE = 'zoo_data.json'

# Initialize the JSON file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"animals": [], "employees": []}, f)

# Helper function to read data from the JSON file
def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Helper function to write data to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Animal Management Endpoints
@app.route('/animals', methods=['GET'])
def get_animals():
    data = read_data()
    return jsonify(data['animals'])

@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    data = read_data()
    animal = next((a for a in data['animals'] if a['id'] == id), None)
    if animal:
        return jsonify(animal)
    return jsonify({"error": "Animal not found"}), 404

@app.route('/animals', methods=['POST'])
def add_animal():
    data = read_data()
    new_animal = request.json
    new_animal['id'] = len(data['animals']) + 1
    data['animals'].append(new_animal)
    write_data(data)
    return jsonify(new_animal), 201

@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    data = read_data()
    animal = next((a for a in data['animals'] if a['id'] == id), None)
    if animal:
        animal.update(request.json)
        write_data(data)
        return jsonify(animal)
    return jsonify({"error": "Animal not found"}), 404

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    data = read_data()
    animal = next((a for a in data['animals'] if a['id'] == id), None)
    if animal:
        data['animals'].remove(animal)
        write_data(data)
        return jsonify({"message": "Animal deleted"})
    return jsonify({"error": "Animal not found"}), 404

# Employee Management Endpoints
@app.route('/employees', methods=['GET'])
def get_employees():
    data = read_data()
    return jsonify(data['employees'])

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    data = read_data()
    employee = next((e for e in data['employees'] if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employees', methods=['POST'])
def add_employee():
    data = read_data()
    new_employee = request.json
    new_employee['id'] = len(data['employees']) + 1
    data['employees'].append(new_employee)
    write_data(data)
    return jsonify(new_employee), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = read_data()
    employee = next((e for e in data['employees'] if e['id'] == id), None)
    if employee:
        employee.update(request.json)
        write_data(data)
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    data = read_data()
    employee = next((e for e in data['employees'] if e['id'] == id), None)
    if employee:
        data['employees'].remove(employee)
        write_data(data)
        return jsonify({"message": "Employee deleted"})
    return jsonify({"error": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)