from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import HTTPException
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_jwt_extended import JWTManager,create_access_token
from flask_bcrypt import generate_password_hash, check_password_hash,Bcrypt

# Flask configurations and inheritances
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

from models.routes import admins_routes, book_routes , employee_routes , loans_routes,register_routes,users_routes
import format_respons


#**********************login+blueprint**********************888

# auth_bp = Blueprint('auth', __name__)
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     user = User.query.filter_by(email=email).first()

#     if user and bcrypt.check_password_hash(user.password, password):
#         access_token = create_access_token(identity=user.id)
#         return jsonify(access_token=access_token), 200
#     return jsonify({"msg": "Bad email or password"}), 401



    


if __name__ == "__main__":
    #admin(app)
    # Create the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)
