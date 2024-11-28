from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data
animals = [
    {"id": 1, "species": "Lion", "age": 5, "gender": "Male", "special_requriments": "None"},
    {"id": 2, "species": "Elephant", "age": 10, "gender": "Female", "special_requriments": "Large Enclosure"},
]

employees = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "1234567890", "role": "Zookeeper", "schedule": "9am-5pm"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "phone": "0987654321", "role": "Veterinarian", "schedule": "10am-6pm"},
]

# Animal Management Endpoints
@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = next((animal for animal in animals if animal["id"] == id), None)
    if animal is None:
        abort(404)
    return jsonify(animal)

@app.route('/animals', methods=['POST'])
def add_animal():
    new_animal = request.json
    new_animal["id"] = len(animals) + 1
    animals.append(new_animal)
    return jsonify(new_animal), 201

@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = next((animal for animal in animals if animal["id"] == id), None)
    if animal is None:
        abort(404)
    updated_data = request.json
    animal.update(updated_data)
    return jsonify(animal)

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = next((animal for animal in animals if animal["id"] == id), None)
    if animal is None:
        abort(404)
    animals.remove(animal)
    return '', 204

# Employee Management Endpoints

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((employee for employee in employees if employee["id"] == id), None)
    if employee is None:
        abort(404)
    return jsonify(employee)

@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((employee for employee in employees if employee["id"] == id), None)
    if employee is None:
        abort(404)
    updated_data = request.json
    employee.update(updated_data)
    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = next((employee for employee in employees if employee["id"] == id), None)
    if employee is None:
        abort(404)
    employees.remove(employee)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)