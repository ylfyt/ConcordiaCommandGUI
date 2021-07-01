# Importing Libraries
from ctypes.wintypes import SERVICE_STATUS_HANDLE
from Arduino import Arduino
from typing import Collection
from OffCommandFrame import OffCommandFrame
from ManualFrame import ManualFrame
from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Concordia Command Center")
        self.geometry("1024x768")
        self.resizable(False, False)

        self.arduino = Arduino()

        self.container = Frame(self, bd=5)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.offCommandFrame = OffCommandFrame(self.container, self)
        self.offCommandFrame.gridMain(row=0, column=0, sticky="nsew")

        self.manualFrame = ManualFrame(self.container, self)
        self.manualFrame.gridMain(row=1, column=0, sticky="nsew")


    def sendToArduino(self, cmd):
        self.arduino.sendCommand(cmd)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
