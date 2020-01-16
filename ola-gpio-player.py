#!/usr/bin/env python
#coding: utf8 
 
import time
import RPi.GPIO as GPIO
import os
 
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)

# Pinkonfiguration für Inputs und LEDs, muss die gleiche Anzahl sein!
inp = [37, 35, 31, 23, 21, 7, 3]
outp = [38, 36, 32, 24, 22, 5, 11]

GPIO.setwarnings(False) 

# Pins als Eingang/Ausgang festlegen
j = 0
while j < len(inp):
    GPIO.setup(inp[j], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(outp[j], GPIO.OUT)
    j = j + 1

# Startsequenz 1x abefeuern
os.system ('ola_recorder -p startseqneu -u 1 -i 1')


#i = 0

def doIfHigh(channel):
    # Zugriff auf Variable i ermöglichen
	global i
	global inp
	global outp
# Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
	print "Eingang " + str(channel) + " HIGH " + str(i)
# Recorder stoppen
	os.system ('killall -9 ola_recorder')
# LEDs aus
	m = 0
	while m < len (outp):
		GPIO.output(outp[m], GPIO.LOW)
		m = m + 1
#Recorder wieder starten
	if channel == inp[1]:
		os.system ('ola_recorder -p pastellcolors -u 1 -i 0 &')
		GPIO.output(outp[1], GPIO.HIGH)
	elif channel == inp[2]:
		os.system ('ola_recorder -p primarycolors2 -u 1 -i 0 &')
		GPIO.output(outp[2], GPIO.HIGH)
	elif channel == inp[3]:
		os.system ('ola_recorder -p wwcw -u 1 -i 0 &')
		GPIO.output(outp[3], GPIO.HIGH)
	elif channel == inp[4]:
		os.system ('ola_recorder -p softshow -u 1 -i 0 &')
		GPIO.output(outp[4], GPIO.HIGH)
	elif channel == inp[5]:
		os.system ('ola_recorder -p hardshow -u 1 -i 0 &')
		GPIO.output(outp[5], GPIO.HIGH)
	elif channel == inp[6]:
		os.system ('ola_recorder -p testshow2 -u 1 -i 0 &')
		GPIO.output(outp[6], GPIO.HIGH)
	elif channel == inp[0]:
		GPIO.output(outp[0], GPIO.HIGH)   
#	i = i + 1
     
# Ereignis deklarieren
k = 0
while k < len (outp):
	GPIO.add_event_detect(inp[k], GPIO.FALLING, callback = doIfHigh, bouncetime = 200)
	k = k + 1
	
# main loop
while 1:
    time.sleep(0.1)
