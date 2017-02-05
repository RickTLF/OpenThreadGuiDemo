#from tkinter import *

"""
//////////////////////////////////////////////////
--------------------------------------------------
SANDSCOOP
--------------------------------------------------
//////////////////////////////////////////////////

Developer     :   Rick Kock
Date          :   25/01/2017
Team members  :   David de Prez, Tim Spaans
Institution   :   Avans Hogeschool, Den Bosch

//////////////////////////////////////////////////
"""
from tkinter import *
import tkinter.messagebox

class SandScoop:
    cntMenuItems = 0
    btnWidth = "20"
    windowWidth = 300
    windowHeight = 300
    root = Tk()
    backgroundColor = 'white'
    menu = Menu(root)
    subMenu = Menu(menu)

    def __init__(self, thisTitle, width, height, color='white'):
        self.windowWidth = width
        self.windowHeight = height
        self.root.configure(background=self.backgroundColor)
        self.root.minsize(self.windowWidth, self.windowHeight)
        self.root.title(thisTitle)
        self.backgroundColor = color

    def __shutdown(self):
        answer = tkinter.messagebox.askquestion('Exit', 'Are you sure?')
        if answer == 'yes':
            #ser.close()
            self.root.destroy()

    def __doNothing(self):
        print("Ok ok I won't.")

    def addMenu(self, text, cnt=1):
        self.cntMenuItems = cnt
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label=text, menu=self.subMenu)

        if (cnt==0):
            self.subMenu.configure(background='black', fg='white')
            self.subMenu.add_command(label="Exit", command=self.__shutdown)

    def addMenuItem(self, label, command):

        # Only add as many items as specified in addMenu.
        if (self.cntMenuItems > 0 and (self.subMenu.index('end') <= self.cntMenuItems)):
            self.subMenu.add_command(label=label, command=command)
            # Automatically add an exit menu option after all
            # other menu items.
            if (self.subMenu.index('end') == self.cntMenuItems):
                self.subMenu.add_command(label="Exit", command=self.__shutdown)

    # Add a label, textBox and a button
    def addLabel(self, text, row, column):
        label = Label(self.root, text=text, fg="black", bg=self.backgroundColor)
        label.grid(row=row, column=column, sticky=W)

    def addInputBox(self, width, row, column):
        inputBox = Entry(self.root, width=width)
        inputBox.grid(row=row, column=column, sticky=W)

    def addButton(self, text, row, column, command):
        button = Button(self.root, text=text, fg="white", command=command, bg='black')
        button.config(width=int(self.windowWidth/25))
        button.grid(row=row, column=column, padx=5, pady=5)

    def createGui(self):
        """
        --------------------------------------------------
        createGui
        --------------------------------------------------
        Finally, put things together by using grid.
        --------------------------------------------------
        """
        self.root.grid()
        self.root.mainloop()