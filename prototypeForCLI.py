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

# Create a button
button = Button(root, text="Button", fg="black")
button.config(width="15")
button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

# Add a label
label = Label(root, text="Label", fg="black")
label.grid(row=4, sticky=W)

root.grid()
root.mainloop()
###################################################