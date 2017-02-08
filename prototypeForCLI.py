#//////////////////////////////////////////////////
#--------------------------------------------------
# OPENTHREAD GUI DEMO
#--------------------------------------------------
#//////////////////////////////////////////////////
#
# Developer     :   Rick Kock
# Date          :   25/01/2017
# Team members  :   David de Prez, Tim Spaans
# Institution   :   Avans Hogeschool, Den Bosch
#
#//////////////////////////////////////////////////

#--------------------------------------------------
# Imports
#--------------------------------------------------
import serial
from sandScoop import *
import sandScoop
import threading
#--------------------------------------------------
# Global vars
#--------------------------------------------------
dialog_gui = SandScoop('Avans OpenThread Demo')
#--------------------------------------------------

print(sandScoop.__doc__)

#bgColor = '#330033'

#def printSomething():
    #print("Yellow world!")


def setup():
    """
    --------------------------------------------------
    setup
    --------------------------------------------------
    Setup the program GUI.
    --------------------------------------------------
    """

    # gui setup


def update():
    """
    --------------------------------------------------
    createGui
    --------------------------------------------------
    Finally, put things together by using grid.
    --------------------------------------------------
    """
    dialog_gui.createGui()

'''dialog_gui.addLabel('some Text', 0, 0)
dialog_gui.addInputBox('20', 0, 1)
dialog_gui.addButton('submit', 0, 2, printSomething)

dialog_gui.addLabel('some Text', 1, 0)
dialog_gui.addInputBox('20', 1, 1)
dialog_gui.addButton('submit', 1, 2, printSomething)

dialog_gui.addLabel('some Text', 2, 0)
dialog_gui.addInputBox('20', 2, 1)
dialog_gui.addButton('submit', 2, 2, printSomething)

dialog_gui.createTable(3, 16, 4)'''

#dialog_gui.addMenu("File", 0)

import tkinter as tk
from tkinter import ttk


#print(dialog_gui.createGui.__doc__)



