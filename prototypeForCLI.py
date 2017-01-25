####################################################
# OPENTHREAD GUI DEMO
#
# Developer     :   Rick Kock
# Date          :   25/01/2017
# Team members  :   David de Prez, Tim Spaans
# Institution   :   Avans Hogeschool, Den Bosch
#
###################################################

# Imports
from tkinter import *
import tkinter.ttk as ttk

# Global variables
root = Tk()

###################################################
# SETUP
###################################################

root.minsize(400, 300)
root.title('OpenThread GUI demo Avans')

###################################################
# MAIN
###################################################

# Add textbox
inputBox = Entry(root, width="20")
inputBox.grid(row=0, column=0, columnspan=1)

# Add a text-area representing the output
threadNetworkScanResults = Text(root, height=5, width=20)
threadNetworkScanResults.grid(row=1, column=0, columnspan=1)

# Add a listbox
listBox = Listbox(root)
for item in ["listItem1", "listItem2"]:
    listBox.insert(END, item)

listBox.grid(row=2, column=0, columnspan=1)

root.grid()
root.mainloop()
###################################################