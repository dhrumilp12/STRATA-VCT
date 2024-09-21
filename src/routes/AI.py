
from flask import Blueprint, request
from flask import jsonify
from src.agents.ai_agents import conversation  

ai_routes = Blueprint("ai", __name__)

@ai_routes.route('/ai-response', methods=['POST'])
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