from tkinter import *
from tkinter import ttk


class WriteCommandFrame(Frame):
    def __init__(self, master, controller):
        self.WIDTH = 512
        self.HEIGHT = 384

        self.ct = controller
        color = "gray35"

        self.mainFrame = Frame(master)
        Frame.__init__(self, self.mainFrame, width=self.WIDTH, height=self.HEIGHT, background=color)
        self.grid(row=0, column=0)

        self.initWidget()
    
    def initWidget(self):
        # W COMMAND
        self.wButton = Button(self, text="W", font = "Helvetica 10 bold", width=10, height=2, command=self.wCommand)
        self.wButton.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        
        self.WIDNUM = 4
        self.wVars = [StringVar() for i in range(self.WIDNUM)]
        self.wEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.wVars[i]) for i in range(self.WIDNUM)]
        for i in range(self.WIDNUM):
            self.wEntrys[i].grid(row=0, column=i+1, padx=(10, 10), pady=(10, 10))

        # WBPF COMMAND
        self.wbpfButton = Button(self, text="WBPF", font = "Helvetica 10 bold", width=10, height=2, command=self.wbpfCommand)
        self.wbpfButton.grid(row=1, column=0, padx=(20, 20), pady=(10, 10))
        
        self.WBPFIDNUM = 4
        self.wbpfVars = [StringVar() for i in range(self.WBPFIDNUM)]
        self.wbpfEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.wbpfVars[i]) for i in range(self.WBPFIDNUM)]
        for i in range(self.WBPFIDNUM):
            self.wbpfEntrys[i].grid(row=1, column=i+1, padx=(20, 20), pady=(10, 10))

        # WBP COMMAND
        self.wbpButton = Button(self, text="WBP", font = "Helvetica 10 bold", width=10, height=2, command=self.wbpCommand)
        self.wbpButton.grid(row=2, column=0, padx=(20, 20), pady=(10, 10))
        
        self.WBPIDNUM = 4
        self.wbpVars = [StringVar() for i in range(self.WBPIDNUM)]
        self.wbpEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.wbpVars[i]) for i in range(self.WBPIDNUM)]
        for i in range(self.WBPIDNUM):
            self.wbpEntrys[i].grid(row=2, column=i+1, padx=(20, 20), pady=(10, 10))
    

    def wCommand(self):
        wId = [self.wEntrys[i].get() for i in range(self.WIDNUM)]
        
        param = ""
        for i in range(len(wId)):
            id = wId[i]
            if (id != ''):
                try:
                    id = int(id)
                    param += str(id)
                    param += " "
                except:
                    print("ID is not Number")

        if (param != ""):
            param = param[:len(param)-1]
            cmd = "!w " + param + "#"
            print(cmd)
            # sending cmd to arduino via port
            self.ct.sendToArduino(cmd)
        else:
            print("Python: Invalid input")

        # Reset Entry
        for var in self.wVars:
            var.set('')

    def wbpfCommand(self):
        wbpfId = [self.wbpfEntrys[i].get() for i in range(self.WBPFIDNUM)]
        
        param = ""
        for i in range(len(wbpfId)):
            id = wbpfId[i]
            if (id != ''):
                try:
                    id = int(id)
                    param += str(id)
                    param += " "
                except:
                    print("ID is not Number")

        if (param != ""):
            param = param[:len(param)-1]
            cmd = "!wBPf " + param + "#"
            print(cmd)
            # sending cmd to arduino via port
            self.ct.sendToArduino(cmd)
        else:
            print("Python: Invalid input")

        # Reset Entry
        for var in self.wbpfVars:
            var.set('')

    def wbpCommand(self):
        wbpId = [self.wbpEntrys[i].get() for i in range(self.WBPIDNUM)]
        
        param = ""
        for i in range(len(wbpId)):
            id = wbpId[i]
            if (id != ''):
                try:
                    id = int(id)
                    param += str(id)
                    param += " "
                except:
                    print("ID is not Number")

        if (param != ""):
            param = param[:len(param)-1]
            cmd = "!wBP " + param + "#"
            print(cmd)
            # sending cmd to arduino via port
            self.ct.sendToArduino(cmd)
        else:
            print("Python: Invalid input")

        # Reset Entry
        for var in self.wbpVars:
            var.set('')
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    