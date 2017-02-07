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
#--------------------------------------------------

print(sandScoop.__doc__)

bgColor = '#330033'

def printSomething():
    print("Yellow world!")

# gui setup
dialog_gui = SandScoop('the title', 200, 200)
dialog_gui.addTabs()

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

def doNothing():
    print("Do nothing.")

dialog_gui.addMenu("File", 0)

dialog_gui.createGui()
#print(dialog_gui.createGui.__doc__)


