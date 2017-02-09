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
from functools import partial
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText

class SandScoop:
    #style = ttk.Style()
    root = Tk()
    backgroundColor = ""
    menu = Menu(root)
    subMenu = Menu(menu)

    cntMenuItems = 0

    notebook = ttk.Notebook(root)
    configFrame = ttk.Frame(notebook)
    netInfoFrame = ttk.Frame(notebook)
    lightingControlFrame = ttk.Frame(notebook)

    def __init__(self, thisTitle, color='white'):
        self.root.minsize(420, 350)
        self.root.maxsize(700, 500)
        self.backgroundColor = color
        self.root.configure(background=self.backgroundColor)
        self.root.title(thisTitle)
        self.__addMenu('File', 0)
        #self.__addMenuItem('quit', self.__shutdown)

    def displayTabs(self):
        """
        --------------------------------------------------
        displayTabs
        --------------------------------------------------
        Displays the configuration frame. Usually used by
        the user the first time the program runs.
        The user may want to configure the network name,
        channel, child timeout etc.

        This frame displays network information. This
        allows the user to view child children, list of
        attached child ID's, routers etc. The user may
        also be able to perform MLE discovery operations
        and channel scans.

        This frame displays a list of all lights connected
        to the Thread network. Furthermore, this frame
        allows the user to simply control the light's
        brightness and whether the light should be turned
        on or off.
        --------------------------------------------------
        """
        self.notebook.add(self.configFrame, text='Configuration')
        self.notebook.add(self.netInfoFrame, text='Network information')
        self.notebook.add(self.lightingControlFrame, text='Lighting control')
        self.notebook.grid()

        self.__displayConfigScreen()
        self.__displayNetworkScreen()

    def __displayNetworkScreen(self):
        self.__createTable(0, 8, 4, 4)

    def __displayConfigScreen(self):
        """
        --------------------------------------------------
        __displayConfigScreen()
        --------------------------------------------------
        Displays the widgets represented on the
        configuration screen.
        --------------------------------------------------
        """
        commands = ["channel", "childmax", "childtimeout",
                    "dataset delay", "dataset panid", "netdataregister",
                    "dataset active", "extaddr", "masterkey"]

        labels = ["Channel: ", "Max children: ", "Child timeout: ",
                  "Timer delay: ", "Panid: ",
                  "Register local network: ", "Active timestamp: "
                  "Extended address: ", "Master key: "]

        for cmd in range(0, len(commands) -1):
            self.__addBaseInputComponent(self.configFrame, labels[cmd], cmd, command=lambda cmd=cmd: self.__doNothing(commands[cmd]))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def __addBaseInputComponent(self, parent, label, row, command):
        self.__addLabel(parent, label, row, 0)
        self.__addInputBox(parent, 20, row, 1)
        self.__addButton(parent, "submit", row, 2, command)

    def __doNothing(self, cmd):
        print("Button pressed: " + cmd)

    def __addLabel(self, parent, text, row, column):
        label = Label(parent, text=text, fg="black", bg=self.backgroundColor)
        label.grid(row=row, column=column, sticky=W)

    def __addInputBox(self, parent, width, row, column):
        inputBox = Entry(parent, width=width)
        inputBox.grid(row=row, column=column, sticky=W)

    def __addButton(self, parent, text, row, column, command):
        button = Button(parent, text=text, fg="white", command=command, bg='grey')
        button.config(width=10)
        button.grid(row=row, column=column, padx=5, pady=5)

    def updateGui(self):
        """
        --------------------------------------------------
        updateGui
        --------------------------------------------------
        Updates every widget.
        --------------------------------------------------
        """

    def displayLastError(self):
        """
        --------------------------------------------------
        displayLastError
        --------------------------------------------------
        Will display the last error generated by program
        validating inputs.
        --------------------------------------------------
        """

    def saveWidgetId(self, id):
        """
        --------------------------------------------------
        saveWidgetId
        --------------------------------------------------
        Sometimes, only one widget should be updated after
        receiving data. This method saves the
        corresponding widget's id to later update the
        widget itself. see updateWidget().
        --------------------------------------------------
        """

    def updateWidget(self, id):
        """
        --------------------------------------------------
        updateWidget
        --------------------------------------------------
        Updates the widget with the corresponding id. To
        update a widget, make sure to first use the
        daveWidget() method.
        --------------------------------------------------
        """

    def isButtonPressed(self):
        """
        --------------------------------------------------
        isButtonPressed
        --------------------------------------------------
        Simple check to see whether or not a button has
        been pressed or not.
        --------------------------------------------------
        """

    def validateInput(self, type):
        """
        --------------------------------------------------
        validateInput
        --------------------------------------------------
        Depending on the type of input being implemented,
        Every input should be validated. If the user's
        input is invalid, the program will generate an
        error and won't proceed to transmit the command to
        the corresponding device. The program will proceed
        running normally, but the (last) error generated
        will be displayed in the error pane.
        --------------------------------------------------
        """

    def updateProgramData(self):
        """
        --------------------------------------------------
        updateProgramData
        --------------------------------------------------
        Sometimes - after a time interval has elapsed for
        example - the data needs to be updated but the
        widgets of the current frame shouldn't.
        --------------------------------------------------
        """

    def constructGui(self):
        """
        --------------------------------------------------
        constructGui
        --------------------------------------------------
        Construct the graphical user interface by calling
        grid() and mainloop() from tkinter library. This
        method should always be called in order to
        display all widgets belonging to the tkinter
        library.
        --------------------------------------------------
        """
        self.root.grid()
        self.root.mainloop()

    def __createTable(self, row, maxCells, maxCol, tBreak):
        """
        --------------------------------------------------
        displayTabs
        --------------------------------------------------
        Creates a custom table of labels.
        --------------------------------------------------
        """
        #blankLabel = Label(self.root, text="", fg="black")
        #blankLabel.grid(row=row, sticky=W, columnspan=2)
        thisRow = 0
        for j in range(0, maxCells):

            label = Label(self.netInfoFrame, text=str(j), fg="black", bg="white")


            '''tableCel = Entry(self.root, width="10")
            tableCel.insert(0, str(j))
            tableCel.config(state=DISABLED)
            tableCel.config(disabledbackground="white")
            tableCel.config(disabledforeground="black")'''
            if j % tBreak == 0:
                thisRow += 1
            label.grid(row=thisRow, column=j % maxCol, columnspan=1)

    def __shutdown(self):
        answer = tkinter.messagebox.askquestion('Exit', 'Are you sure?')
        if answer == 'yes':
            # ser.close()
            self.root.destroy()

    def __addMenu(self, text, cnt=1):
        self.cntMenuItems = cnt
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label=text, menu=self.subMenu)

        if (cnt == 0):
            self.subMenu.configure(background='white', fg='blue')
            self.subMenu.add_command(label="Exit", command=self.__shutdown)

    def __addMenuItem(self, label, command):
        # Only add as many items as specified in addMenu.
        if (self.cntMenuItems > 0 and (self.subMenu.index('end') <= self.cntMenuItems)):
            self.subMenu.add_command(label=label, command=command)
            # Automatically add an exit menu option after all
            # other menu items.
            if (self.subMenu.index('end') == self.cntMenuItems):
                self.subMenu.add_command(label="Exit", command=self.__shutdown)