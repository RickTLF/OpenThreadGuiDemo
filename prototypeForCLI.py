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
inputBox.grid(row=1, column=1, columnspan=3)

root.grid()
root.mainloop()
###################################################