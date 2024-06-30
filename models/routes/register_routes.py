from __main__ import app, db

from flask import  request
from models.register import Register
from flask_bcrypt import bcrypt 
# from datetime import datetime
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException
from format_respons import format_response




# Register CRUD routes ...
@app.route('/register', methods=['POST'])
def create_register():
    try:
        data = request.get_json()
        password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_register = Register(
            UserName=data['UserName'],
            email=data['email'],
            password=password_hash
        )
        db.session.add(new_register)
        db.session.commit()
        return format_response(new_register.to_dict()), 201
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/registers', methods=['GET'])
def get_registers():
    try:
        registers = Register.query.all()
        return format_response([register.to_dict() for register in registers])
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/register/<int:id>', methods=['GET'])
def get_register(id):
    try:
        register = Register.query.get(id)
        if register is None:
            return format_response(error='Register not found'), 404
        return format_response(register.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/register/<int:id>', methods=['PUT'])
def update_register(id):
    try:
        data = request.get_json()
        register = Register.query.get(id)
        if register is None:
            return format_response(error='Register not found'), 404
        register.UserName = data['UserName']
        register.email = data['email']
        register.password = data['password']
        db.session.commit()
        return format_response(register.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/register/<int:id>', methods=['DELETE'])
def delete_register(id):
    try:
        register = Register.query.get(id)
        if register is None:
            return format_response(error='Register not found'), 404
        db.session.delete(register)
        db.session.commit()
        return format_response(message='Register deleted successfully')
    except Exception as e:
        return format_response(error=str(e)), 400
