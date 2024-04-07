from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")  # Allow all origins

@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    try:
        data = request.json  # get JSON data from the POST request
        print("Received POST request with body:", data)
        
        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
