import serial.tools.list_ports
import time
from Data import Data 
# ports = serial.tools.list_ports.comports()

arduinoData = None


def connect(port="COM3", baudrate=9600):
    
    global arduinoData
    if arduinoData is None or not arduinoData.is_open:
        arduinoData = serial.Serial(port, baudrate)
        time.sleep(2)
        print("COM3 port open")

    else:
        print("Error in connection")

# connect()
def close() -> None:
    global arduinoData

    if arduinoData and arduinoData.is_open:
        arduinoData.close()
        print("Port closed")

def getTempC() -> float:
    connect()

    arduinoData.write(b'getTempC\r')
    data = arduinoData.readline().decode().strip()
    if data == "ERR":
        return None
    return float(data)

def getTempF() -> float:
    connect()

    arduinoData.write(b'getTempF\r')
    data = arduinoData.readline().decode().strip()
    if data == "ERR":
        return None
    return float(data)

def getHumidity() -> float:
    connect()

    arduinoData.write(b'getHumidity\r')
    data = arduinoData.readline().decode().strip()
    if data == "ERR":
        return None
    return float(data)

def getAll():
    connect()

    arduinoData.write(b'getAll\r')
    data = arduinoData.readline().decode().strip()

    if data == "ERR":
        return None
    try:
        h, tC, tF = map(float, data.split(","))
        d =  Data(tC, tF, h)
        return d
    except ValueError:
        return {"error": "Malformed data"}

def on() -> str:

    arduinoData.write(b'ON\r')
    print("led on")
    data = arduinoData.readline().decode().strip()
    if data == "ERR":
        return "ERR"
    return "LED is ON"
    
def off() -> str:

    arduinoData.write(b'OFF\r')
    data = arduinoData.readline().decode().strip()
    print("LED OFF")
    if data == "ERR":
        return None
    return "LED is OFF"

def decideReturn(c: str):
    
    match c:
        case "getTempC":
            val = getTempC()
        case "getTempF":
            val = getTempF()
        case "getHumidity":
            val = getHumidity()
        case "getAll":
            val = getAll()
        case "ON":
            val = on()
        case "OFF":
            val = off()
        case _:
            val = "ERROR WRONG CHOICE"
    return val



if __name__ == "__main__":
    # connect()
    print("Test")
# while True:

#     cmd = input("Enter your command: ")
#     val = decideReturn(cmd)
#     print(val)





    #packet = arduinoData.readline()
    #print(packet.decode('utf'))


