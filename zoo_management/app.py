from flask import Flask, request, jsonify, abort

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Alice Smith", "position": "Zookeeper", "department": "Mammals"},
    {"id": 2, "name": "Bob Johnson", "position": "Veterinarian", "department": "Medical"},
    {"id": 3, "name": "Charlie Brown", "position": "Guide", "department": "Tours"},
    {"id": 4, "name": "Diana Prince", "position": "Manager", "department": "Administration"}
]

animals = [
    {"id": 1, "name": "Lion", "species": "Panthera leo"},
    {"id": 2, "name": "Elephant", "species": "Loxodonta"},
    {"id": 3, "name": "Penguin", "species": "Aptenodytes forsteri"},
    {"id": 4, "name": "Giraffe", "species": "Giraffa camelopardalis"}
]

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

if __name__ == '__main__':
    app.run(debug=True)



