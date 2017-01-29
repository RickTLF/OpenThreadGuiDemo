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
import serial
import tkinter.messagebox

import tkinter.ttk as ttk

# Global variables
root = Tk()
ser = serial.Serial('\\.\COM5', 115200, timeout=1)
menu = Menu(root)
subMenu = Menu(menu)

###################################################
# SETUP
###################################################

root.minsize(400, 300)
root.title('OpenThread GUI demo Avans')
root.config(menu=menu)

###################################################
# MAIN
###################################################

# Add a label, textBox and a button
label = Label(root, text="Label", fg="black")
label.grid(row=0, sticky=W)
inputBox = Entry(root, width="20")
inputBox.grid(row=0, column=1, sticky=W)

# Get the text inserted and print in console.
def printEntry():
    inputEntry = inputBox.get()

    print(inputEntry)

    # Itterate through strings checking each character
    for i in range(0, len(inputEntry)):
        print(inputEntry[i])
        '''print(inputEntry[1])
        print(inputEntry[2])
        print(inputEntry[3])'''

    '''if inputEntry == "Done":
        print('TRUE')
    else:
        print('FALSE')'''

    # check to see if the textbox is empty
    '''if len(inputEntry)==0:
        print('Nothing inserted')
    else:
        print(inputEntry)'''

# User Serial port to transmit a command.
def transmitCommand():
    inputEntry = inputBox.get() + '\n'
    ser.write(inputEntry.encode('ascii'))
    print(inputEntry)
    receiveData(inputEntry)

def receiveData(lastCommand):
    readed = 1
    while (readed > 0):
        buf = [0] * 10
        readed = ser.readinto(buf)
        dataString = bytearray(buf).decode("ascii")
        print(dataString[0:len(lastCommand)])
        # print(dataString)
        #print(bytearray(buf).decode("ascii"))
    #if serData == 'Done\n':
        #ser.close()

def shutdown():
    answer = tkinter.messagebox.askquestion('Exit', 'Are you sure?')
    if answer == 'yes':
        ser.close()
        root.destroy()

def doNothing():
    print("Ok ok I won't.")


menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project...", command=doNothing)
subMenu.add_command(label="new...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=shutdown)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_command(label="Redo", command=doNothing)

button = Button(root, text="Button", fg="black", command=transmitCommand)
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

'''
First create a blank label.
The empty label serves no real purpose.
The blank label is used to act as a container,
A container for another grid.
'''
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