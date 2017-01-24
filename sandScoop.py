from tkinter import *

class SandScoop:
    def __init__(self, mas):
        self.master = mas
        #self.constructButton(master)

    def printMessage(self):
        print("Wow, this actually worked!")

    def constructButton(self, master):
        frame = Frame(master)
        frame.pack();
        self.printButton = Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        self.printButton.grid()
