from __main__ import app, db

from flask import request
from models.users import User 
# from datetime import datetime
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException
from format_respons import format_response



# User CRUD routes
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(
            UserName=data['UserName'],
            email=data['email'],
            address=data['address'],
            img=data.get('img')
        )
        new_user.set_password(data['password'])  # Hash password before storing
        db.session.add(new_user)
        db.session.commit()
        return format_response(new_user.to_dict()), 201
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return format_response([user.to_dict() for user in users])
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return format_response(error='User not found'), 404
        return format_response(user.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        user = User.query.get(id)
        if user is None:
            return format_response(error='User not found'), 404
        
        user.UserName = data.get('UserName', user.UserName)
        user.email = data.get('email', user.email)
        user.address = data.get('address', user.address)
        user.img = data.get('img', user.img)
        if 'password' in data:
            user.set_password(data['password'])  # Update password if provided

        db.session.commit()
        return format_response(user.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return format_response(error='User not found'), 404
        db.session.delete(user)
        db.session.commit()
        return format_response(message='User deleted successfully')
    except Exception as e:
        return format_response(error=str(e)), 400
