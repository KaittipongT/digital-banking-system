from flask import Blueprint, request, jsonify
from database import get_db_connection

loans_bp = Blueprint('loans', __name__)

@loans_bp.route('/apply', methods=['POST'])
def apply_loan():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO Loans (user_id, loan_type, amount, interest_rate, status) VALUES (?, ?, ?, ?, ?)',
                 (data['user_id'], data['loan_type'], data['amount'], data['interest_rate'], 'pending'))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Loan application submitted'})
