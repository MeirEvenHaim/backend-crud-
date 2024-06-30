from __main__ import app, db
from flask import request,jsonify
from models.loans import Loan
# from datetime import datetime
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.exceptions import HTTPException
from format_respons import format_response









@app.route('/loans', methods=['POST'])
def create_loan():
    try:
        data = request.get_json()
        new_loan = Loan(
            user_id=data['user_id'],
            admin_id=data['admin_id'],
            book_id=data['book_id']
        )
        db.session.add(new_loan)
        db.session.commit()
        return jsonify(new_loan.to_dict()), 201
    except Exception as e:
        return jsonify(error=str(e)), 400
        
@app.route('/loans', methods=['GET'])
def get_loans():
    try:
        loans = Loan.query.all()
        return jsonify([loan.to_dict() for loan in loans])
    except Exception as e:
        return jsonify(error=str(e)), 500
        
        
@app.route('/loans/<int:id>', methods=['GET'])
def get_loan(id):
    try:
        loan = Loan.query.get(id)
        if loan is None:
            return jsonify(error='Loan not found'), 404
        return jsonify(loan.to_dict())
    except Exception as e:
        return jsonify(error=str(e)), 500
        
@app.route('/loans/<int:id>', methods=['PUT'])
def update_loan(id):
    try:
        data = request.get_json()
        loan = Loan.query.get(id)
        if loan is None:
            return jsonify(error='Loan not found'), 404
        
        loan.user_id = data.get('user_id', loan.user_id)
        loan.admin_id = data.get('admin_id', loan.admin_id)
        loan.book_id = data.get('book_id', loan.book_id)
        
        db.session.commit()
        return jsonify(loan.to_dict())
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/loans/<int:id>', methods=['DELETE'])
def delete_loan(id):
    try:
        loan = Loan.query.get(id)
        if loan is None:
            return jsonify(error='Loan not found'), 404
        db.session.delete(loan)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify(error=str(e)), 400
