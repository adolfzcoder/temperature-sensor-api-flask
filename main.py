from flask import Flask, redirect, url_for, request, jsonify
import readSerial 
from flask_cors import CORS
import time
# readSerial.connect()

app = Flask(__name__)
@app.after_request
@app.after_request
def after_request(response):
    # To avoid errors related to "Permission denied" you have to add urls that might be using the app
    origin = request.headers.get('Origin')
    allowed_origins = [
        'https://adolfs-room-temperature.learnnamibia.com',
        'http://localhost:3000',  
        'http://127.0.0.1:3000',
        'http://localhost:8080',
        'http://127.0.0.1:8080',
        'file://',  # For local HTML files
        '*'  # Allow all origins 
    ]
    
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,ngrok-skip-browser-warning'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working', 'status': 'success'})
@app.route('/get_data/', methods=['GET', 'OPTIONS'])
def get_data():

    if request.method == 'OPTIONS':
        return '', 200
    type = request.args.get('type')

    if(type == 'tempc'):
        temp = readSerial.getAll()
        time.sleep(2)

        if(temp is None):
            return jsonify({'error': 'Sensor error'}), 500
        return jsonify({'temperature_celsius': temp})
    
    elif(type == 'tempf'):
        temp = readSerial.getTempF()
        time.sleep(2)

        if(temp is None):
            return jsonify({'error': 'Sensor error'}), 500
        return jsonify({'temperature_fahrenheit': temp})
    
    elif(type == 'humidity'):
        humidity = readSerial.getHumidity()
        time.sleep(2)
        if(humidity is None):
            return jsonify({'error': 'Sensor error'}), 500
        return jsonify({'humidity': humidity})
    
    elif(type == 'all'):
        data_obj = readSerial.getAll()
        time.sleep(2)

        if(data_obj is None):
            return jsonify({'error': 'Sensor error'}), 500
        return jsonify(data_obj.to_dict())
    
    else:
        return jsonify({'error': 'Invalid choice'}), 400
    
# readSerial.close()
if __name__ == '__main__':
    app.run(debug=True, port=4040)
