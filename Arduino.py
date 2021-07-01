import serial
import time
from threading import *

class Arduino:
    def __init__(self):
        PORT = 'COM10'
        BAUDRATE = 115200
        TIMEOUT = .1

        self.arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
        self.command = "!def#"
    
    def sendCommand(self, cmd):
        cmd = "!help#"
        self.command = cmd
        Thread(target=self.write_read).start()

    def write_read(self):
        self.arduino.write(bytes(self.command, 'utf-8'))
        time.sleep(0.05)
        data = self.arduino.readlines()
        for line in data:
            line = line.decode("utf-8")
            print(line, end="")
    