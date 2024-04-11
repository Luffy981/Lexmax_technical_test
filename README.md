# 🚀 Backend Challenge

- [📝 Description](#-description)
- [💻 Development Scope](#-development-scope)
- [🛠 Execution Instructions](#-execution-instructions)
- [📄 Postman Documentation](#-postman-documentation)
- [📂 File and Code Structure](#-file-and-code-structure)
- [👨‍💻 Author](#-author)

## 📝 Description

Welcome to the backend challenge proposed by Lexmax! **Backend Challenge** is a Python API built with Flask to manage users. This API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on user data stored in an SQLite database.

## 💻 Development Scope

### Developed Features
- **User Creation:** Add a new user to the database by providing details such as name, last name, email, address, etc.
  
- **Fetch All Users:** Retrieve a list of all registered users in the database.

- **Fetch Specific User by ID:** Get information about a specific user using their unique ID.

- **Update User Information:** Update the information of an existing user using their unique ID.

- **Delete User by ID:** Delete a user from the database using their unique ID.

## 🛠 Execution Instructions

### Prerequisites
- Docker installed on your system.

### Steps to Run the Solution

1. **Clone the Repository:**
   
    ```
    git clone https://github.com/Luffy981/lexmax_technical_test.git
    ```

2. **Navigate to the Root of the Project:**

    ```
    cd lexmax_technical_test
    ```

3. **Build the Docker Image:**

    ```
    docker-compose build
    ```

4. **Start the Container:**

    ```
    docker-compose up
    ```

5. **Access the API:**
   
   The API will be available at `http://localhost:5000`.

6. **Access the API Documentation:**
   
   The API documentation will be available at `http://localhost:5000/apidocs/`.

7. **Interact with the API:**
   
   Use the routes and methods specified in the documentation to interact with the API and manage users.

## 📄 Postman Documentation

Explore the API endpoints and interact with them using Postman. View the detailed documentation [here](https://documenter.getpostman.com/view/27590507/2sA3Bhcu3z).

## 📂 File and Code Structure

The project follows the Model-View-Controller (MVC) pattern to separate concerns and organize code:

### 📁 Folder `api`
Contains files related to the Flask API.

- **`__init__.py`:** File indicating that the `api` folder is a Python package.
  
- **Folder `v1`:** Version 1 of the API.

  - **`app.py`:** Main file initializing the Flask application and defining routes.
  
  - **`index.py`:** Starting file for version 1 of the API.
  
  - **`__init__.py`:** File indicating that the `v1` folder is a Python package.
  
  - **Folder `views`:** Contains view controllers of the API.

    - **Folder `documentation`:** API documentation in YAML format.

    - **`index.py`:** Controller for the root route of the API.
    
    - **`__init__.py`:** File indicating that the `views` folder is a Python package.
    
    - **`users.py`:** Controller for user-related operations.

### 🗃️ File `database.db`
SQLite database file storing user data.

### 🐳 Files `docker-compose.yml` and `Dockerfile`
Files for Docker container configuration and build for the project.

### 🗂️ Folder `models`
Contains data models of the application.

- **`base_model.py`:** Defines the base class for all models.

- **Folder `engine`:** Contains the database storage engine.

  - **`db_storage.py`:** Defines the logic for interacting with the database.

  - **`__init__.py`:** File indicating that the `engine` folder is a Python package.

- **`__init__.py`:** File indicating that the `models` folder is a Python package.

### 📄 File `README.md`
The file you are currently reading, providing information about the project and its structure.

### 📋 File `requirements.txt`
List of project dependencies to be installed with pip.

This structure helps maintain organized code and facilitates project navigation and understanding.

## 👨‍💻 Author

**Smith Flores**
- GitHub: [Luffy981](https://github.com/Luffy981)
- LinkedIn: [Smith Flores](https://www.linkedin.com/in/smith-flores/)
