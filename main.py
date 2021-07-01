# Importing Libraries
from tkinter import *
from classes.Arduino import Arduino

from classes.OffCommandFrame import OffCommandFrame
from classes.ManualCommandFrame import ManualCommandFrame
from classes.WriteCommandFrame import WriteCommandFrame
from classes.GeneralCommandFrame import GeneralCommandFrame

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Concordia Command Center")
        # self.geometry("1024x768")
        self.resizable(False, False)
        self.iconbitmap(r'img/dago_concordia.ico')

        self.arduino = Arduino()

        self.container = Frame(self, bd=5, bg='gray35')
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.generalCommandFrame = GeneralCommandFrame(self.container, self)
        self.generalCommandFrame.gridMain(row=0, column=0, pady=(10, 10))

        self.offCommandFrame = OffCommandFrame(self.container, self)
        self.offCommandFrame.gridMain(row=1, column=0, pady=(10, 10))
        
        self.writeCommandFrame = WriteCommandFrame(self.container, self)
        self.writeCommandFrame.gridMain(row=2, column=0, pady=(10, 10))

        self.manualCommandFrame = ManualCommandFrame(self.container, self)
        self.manualCommandFrame.gridMain(row=3, column=0, columnspan=2, pady=(10, 10))


    def sendToArduino(self, cmd):
        self.arduino.sendCommand(cmd)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
