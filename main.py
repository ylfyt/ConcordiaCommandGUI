# Importing Libraries


from typing import Collection
from OffCommandFrame import OffCommandFrame
from tkinter import *
import serial
import time

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Concordia Command Center")
        self.geometry("1024x768")
        self.resizable(False, False)

        # self.arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)

        self.container = Frame(self, bd=5)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.offCommandFrame = OffCommandFrame(self.container, self)
        self.offCommandFrame.gridMain(row=0, column=0, sticky="nsew")


    def write_read(self, x):
        return
        x += ";"
        self.arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        # data = arduino.readline()
        data = self.arduino.readline()
        data = data.decode("utf-8")
        print(data)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
