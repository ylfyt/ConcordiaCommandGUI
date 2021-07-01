from tkinter import *

class ManualCommandFrame(Frame):
    def __init__(self, master, controller):
        self.WIDTH = 900
        self.HEIGHT = 50

        self.ct = controller
        color = "gray35"

        self.mainFrame = Frame(master)
        Frame.__init__(self, self.mainFrame, width=self.WIDTH, height=self.HEIGHT, background=color)
        self.grid(row=0, column=0)

        self.initWidget()
    
    def initWidget(self):
        self.cmdVar = StringVar()
        self.commandEntry = Entry(self, width=87, textvariable=self.cmdVar, font = "Helvetica 14 bold")
        self.commandEntry.grid(row=0, column=0, padx=(5, 5))
        self.commandEntry.bind('<Return>', self.sendCommandEnter)


        self.sendButton = Button(self, text="Send", command=self.sendCommand)
        self.sendButton.grid(row=0, column=1)
        
    def sendCommand(self):
        cmd = self.cmdVar.get()
        self.cmdVar.set("")
        if (cmd != ""):
            print(cmd)
            self.ct.sendToArduino(cmd)
    
    def sendCommandEnter(self, event):
        cmd = self.cmdVar.get()
        self.cmdVar.set("")
        if (cmd != ""):
            print(cmd)
            self.ct.sendToArduino(cmd)

        
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    