from flask import Blueprint, request, jsonify
from database import get_db_connection

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/create', methods=['POST'])
def create_account():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO Accounts (user_id, account_number, account_type, balance) VALUES (?, ?, ?, ?)',
                 (data['user_id'], data['account_number'], data['account_type'], data['balance']))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Account created successfully'})
