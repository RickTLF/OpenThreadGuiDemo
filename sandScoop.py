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

from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText

# TODO: Add panes for widgets!
# TODO: Add labelFrame!

class SandScoop:

    def displayConfigFrame(self):
        """
        --------------------------------------------------
        displayConfigFrame
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def displayNetworkFrame(self):
        """
        --------------------------------------------------
        displayNetworkFrame
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def displayLightingControl(self):
        """
        --------------------------------------------------
        displayLightingControl
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def updateGui(self):
        """
        --------------------------------------------------
        updateGui
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def saveWidgetId(self):
        """
        --------------------------------------------------
        saveWidgetId
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def displayLastError(self):
        """
        --------------------------------------------------
        displayLastError
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def saveWidgetId(self, id):
        """
        --------------------------------------------------
        saveWidgetId
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def updateWidget(self):
        """
        --------------------------------------------------
        updateWidget
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def isButtonPressed(self):
        """
        --------------------------------------------------
        isButtonPressed
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def validateInput(self, type):
        """
        --------------------------------------------------
        validateInput
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """

    def updateProgramData(self):
        """
        --------------------------------------------------
        updateProgramData
        --------------------------------------------------
        Setup the program GUI.
        --------------------------------------------------
        """


    '''classFrames = []
    classAdditions = []
    cntMenuItems = 0
    btnWidth = "20"
    root = Tk()
    backgroundColor = 'white'
    menu = Menu(root)
    subMenu = Menu(menu)

    def __init__(self, thisTitle, color='white'):
        self.root.geometry('500x300')
        self.root.configure(background=self.backgroundColor)
        self.root.title(thisTitle)
        self.backgroundColor = color

    def __shutdown(self):
        answer = tkinter.messagebox.askquestion('Exit', 'Are you sure?')
        if answer == 'yes':
            #ser.close()
            self.root.destroy()

    def __doNothing(self):
        print("Ok ok I won't.")

    def addTabs(self, frames):
        notebook = ttk.Notebook(self.root)

        # Add frames

        # For each frame, create frame
        for frame in range(0, len(frames)-1):
            self.classFrames[frame] = ttk.Frame(notebook)

        for frame in range(0, len(frames)-1):
            self.classFrames[frame] = ttk.Frame(notebook)
            self.classAdditions[frame] = notebook.add(self.classFrames[frame], text=frames[frame])

        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)

        #Add tabs
        notebook.add(frame1, text='Frame One')
        notebook.add(frame2, text='Frame Two')
        notebook.add(frame3, text='Frame Three')
        notebook.grid()

        tkLabel = Label(frame1, text=" Hello Python!")
        tkLabel.grid()

        strVersion = "running Python version "
        tkLabelVersion = Label(frame2, text=strVersion)
        tkLabelVersion.grid()
        strPlatform = "Platform: "
        tkLabelPlatform = Label(frame2, text=strPlatform)
        tkLabelPlatform.grid()

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

    def createTable(self, row, maxCells, maxCol):
        blankLabel = Label(self.root, text="", fg="black")
        blankLabel.grid(row=row, sticky=W, columnspan=2)
        thisRow = 0
        for j in range(0, maxCells):
            tableCel = Entry(self.root, width="10")
            tableCel.insert(0, str(j))
            tableCel.config(state=DISABLED)
            tableCel.config(disabledbackground="white")
            tableCel.config(disabledforeground="black")
            if j % 4 == 0:
                thisRow += 1
            tableCel.grid(row=thisRow, column=j % maxCol, columnspan=1, in_=blankLabel)
            '''