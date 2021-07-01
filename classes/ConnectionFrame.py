from tkinter import *
from tkinter import ttk

import serial.tools.list_ports

class ConnectionFrame(Frame):
    def __init__(self, master, controller, color):
        self.WIDTH = 512
        self.HEIGHT = 384

        self.ct = controller
        # color = "gray35"

        self.mainFrame = Frame(master, bg=color)
        Frame.__init__(self, self.mainFrame, width=self.WIDTH, height=self.HEIGHT, background=color)
        self.grid(row=0, column=0)

        self.initWidget()
    
    def initWidget(self):
        self.refreshButton = Button(self, text="Refresh", font = "Helvetica 10 bold", width=10, bg='blue', command=self.refresh)
        self.refreshButton.grid(row=0, column=0, padx=(5, 5), pady=(10, 10))

        self.labelTextPort = Label(self, text="Port : ", font = "Helvetica 14", bg='lightblue')
        self.labelTextPort.grid(row=0, column=1, padx=(5, 5), pady=(10, 10))
 
        self.portOptionCombo = ttk.Combobox(self, values=[], state="readonly", font = "Helvetica 12", width=20)
        self.portOptionCombo.grid(row=0, column=2, padx=(5, 5), pady=(10, 10))

        self.connectButton = Button(self, text="Connect", font = "Helvetica 10 bold", width=10, bg='lightgreen', command=self.connect)
        self.connectButton.grid(row=0, column=3, padx=(5, 5), pady=(10, 10))
        
    def refresh(self):
        con = self.getPortList()
        print(con)
        self.portOptionCombo['values'] = con
        self.portOptionCombo.set('')

    def connect(self):
        port = self.portOptionCombo.get()
        if (port != ''):
            print("connecting to " + port)
            self.ct.connectToArduino(port)

    
    def getPortList(self):
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
        
        return connected

        
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    