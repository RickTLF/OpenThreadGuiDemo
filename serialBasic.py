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
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText

# TODO: Add panes for widgets!
# TODO: Add labelFrame!

class SandScoop:
    stringBuffer = []
    currentString = 'None'

    def __init__(self):
        #self.root.

    def validateStrings(self, input):
        """
        --------------------------------------------------
        validateStrings()
        --------------------------------------------------
        First make sure that the data sent is valid before
        it can be transmitted.
        --------------------------------------------------
        """

    def transmitData(self, command):
        """
        --------------------------------------------------
        transmitData()
        --------------------------------------------------
        Transmit data using pySerial. While waiting to
        receive the 'Done' keyword, no other data should
        be transmitted. This process should not be
        interfered. However, note that this may not be
        the final solution.
        --------------------------------------------------
        """

    def receiveData(self):
        """
        --------------------------------------------------
        receiveData()
        --------------------------------------------------
        As you receive data from a device, add the data
        to a buffer. skip the command you've sent which
        will (probably) also be included in the buffer.
        Receive data until wait() returns false.
        --------------------------------------------------
        """

    def wait(self, keyword):
        """
        --------------------------------------------------
        wait()
        --------------------------------------------------
        Wait for a particular keyword to be received. Once
        received, it means you've received all the data
        from the device and the program may proceed.
        --------------------------------------------------
        """

    def addDataToBuffer(self):
        """
        --------------------------------------------------
        addDataToBuffer()
        --------------------------------------------------
        This method converts the byte values to string
        values and adds them to buffer.
        --------------------------------------------------
        """

    def transmitBufferCommands(self):
        """
        --------------------------------------------------
        transmitBufferCommands()
        --------------------------------------------------
        Transmit commands to the corresponding device.
        This method uses an array of commands and sends
        transmits them to a device using a loop. This
        method is usually used when updating data that
        need to bee updated after a given time.
        --------------------------------------------------
        """

    def areAllCommandsTransmitted(self, lastKeyword, cntCommands):
        """
        --------------------------------------------------
        areAllCommandsTransmitted()
        --------------------------------------------------
        Checks to see if all commands that have been
        transmitted by waiting for the last keyword
        received.
        --------------------------------------------------
        """