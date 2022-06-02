from flask import Flask, render_template, jsonify, request
import stripe, os
import json

stripe.api_key = 'sk_test_51L0zKlD28WDPIuZrS6pzBpPSSZWeu7yPodiaHx8kowH0WkIPaXqeM9PIpg4rxKVjNPf1ZoXMiZrVwIPWW9A55ukM00DBCT9ZmB'

app = Flask(__name__)

@app.route('/try_pay', methods=['GET'])
def try_pay():
    return render_template('checkout.html')

@app.route('/create-payment-intent', methods=['POST', 'GET'])
def create_payment():
    try:
        data = json.loads(request.data)
        #print(data)
        #donation = request.args.get("donationAmount", type=str)
        #print(donation)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=1500,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

