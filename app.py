"""
Money Transfer Application - Python Flask Implementation
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Constants
SENDING_FEES = 0.02
EXCHANGE_RATE = 655

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', 
                          sending_fees=SENDING_FEES, 
                          exchange_rate=EXCHANGE_RATE)

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate transfer amounts and fees"""
    try:
        # Get amount from request
        data = request.get_json()
        user_amount = float(data.get('amount', 0))
        
        # Calculate values
        fee_amount = SENDING_FEES * user_amount
        amount_plus_fees = user_amount + fee_amount
        receiving_amount = EXCHANGE_RATE * user_amount
        
        # Return calculation results
        return jsonify({
            'user_amount': user_amount,
            'fee_amount': fee_amount,
            'amount_plus_fees': amount_plus_fees,
            'receiving_amount': receiving_amount,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

@app.route('/process', methods=['POST'])
def process_payment():
    """Process the payment (simulated)"""
    # In a real application, this would connect to a payment processor
    # For this demo, we'll just return success
    return jsonify({'success': True, 'message': 'Payment processed successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)