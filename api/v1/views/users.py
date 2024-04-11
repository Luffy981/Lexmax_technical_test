#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.users import Users
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/users/all_users.yml')
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(Users).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/users/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(Users, int(user_id))
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/users/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(Users, int(user_id))

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()
    return make_response("User successfully deleted", 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/users/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'name' not in request.get_json():
        abort(400, description="Missing email")
    if 'lastname' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    instance = Users(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/users/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(Users, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")
    
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'lastname' not in request.get_json():
        abort(400, description="Missing lastname")


    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)