#!/usr/bin/python3
import unittest
from api.v1.app import app
from models import storage, DBStorage
import json
from models.users import Users

class TestAPI(unittest.TestCase):
    """
    A comprehensive set of tests for the API endpoints.

    This test suite verifies the functionality of various API endpoints
    including retrieving users, retrieving a specific user, creating a new user,
    updating an existing user, and deleting a user.
    """

    def setUp(self):
        """
        Preparation steps before each test case.

        This method is called before each individual test case is run.
        It sets up necessary resources and environment for testing.
        """
        self.app = app.test_client()
        self.db = storage
        self.db.reload()

        # Create a test user
        self.test_user = Users(email='test@example.com', name='Test', lastname='User')
        self.test_user.save()

    def tearDown(self):
        """
        Clean-up steps after each test case.

        This method is called after each individual test case is run.
        It cleans up any resources or environment set up in setUp() method.
        """
        self.db.close()

    def test_get_users(self):
        """
        Test retrieving all users.

        This test case verifies that the API endpoint for retrieving all users
        returns a successful response with status code 200.
        """
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))

    def test_get_user(self):
        """
        Test retrieving a specific user.

        This test case verifies that the API endpoint for retrieving a specific user
        returns a successful response with status code 200 when given a valid user ID.
        """
        user_id = self.test_user.id
        response = self.app.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))

    def test_delete_user(self):
        """
        Test deleting a user.

        This test case verifies that the API endpoint for deleting a user
        successfully removes the user from the system and returns a status code of 200.
        """
        user_id = self.test_user.id
        response = self.app.delete(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(storage.get(Users, user_id))

    def test_post_user(self):
        """
        Test creating a new user.

        This test case verifies that the API endpoint for creating a new user
        successfully adds the user to the system and returns a status code of 201.
        """
        user_data = {
            'email': 'test@example.com',
            'name': 'Test',
            'lastname': 'User'
        }
        response = self.app.post('/api/v1/users', json=user_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(data['id'])

    def test_put_user(self):
        """
        Test updating an existing user.

        This test case verifies that the API endpoint for updating an existing user
        successfully modifies the user's information and returns a status code of 200.
        """
        user_id = self.test_user.id
        user_data = {
            'email': 'updated@example.com',
            'name': 'Updated',
            'lastname': 'User'
        }
        response = self.app.put(f'/api/v1/users/{user_id}', json=user_data)
        self.assertEqual(response.status_code, 200)
        updated_user = storage.get(Users, user_id)
        self.assertEqual(updated_user.email, user_data['email'])
        self.assertEqual(updated_user.name, user_data['name'])
        self.assertEqual(updated_user.lastname, user_data['lastname'])

if __name__ == '__main__':
    unittest.main()
