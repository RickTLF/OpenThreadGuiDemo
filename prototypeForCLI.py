#########################################
# GUI specifically designed to test cli
# of dialog openThread.
#########################################

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import serial
import time

root = Tk()
menu = Menu(root)
subMenu = Menu(menu)
bgColor = "#336699"

ser = serial.Serial('\\.\COM5', 115200, timeout=1)

# ***** methods *****

def createNetwork():
    status['text'] = "Change status"

    channel = entryChannel.get()
    byteChannel = int(channel)

    panid = entryPanid.get()
    bytePanid = int(panid)

    networkName = entryNetworkName.get()
    byteNetworkName = networkName

    channel = 'channel ' + str(byteChannel) + '\n'
    panid = 'panid ' + str(bytePanid) + '\n'
    networkName = 'networkname ' + str(byteNetworkName) + '\n'

    ser.write(channel.encode('ascii'))
    time.sleep(1)
    ser.write(panid.encode('ascii'))
    time.sleep(1)
    ser.write(networkName.encode('ascii'))
    time.sleep(1)
    ser.write('start\n'.encode('ascii'))

def showHelp():
    ser.write('help\n'.encode('ascii'))

    readed = 1
    while (readed > 0):
        buf = [0]*10
        readed = ser.readinto(buf)
        threadNetworkScanResults.insert(END, bytearray(buf).decode("ascii"))
        print(bytearray(buf).decode("ascii"))

    """
    time.sleep(1)

    while (ser.in_waiting > 0):
        s = ser.read(ser.in_waiting)
        threadNetworkScanResults.insert(END, s)
        print(s)

    """


def doNothing():
    print("Ok ok I won't.")

# TODO: Create method for channel

# TODO: Create method for childtimeout

# TODO: Create method for contextreusedelay

# TODO: Create method for extaddr

# TODO: Create method for expanid

# TODO: Create method for ipaddr

# TODO: Create method for keysequence

# TODO: Create method for leaderweight

# TODO: Create method for masterkey

# TODO: Create method for mode

# TODO: Create method for netdataregister

# TODO: Create method for networkidtimeout

# TODO: Create method for networkname

# TODO: Create method for panid

# TODO: Create method for ping

# TODO: Create method for prefix

# TODO: Create method for releaserouterid

# TODO: Create method for rloc16

# TODO: Create method for route

# TODO: Create method for routerupgradethreshold

# TODO: Create method for scan

# TODO: Create method for start

# TODO: Create method for state

# TODO: Create method for stop

# TODO: Create method for whitelist

# TODO: Create method for shutting window down

# ***** Exit option *****

def shutdown():
    answer = tkinter.messagebox.askquestion('Exit', 'Are you sure?')

    if answer == 'yes':
        ser.close()
        root.destroy()

# ***** Base window *****

root.config(menu=menu, bg=bgColor)
root.minsize(400, 310)
root.title('openThread demo')

# ***** Main menu *****


menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project...", command=doNothing)
subMenu.add_command(label="new...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=shutdown)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_command(label="Redo", command=doNothing)

# ***** content *****

titleSetup = Label(root, text="SETUP", bg=bgColor, fg="white")

labelChannel = Label(root, text="channel", bg=bgColor, fg="white")
labelPanid = Label(root, text="panid", bg=bgColor, fg="white")
labelNetworkName = Label(root, text="network name", bg=bgColor, fg="white")

entryChannel = Entry(root, width="20")
entryPanid = Entry(root, width="20")
entryNetworkName = Entry(root, width="20")

titleSetup.grid(row=0, columnspan=4)
labelChannel.grid(row=1, sticky=E)
labelPanid.grid(row=2, sticky=E)
labelNetworkName.grid(row=3, sticky=E)

entryChannel.grid(row=1, column=1, columnspan=3)
entryPanid.grid(row=2, column=1, columnspan=3)
entryNetworkName.grid(row=3, column=1, columnspan=3)

# ***** Buttons *****

btnStart = Button(root, text="Start", fg="black", command=createNetwork)
btnDetach = Button(root, text="Detach", fg="black")

btnStart.config(width="15")
btnDetach.config(width="15")

btnStart.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
btnDetach.grid(row=5, column=1, columnspan=3)

# ***** Thread network scan results *****

labelThreadNetworkScanResults = Label(root, text="Thread network scan results", bg=bgColor, fg="white")

btnHelp = Button(root, text="Help", fg="black", command=showHelp)
btnHelp.config(width="10")
btnHelp.grid(row=7, column=1, sticky=W, padx=5, pady=5)

threadNetworkScanResults = Text(root, height=5, width=20)

labelThreadNetworkScanResults.grid(row=6, column=1,  columnspan=3)
threadNetworkScanResults.grid(row=8, column=1, columnspan=3)

# threadNetworkScanResults.insert(END, "\n")

# ***** Toolbar *****

'''toolbar = Frame(root, bg="#333399")
insertButt = Button(toolbar, text="Insert image", command=doNothing, bg='#993333')
insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar, text="print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)'''

# ***** Status Bar *****

status = Label(root, text="Status...", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=9, columnspan=4, pady=(5,0), sticky=W+E)
'''
# used for tabs
n = ttk.Notebook(root)
f1 = ttk.Frame(n, height= 300, width=300)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')
n.pack()
'''

print(ser.name)
root.grid()
root.mainloop()