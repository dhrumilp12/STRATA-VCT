import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from src.agents.ai_agents import conversation  # Adjusted import

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/ai-response', methods=['POST'])
def ai_response():
    user_input = request.json.get('input')

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    try:
        response = conversation.predict(input=user_input)
        print("AI Response:", response) 
        return jsonify({'reply': response})
    except Exception as error:
        print("Error:", error)
        return jsonify({'error': 'Error processing your request', 'details': str(error)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)