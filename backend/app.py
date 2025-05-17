from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # این خط برای اجازه ارتباط بین React و Flask لازم است

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)