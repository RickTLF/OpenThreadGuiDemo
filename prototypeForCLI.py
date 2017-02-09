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
# Description:
#
# Base class and support functions implemented
# by Computer engineering students of the Avans
# Universety.
#
# This file is part of SandScoop.
# https://github.com/RickTLF/OpenThreadGuiDemo
# (C) 2017
#
#//////////////////////////////////////////////////


from sandScoop import *
import sandScoop
import threading
#import serial
import time

from BasicCom import BasicCom

ser = BasicCom('COM4', 9600)
ser.transmitData('channel\n')
print(ser.receiveData())
ser.transmitData('help\n')
print(ser.receiveData())
ser.transmitData('networkname\n')
print(ser.receiveData())
ser.closeConnection()

# reset_output_buffer()
# reset_input_buffer()