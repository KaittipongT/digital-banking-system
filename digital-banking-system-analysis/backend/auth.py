from flask import Blueprint, request, jsonify
import bcrypt
import jwt
import datetime
from database import get_db_connection

SECRET_KEY = "your_secret_key"

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    conn = get_db_connection()
    conn.execute('INSERT INTO Users (name, email, phone, address, password_hash) VALUES (?, ?, ?, ?, ?)',
                 (data['name'], data['email'], data['phone'], data['address'], hashed_password))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM Users WHERE email = ?', (data['email'],)).fetchone()
    conn.close()

    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password_hash']):
        token = jwt.encode({'user_id': user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                           SECRET_KEY, algorithm="HS256")
        return jsonify({'token': token})
    
    return jsonify({'error': 'Invalid credentials'}), 401
