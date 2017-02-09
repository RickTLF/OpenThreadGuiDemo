# //////////////////////////////////////////////////
# --------------------------------------------------
# SANDSCOOP
# --------------------------------------------------
# //////////////////////////////////////////////////
#
# Developer     :   Rick Kock
# Date          :   25/01/2017
# Team members  :   David de Prez, Tim Spaans
# Institution   :   Avans Hogeschool, Den Bosch
#
# //////////////////////////////////////////////////

import serial

class BasicCom:

    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate, timeout=None)

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
        Transmit data using pySerial. While waiting to
        receive the 'Done' keyword, no other data should
        be transmitted. This process should not be
        interfered. However, note that this may not be
        the final solution.
        """
        self.ser.write(command.encode('ascii'))

    def receiveData(self):
        """Receive any data from device."""
        dataBuffer = [0]
        stringBuffer = []
        index = 0
        while (True):
            # Insert any data you receive in buffer first.
            self.ser.readinto(dataBuffer)
            currentChar = bytearray(dataBuffer).decode('ascii')
            # Check if the current character is relevant for
            # processing the final list of characters.
            if currentChar is '\r':
                continue
            # Skip the first character if it's a space.
            if currentChar is ' ' and index is 0:
                continue
            stringBuffer.append(bytearray(dataBuffer).decode('ascii'))
            index+=1
            if stringBuffer[len(stringBuffer) - 1] == '>':
                print("Done receiving data")
                return stringBuffer

    def filter_answer(self, stringBuffer, lastCommand):
        """Omit the command transmitted and the '>' character
        To only get the answer."""

        # Iterate through the strings and
        # compare the characters. If the characters
        # match before a newline, discard whatever
        # characters came befor it.
        for letter in stringBuffer:
            if letter is lastCommand[letter]:


        '''if currentChar is '\r':
            continue
        # Skip the first character if it's a space.
        if currentChar is ' ' and index is 0:
            continue
        stringBuffer.append(bytearray(dataBuffer).decode('ascii'))
        index += 1
        if stringBuffer[len(stringBuffer) - 1] == '>':
            print("Done receiving data")
            return stringBuffer'''

    def __wait(self, keyword):
        """
        Wait for a particular keyword to be received. Once
        received, it means you've received all the data
        from the device and the program may proceed.
        """
        self.__receiveData()

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
        Checks to see if all commands that have been
        transmitted by waiting for the last keyword
        received.
        """

    def closeConnection(self):
        self.ser.close()

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -