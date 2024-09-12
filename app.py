import requests
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# D-ID API key and Agent ID
DID_API_KEY = 'ZW1tYW51ZWxkb3JsZXk2MDlAZ21haWwuY29t:TrEj1-zNarqcuUGyhIIXR'
DID_AGENT_ID = 'agt_bMG9ba0R'

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Track user interactions (start, stop, input/output)
@app.route('/track', methods=['POST'])
def track_interaction():
    data = request.json
    action = data.get('action')
    content = data.get('content', '')

    # Log the interaction
    with open('user_interactions.log', 'a') as f:
        f.write(json.dumps({
            "action": action,
            "content": content,
            "timestamp": data.get('timestamp')
        }) + '\n')

    return jsonify({"status": "success", "message": f"Action '{action}' recorded"})

if __name__ == '__main__':
    app.run(debug=True)
