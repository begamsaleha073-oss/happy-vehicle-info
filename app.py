from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = 'wasdark'
API_URL = 'http://dark-op.dev-is.xyz/'

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/vehicle/<vehicle_number>')
def get_vehicle_info(vehicle_number):
    try:
        response = requests.get(f'{API_URL}?key={API_KEY}&vehicle={vehicle_number}')
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch vehicle data'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)