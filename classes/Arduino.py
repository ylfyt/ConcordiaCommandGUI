import serial
import time
from threading import *

class Arduino:
    def __init__(self):
        PORT = 'COM9'
        BAUDRATE = 115200
        TIMEOUT = .1

        try:
            self.arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
        except:
            print("Port cannot open!!")

        self.command = "!def#"
    
    def sendCommand(self, cmd):
        # cmd = "!help#"
        self.command = cmd
        Thread(target=self.write_read).start()

    def write_read(self):
        if hasattr(self, 'arduino'):
            self.arduino.write(bytes(self.command, 'utf-8'))
            time.sleep(0.05)
            data = self.arduino.readlines()
            for line in data:
                line = line.decode("utf-8")
                print(line, end="")
            
            if (self.command == "!save#"):
                time.sleep(2)
                data = self.arduino.readlines()
                for line in data:
                    line = line.decode("utf-8")
                    print(line, end="")