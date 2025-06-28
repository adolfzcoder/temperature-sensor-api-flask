# Temperature & Humidity Sensor Flask API

Using Python and Arduino/C++ to communicate through Flask.
For this project, we use an Arduino Uno R3 and a Flask API server to communicate the temperate and humidity data with a web client.

## Configuration

* **clone the repo with https://github.com/adolfzcoder/temperature-sensor-api-flask.git**
* Identify the ports which your arduino is connected to, uncomment the code below in `readSerial.py`
```python
ports = serial.tools.list_ports.comports()
portList = []
for i in ports:
	portList.append(str(i))
	print(str(i))
```
if on Linux/Mac, it should be something like this ``/dev/ttyUSB0``, if on windows should be `COM3` for example, but to make sure, open your Arduino IDE and check which port the Arduino is connected to. Once that is completed, replace the default port with your port in the function for connecting `def  connect(port='/dev/ttyUSB0', baudrate=9600):`

## API
* Download and Install https://ngrok.com/
* Set up ngrok: https://www.youtube.com/watch?v=9vDANAYiPMo&pp=ygULbmdyb2sgZmxhc2s%3D
* In `main.py` do start the flask server. This server will be operating on the default port of 4040, make sure when you are starting ngrok server it should also be on port 4040
* Do note, the app should be served from the same directory where `main.py` is, `C/User/Github/temperature-sensor-api-flask`
* To start the ngrok server, use `ngrok http 4040`
* Once server address/url is obtained, use that in the client app
