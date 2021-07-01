# Importing Libraries
from tkinter import *
from Arduino import Arduino

from OffCommandFrame import OffCommandFrame
from ManualCommandFrame import ManualCommandFrame
from GeneralCommandFrame import GeneralCommandFrame

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

        self.generalCommandFrame = GeneralCommandFrame(self.container, self)
        self.generalCommandFrame.gridMain(row=0, column=0, sticky="nsew")

        self.offCommandFrame = OffCommandFrame(self.container, self)
        self.offCommandFrame.gridMain(row=0, column=1, sticky="nsew")

        self.manualCommandFrame = ManualCommandFrame(self.container, self)
        self.manualCommandFrame.gridMain(row=1, column=0, sticky="nsew")


    def sendToArduino(self, cmd):
        self.arduino.sendCommand(cmd)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
