from __main__ import app, db
from format_respons import format_response
from flask import request
from models.employee import Employe
# from datetime import datetime
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException




# Employe CRUD routes
@app.route('/employes', methods=['POST'])
def create_employe():
    try:
        data = request.get_json()
        new_employe = Employe(
            UserName=data.get('UserName'),
            email=data.get('email'),
            address=data.get('address'),
            img=data.get('img'),
            expertees=data.get('expertees')
        )
        db.session.add(new_employe)
        db.session.commit()
        return format_response(new_employe.to_dict()), 201
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/employes', methods=['GET'])
def get_employes():
    try:
        employes = Employe.query.all()
        return format_response([employe.to_dict() for employe in employes])
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/employes/<int:id>', methods=['GET'])
def get_employe(id):
    try:
        employe = Employe.query.get(id)
        if employe is None:
            return format_response(error='Employe not found'), 404
        return format_response(employe.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 500

@app.route('/employes/<int:id>', methods=['PUT'])
def update_employe(id):
    try:
        data = request.get_json()
        employe = Employe.query.get(id)
        if employe is None:
            return format_response(error='Employe not found'), 404
        
        employe.UserName = data.get('UserName', employe.UserName)
        employe.email = data.get('email', employe.email)
        employe.address = data.get('address', employe.address)
        employe.img = data.get('img', employe.img)
        employe.expertees = data.get('expertees', employe.expertees)
        
        db.session.commit()
        return format_response(employe.to_dict())
    except Exception as e:
        return format_response(error=str(e)), 400

@app.route('/employes/<int:id>', methods=['DELETE'])
def delete_employe(id):
    try:
        employe = Employe.query.get(id)
        if employe is None:
            return format_response(error='Employe not found'), 404
        db.session.delete(employe)
        db.session.commit()
        return 'file hs been deleted', 204
    except Exception as e:
        return format_response(error=str(e)), 400