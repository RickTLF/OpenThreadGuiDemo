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

'''def receiveDataString(lastCommand):
    buf = receiveData(lastCommand)
    dataString = bytearray(buf).decode("ascii")'''

def receiveData(lastCommand):
    buf = [10] * 1
    dataBuffer = [200]
    dataReceived = 1
    stringBuffer = ""
    i = 0
    characterCount = 0
    ssr = "" #used to place the final string in here

    # The following vars are meant to detect whether there is a space in
    # between two letters. If so, the space should be included when appending
    # the character to the string.

    # example: Network Name

    # Between k and N is a space, so the space between k and N must be saved.

    # The rest of the spaces should be neglected.
    firstStringChar = ""
    secondStringChar = ""
    countCharactersInBetween = 0


    while (dataReceived > 0):
        dataReceived = ser.readinto(buf)
        dataString = bytearray(buf).decode("ascii")
        if ("-" != dataString):
            if ("+" != dataString):
                if ("|" != dataString):
                    if "| " != dataString:
                        if " |" != dataString:
                            if (dataString == " "):  # Detect space and save the occurance.
                                if (characterCount > 0):
                                    firstStringChar = 1;    # It is true that a space has been detected
                                characterCount=1
                            elif (dataString != " "):   # Now wait for a character not to be a space.
                                if (firstStringChar == 1):  # Is it true that a space has been detected early on?
                                    stringBuffer += " "     # Add space between the next character and the previous one.
                                    firstStringChar = 0     # Repeat detection.
                                    #characterCount = 0
                                stringBuffer += dataString  # Proceed to add character that is not space. characterCount += 1


                        #if " " != dataString:

                elif ("|" == dataString):
                    if (stringBuffer != lastCommand +'\n\n'):
                        if (stringBuffer[0] != " "):
                            dataBuffer.append(stringBuffer)
                        else:
                            dataBuffer.append(stringBuffer[1:len(stringBuffer)])

                    #print(stringBuffer)
                    stringBuffer = ""
                    characterCount = 0

    '''for e in dataBuffer:
        print("array contents: ")
        print(e)'''

    print(dataBuffer[2:len(dataBuffer)])

    #print(str(characterCount) + '\n')

        #print(dataString)
        #print(dataReceived)
        #print(stringBuffer)

    #if (dataReceived == 0):

        #print(stringBuffer)

    # readed = 1
    # while (readed > 0):
        #buf = [0] * 10
        #readed = ser.readinto(buf)
        #dataString = bytearray(buf).decode("ascii")
        #print(dataString)
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

# MENU

menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project...", command=doNothing)
subMenu.add_command(label="new...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=shutdown)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_command(label="Redo", command=doNothing)

# TRANSMISSION

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