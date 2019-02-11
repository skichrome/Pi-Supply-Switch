#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
from time import sleep

# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
# Pi pin 28 mapped on pin 7 on power supply, Pi pin 29 mapped on pin 8 on power supply
PinSeven = 20
PinEight = 21
GPIO.setmode(GPIO.BCM) # Set pin numbering to BCM numbering
GPIO.setup(PinSeven, GPIO.IN) # Set up PinSeven as an input
GPIO.setup(PinEight, GPIO.OUT, initial=1) # Setup PinEight as output

while (GPIO.input(PinSeven) == False): # While button not pressed
 GPIO.wait_for_edge(PinSeven, GPIO.RISING) # Wait for a rising edge on PinSeven
 sleep(0.1); # Sleep 100ms to avoid triggering a shutdown when a spike occured
 
sleep(2); # Sleep 2s to distinguish a long press from a short press

if (GPIO.input(PinSeven) == False):
 GPIO.output(PinEight,0) # Bring down PinEight so that the capacitor can discharge and remove power to the Pi
 call('poweroff', shell=False) # Initiate OS Poweroff
else:
 call('reboot', shell=False) # Initiate OS Reboot
