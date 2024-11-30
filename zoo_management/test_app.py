import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)

    def test_get_employee(self):
        response = self.app.get('/employees/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Alice Smith')

    def test_get_employee_not_found(self):
        response = self.app.get('/employees/999')
        self.assertEqual(response.status_code, 404)

    def test_add_employee(self):
        new_employee = {"name": "Eve Adams", "position": "Security", "department": "Security"}
        response = self.app.post('/employees', json=new_employee)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["name"], "Eve Adams")

    def test_update_employee(self):
        updated_employee = {"name": "Alice Johnson", "position": "Senior Zookeeper", "department": "Mammals"}
        response = self.app.put('/employees/1', json=updated_employee)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Alice Johnson")

    def test_delete_employee(self):
        response = self.app.delete('/employees/1')
        self.assertEqual(response.status_code, 204)
        get_response = self.app.get('/employees/1')
        self.assertEqual(get_response.status_code, 404)

    def test_get_animals(self):
        response = self.app.get('/animals')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)

    def test_get_animal(self):
        response = self.app.get('/animals/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Lion')

    def test_get_animal_not_found(self):
        response = self.app.get('/animals/999')
        self.assertEqual(response.status_code, 404)

    def test_add_animal(self):
        new_animal = {"name": "Tiger", "species": "Panthera tigris"}
        response = self.app.post('/animals', json=new_animal)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["name"], "Tiger")

    def test_update_animal(self):
        updated_animal = {"name": "African Lion", "species": "Panthera leo"}
        response = self.app.put('/animals/1', json=updated_animal)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "African Lion")

    def test_delete_animal(self):
        response = self.app.delete('/animals/1')
        self.assertEqual(response.status_code, 204)
        get_response = self.app.get('/animals/1')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()