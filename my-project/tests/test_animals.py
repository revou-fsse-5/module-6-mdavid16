def test_get_animals(client):
    response = client.get("/animals")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_animal(client):
    new_animal = {
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "special_requirements": "None"
    }
    response = client.post("/animals", json=new_animal)
    assert response.status_code == 201
    assert response.json["species"] == "Lion"

def test_get_animal(client):
    response = client.get("/animals/1")
    assert response.status_code == 200
    assert response.json["species"] == "Lion"

def test_update_animal(client):
    updated_animal = {
        "species": "Tiger",
        "age": 6,
        "gender": "Female",
        "special_requirements": "None"
    }
    response = client.put("/animals/1", json=updated_animal)
    assert response.status_code == 200
    assert response.json["species"] == "Tiger"

def test_delete_animal(client):
    response = client.delete("/animals/1")
    assert response.status_code == 200
    assert response.json["message"] == "Animal deleted"