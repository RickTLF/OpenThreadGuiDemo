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


# Add a label, textBox and a button
label = Label(root, text="Label", fg="black")
label.grid(row=0, sticky=W)
inputBox = Entry(root, width="20")
inputBox.grid(row=0, column=1, sticky=W)
button = Button(root, text="Button", fg="black")
button.config(width="15")
button.grid(row=0, column=2, padx=5, pady=5)

# Add a text-area representing the output
threadNetworkScanResults = Text(root, height=5, width=20)
threadNetworkScanResults.grid(row=1, column=0, columnspan=2)

# Add a listbox
listBox = Listbox(root)
for item in ["listItem1", "listItem2"]:
    listBox.insert(END, item)

listBox.grid(row=2, column=0, columnspan=1)

# Create a table
blankLabel = Label(root, text="", fg="black")
blankLabel.grid(row=5, sticky=W, columnspan=2)

#for i in range(0,2):
thisRow = 0

for j in range(0,6):
    tableCel = Entry(root, width="10")
    tableCel.insert(0, 'cel ' + str(j))
    tableCel.config(state=DISABLED)
    tableCel.config(disabledbackground="white")
    tableCel.config(disabledforeground="black")
    if j%3 == 0:
        thisRow+=1

    tableCel.grid(row=thisRow, column=j%3, columnspan=1, in_=blankLabel)


root.grid()
root.mainloop()
###################################################