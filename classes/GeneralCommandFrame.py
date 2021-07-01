from tkinter import *
from tkinter import ttk


class GeneralCommandFrame(Frame):
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
        self.defButton = Button(self, text="DEF", font = "Helvetica 10 bold", width=10, height=2, command=self.defCommand)
        self.defButton.grid(row=0, column=0, padx=(5, 5), pady=(10, 10))

        self.labelTextPage = Label(self, text="Page : ", font = "Helvetica 14", bg='lightblue')
        self.labelTextPage.grid(row=1, column=0, padx=(5, 5), pady=(10, 10))

        self.pageOption = [str(i) for i in range(76)] 
        self.pageOptionCombo = ttk.Combobox(self, values=self.pageOption, state="readonly", font = "Helvetica 12", width=10)
        self.pageOptionCombo.grid(row=1, column=1, padx=(5, 5), pady=(10, 10))

        self.labelTextStep = Label(self, text="Step : ", font = "Helvetica 14", bg='lightblue')
        self.labelTextStep.grid(row=1, column=2, padx=(5, 5), pady=(10, 10))

        self.stepOption = [str(i+1) for i in range(20)] 
        self.stepOptionCombo = ttk.Combobox(self, values=self.stepOption, state="readonly", font = "Helvetica 12", width=10)
        self.stepOptionCombo.grid(row=1, column=3, padx=(5, 5), pady=(10, 10))
        
        self.gButton = Button(self, text="G",width=7, font = "Helvetica 12", command=self.gCommand)
        self.gButton.grid(row=1, column=4, padx=(5, 5), pady=(10, 10))

        self.pageOptionCombo.bind("<<ComboboxSelected>>", self.pageSelected)
        self.stepOptionCombo.bind("<<ComboboxSelected>>", self.stepSelected)

    def defCommand(self):
        cmd = "!def#"
        print(cmd)
        self.ct.sendToArduino(cmd)
        
    def gCommand(self):
        stepNum = self.stepOptionCombo.get()
        if (stepNum != ''):
            cmd = "!g " + stepNum + "#"
            print(cmd)
            self.ct.sendToArduino(cmd)

    def pageSelected(self, event):
        pageNum = self.pageOptionCombo.get()
        cmd = "!p " + pageNum + "#"
        print(cmd)
        # Send command to arduino
        self.ct.sendToArduino(cmd)

        # Reset Step Selection
        self.stepOptionCombo.set('')

    def stepSelected(self, event):
        stepNum = self.stepOptionCombo.get()
        cmd = "!g " + stepNum + "#"
        print(cmd)

        # Send command to Arduino
        self.ct.sendToArduino(cmd)
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    