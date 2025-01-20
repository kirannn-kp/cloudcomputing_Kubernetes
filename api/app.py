from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow any origin (you can restrict this later for security reasons)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api', methods=['GET'])
def api():
    return jsonify(message="Hello from the Google cloud API!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
