from flask import Flask, request, jsonify
from negotiation_logic import handle_negotiation

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Negotiation Chatbot API. Use the /negotiate endpoint to interact."

@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.json
    user_input = data.get('user_input')
    user_price = data.get('user_price')

    if not user_price:
        return jsonify({"error": "User price is required"}), 400

    # Get bot's response for negotiation
    response = handle_negotiation(user_input, user_price)
    
    return jsonify({"bot_response": response})

if __name__ == '__main__':
    app.run(debug=True)
