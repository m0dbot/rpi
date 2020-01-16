#!/usr/bin/env python
#coding: utf8 
 
import time
import RPi.GPIO as GPIO
import os

# pin config for inputs and LEDs, must be the same number of variables! First one is freeze/blackout
GPIO.setmode(GPIO.BOARD)
inp = [37, 35, 31, 23, 21, 7, 3] 
outp = [38, 36, 32, 24, 22, 5, 11]
GPIO.setwarnings(False) 

# set pins as in/output
j = 0
while j < len(inp):
    GPIO.setup(inp[j], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(outp[j], GPIO.OUT)
    j = j + 1

# run startseqence one time
os.system ('ola_recorder -p startseqence -u 1 -i 1')


#i = 0   # debug

def doIfHigh(channel):
#	global i   # debug
	global inp
	global outp
#	print "Eingang " + str(channel) + " HIGH " + str(i)    # debug
# stop recorder
	os.system ('killall -9 ola_recorder')
# all LEDs off
	m = 0
	while m < len (outp):
		GPIO.output(outp[m], GPIO.LOW)
		m = m + 1
# LED on		
	GPIO.output(outp[channel], GPIO.HIGH)
# start recorder again
	if channel == inp[1]:
		os.system ('ola_recorder -p pastellcolors -u 1 -i 0 &') # replace 'pastellcolors' with your recording's file name, located in /home/pi
	elif channel == inp[2]:
		os.system ('ola_recorder -p primarycolors2 -u 1 -i 0 &')
	elif channel == inp[3]:
		os.system ('ola_recorder -p wwcw -u 1 -i 0 &')
	elif channel == inp[4]:
		os.system ('ola_recorder -p softshow -u 1 -i 0 &')
	elif channel == inp[5]:
		os.system ('ola_recorder -p hardshow -u 1 -i 0 &')
	elif channel == inp[6]:
		os.system ('ola_recorder -p testshow2 -u 1 -i 0 &')
#	elif channel == inp[0]: # freeze button. For blackout, uncomment this line and next and create a 'black' file with ola_recorder
#		os.system ('ola_recorder -p black -u 1 -i 0 &') 

#	i = i + 1   # debug
     
# declare event
k = 0
while k < len (outp):
	GPIO.add_event_detect(inp[k], GPIO.FALLING, callback = doIfHigh, bouncetime = 200)
	k = k + 1
	
# main loop
while 1:
    time.sleep(0.1)
