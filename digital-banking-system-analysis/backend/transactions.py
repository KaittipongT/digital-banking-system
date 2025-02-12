from flask import Blueprint, request, jsonify
from database import get_db_connection

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    conn = get_db_connection()
    
    sender = conn.execute('SELECT balance FROM Accounts WHERE account_number = ?', (data['sender_account'],)).fetchone()
    receiver = conn.execute('SELECT balance FROM Accounts WHERE account_number = ?', (data['receiver_account'],)).fetchone()

    if not sender or not receiver:
        return jsonify({'error': 'Invalid account details'}), 400

    if sender['balance'] < data['amount']:
        return jsonify({'error': 'Insufficient funds'}), 400

    conn.execute('UPDATE Accounts SET balance = balance - ? WHERE account_number = ?', (data['amount'], data['sender_account']))
    conn.execute('UPDATE Accounts SET balance = balance + ? WHERE account_number = ?', (data['amount'], data['receiver_account']))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Transfer successful'})
