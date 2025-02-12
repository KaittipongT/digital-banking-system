from flask import Flask
from auth import auth_bp
from transactions import transactions_bp
from accounts import accounts_bp
from loans import loans_bp
from credit_cards import credit_cards_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(transactions_bp, url_prefix='/transactions')
app.register_blueprint(accounts_bp, url_prefix='/accounts')
app.register_blueprint(loans_bp, url_prefix='/loans')
app.register_blueprint(credit_cards_bp, url_prefix='/credit-cards')

if __name__ == '__main__':
    app.run(debug=True)
