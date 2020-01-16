#!/usr/bin/env python
#coding: utf8 
 
import time
import RPi.GPIO as GPIO
import os

# pin config for inputs and LEDs, must be the same number of variables! First one is freeze/blackout button
# if you do't want LEDs, enter unused GPIO pins
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
# -- stop recorder
	os.system ('killall -9 ola_recorder')
# all LEDs off
	m = 0
	while m < len (outp):
		GPIO.output(outp[m], GPIO.LOW)
		m = m + 1
# -- LED on		
	GPIO.output(outp[channel], GPIO.HIGH)
# -- start recorder again
	if channel == inp[0]: # -- freeze/blackout button. 
#		os.system ('ola_recorder -p black -u 1 -i 0 &') # -- For blackout, uncomment this line and create a 'black' file with ola_recorder
		GPIO.output(outp[0], GPIO.HIGH)
	else:
		n = 1
		while n < len (outp):
			if channel == inp[n]:
				os.system ('ola_recorder -p show' + n + ' -u 1 -i 0 &') # name your ola_recorder recordings show1, show2... no suffix, and place them in /home/pi  
				GPIO.output(outp[n], GPIO.HIGH)


#	i = i + 1   # debug
     
# declare event
k = 0
while k < len (outp):
	GPIO.add_event_detect(inp[k], GPIO.FALLING, callback = doIfHigh, bouncetime = 200)
	k = k + 1
	
# main loop
while 1:
    time.sleep(0.1)
