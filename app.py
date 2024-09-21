import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from src.routes import register_blueprints

load_dotenv()

app = Flask(__name__)

# Register routes
register_blueprints(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)