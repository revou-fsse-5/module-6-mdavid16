def test_get_employees(client):
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_employee(client):
    new_employee = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "1234567890",
        "role": "Keeper",
        "schedule": "9-5"
    }
    response = client.post("/employees", json=new_employee)
    assert response.status_code == 201
    assert response.json["name"] == "John Doe"

def test_get_employee(client):
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json["name"] == "John Doe"

def test_update_employee(client):
    updated_employee = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone_number": "0987654321",
        "role": "Manager",
        "schedule": "8-4"
    }
    response = client.put("/employees/1", json=updated_employee)
    assert response.status_code == 200
    assert response.json["name"] == "Jane Doe"

def test_delete_employee(client):
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json["message"] == "Employee deleted"