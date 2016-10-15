import serial
from time import time

class SensorSerialView():

    def __init__(self):
        print 'try to connect'
        self.sensor = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)
        print("connected to: " + self.sensor.portstr)

    def getValues(self):
        values = []
        # while len(values) != 4:
        # value = self.sensor.readline()

        value = self.sensor.read(1)
        while value != '+': #caracter de inicio
            value = self.sensor.read(1)
        sensorValue = []
        value = self.sensor.read(1)
        while value != '/': #caracter de fin
            if value != '-': #caracter de separacion
                sensorValue.append(value)
            else:
                values.append(sensorValue)
                sensorValue = []
            value = self.sensor.read(1)
        values.append(sensorValue)
        self.sensor.flushInput()
        # print values
        sensors = []
        for valueCode in values:
            result = 0
            for i in range(0, len(valueCode)):
                if not valueCode[i] == '':
                    result += int(valueCode[i]) * (10 ** (len(valueCode) - i - 1))
            sensors.append(str(result))
        # print sensors
        return sensors