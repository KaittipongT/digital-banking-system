from flask import Blueprint, request, jsonify
from database import get_db_connection

credit_cards_bp = Blueprint('credit_cards', __name__)

@credit_cards_bp.route('/issue', methods=['POST'])
def issue_card():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO Credit_Cards (user_id, card_number, card_type, credit_limit, balance) VALUES (?, ?, ?, ?, ?)',
                 (data['user_id'], data['card_number'], data['card_type'], data['credit_limit'], 0))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Credit card issued'})
