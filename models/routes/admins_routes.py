from __main__ import app, db
from flask import request
from models.admins import Admin 
#from datetime import datetime
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException
from format_respons import format_response






# Admin CRUD routes
#def admin(app):
@app.route('/admins', methods=['POST'])
def create_admin():
    try:
        data = request.get_json()
        new_admin = Admin(
            UserName=data['UserName'],
            email=data['email'],
            address=data['address'],
            authorety_level=data['authorety_level'],
            img=data.get('img')
        )
        new_admin.set_password(data['password'])  # Hash password before storing
        db.session.add(new_admin)
        db.session.commit()
        return format_response(new_admin.to_dict()), 201
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/admins', methods=['GET'])
def get_admins():
    try:
        admins = Admin.query.all()
        return format_response([admin.to_dict() for admin in admins])
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/admins/<int:id>', methods=['GET'])
def get_admin(id):
    try:
        admin = Admin.query.get(id)
        if admin is None:
            return format_response(error='Admin not found'), 404
        return format_response(admin.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/admins/<int:id>', methods=['PUT'])
def update_admin(id):
    try:
        data = request.get_json()
        admin = Admin.query.get(id)
        if admin is None:
            return format_response(error='Admin not found'), 404
        
        admin.UserName = data.get('UserName', admin.UserName)
        admin.email = data.get('email', admin.email)
        admin.address = data.get('address', admin.address)
        admin.authorety_level = data.get('authorety_level', admin.authorety_level)
        admin.img = data.get('img', admin.img)
        if 'password' in data:
            admin.set_password(data['password'])  # Update password if provided

        db.session.commit()
        return format_response(admin.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/admins/<int:id>', methods=['DELETE'])
def delete_admin(id):
    try:
        admin = Admin.query.get(id)
        if admin is None:
            return format_response(error='Admin not found'), 404
        db.session.delete(admin)
        db.session.commit()
        return format_response(message='Admin deleted successfully')
    except Exception as e:
        return format_response(error=str(e)), 400
