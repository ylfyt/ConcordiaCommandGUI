from tkinter import *

class OffCommandFrame(Frame):
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
        self.offButton = Button(self, text="OFF", font = "Helvetica 10 bold", width=10, height=2, command=self.offCommand)
        self.offButton.grid(row=0, column=0, padx=(5, 5), pady=(10, 10))
        
        self.OFFIDNUM = 4
        self.offVars = [StringVar() for i in range(self.OFFIDNUM)]
        self.offEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.offVars[i]) for i in range(self.OFFIDNUM)]
        for i in range(self.OFFIDNUM):
            self.offEntrys[i].grid(row=0, column=i+1, padx=(5, 5), pady=(10, 10))

        self.onAllButton = Button(self, text="ON ALL", font = "Helvetica 10 bold", width=10, height=2, bg='lime green', command=self.onAllCommand)
        self.onAllButton.grid(row=1, column=0, padx=(5, 5), pady=(10, 10))

        self.oaButton = Button(self, text="OA", font = "Helvetica 10 bold", width=10, height=2, command=self.oaCommand)
        self.oaButton.grid(row=1, column=1, padx=(5, 5), pady=(10, 10))
        self.olaButton = Button(self, text="OLA", font = "Helvetica 10 bold", width=10, height=2, command=self.olaCommand)
        self.olaButton.grid(row=1, column=2, padx=(5, 5), pady=(10, 10))
        self.oraButton = Button(self, text="ORA", font = "Helvetica 10 bold", width=10, height=2, command=self.oraCommand)
        self.oraButton.grid(row=1, column=3, padx=(5, 5), pady=(10, 10))
        self.ohButton = Button(self, text="OH", font = "Helvetica 10 bold", width=10, height=2, command=self.ohCommand)
        self.ohButton.grid(row=1, column=4, padx=(5, 5), pady=(10, 10))


        self.ofButton = Button(self, text="OF", font = "Helvetica 10 bold", width=10, height=2, command=self.ofCommand)
        self.ofButton.grid(row=2, column=0, padx=(5, 5), pady=(10, 10))
        self.olfButton = Button(self, text="OLF", font = "Helvetica 10 bold", width=10, height=2, command=self.olfCommand)
        self.olfButton.grid(row=2, column=1, padx=(5, 5), pady=(10, 10))
        self.orfButton = Button(self, text="ORF", font = "Helvetica 10 bold", width=10, height=2, command=self.orfCommand)
        self.orfButton.grid(row=2, column=2, padx=(5, 5), pady=(10, 10))
        self.ohipButton = Button(self, text="OHIP", font = "Helvetica 10 bold", width=10, height=2, command=self.ohipCommand)
        self.ohipButton.grid(row=2, column=3, padx=(5, 5), pady=(10, 10))

        self.offAllButton = Button(self, text="OFF ALL", font = "Helvetica 10 bold", width=10, height=2, bg='red', command=self.offAllCommand)
        self.offAllButton.grid(row=2, column=4, padx=(5, 5), pady=(10, 10))
    
    def offCommand(self):
        offId = [self.offEntrys[i].get() for i in range(self.OFFIDNUM)]
        
        param = ""
        for i in range(len(offId)):
            id = offId[i]
            if (id != ''):
                try:
                    id = int(id)
                    param += str(id)
                    param += " "
                except:
                    print("ID is not Number")

        if (param != ""):
            param = param[:len(param)-1]
            command = "!off " + param + "#"
            print("Python: " + command)
            
            # sending command to arduino via port
            self.ct.write_read(command)
        else:
            print("Python: Invalid input")

        # Reset Entry
        for var in self.offVars:
            var.set('')
        
    def oaCommand(self):
        print("!oa#")

    def olaCommand(self):
        print("!ola#")

    def oraCommand(self):
        print("!ora#")

    def ohCommand(self):
        print("!oh#")

    def ofCommand(self):
        print("!of#")

    def olfCommand(self):
        print("!olf#")

    def orfCommand(self):
        print("!orf#")

    def ohipCommand(self):
        print("!ohip#")

    def offAllCommand(self):
        print("!off#")
    
    def onAllCommand(self):
        print("!on#")
        
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    