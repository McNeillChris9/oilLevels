#!/usr/bin/python

#-----------------------------------------------------#
#									#
#		Name: Sonic.py					#
#	   Author: James Clarke, Pridopia.			#
#	  Website: http://www.pridopia.co.uk		#
#		 Date: 14 / 11 / 13				#
#		    Version: 1.00					#
#									#
#-----------------------------------------------------#
#
# Copyright 2013 Pridopia ( www.pridopia.co.uk )
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# http://www.pridopia.com/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIC,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either-express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import time, sys, os
import RPi.GPIO as GPIO

# See if they inputted at least 2 Variables.
if len( sys.argv ) < 3:
	print("\n\nTo use, type\npython "+sys.argv[0] + " Trigger_pin Echo_pin\nThey both need to be BCM GPIO Numbers.\n")
	sys.exit()

def Measure():	
	start = 0
	realstart = 0
	realstart = time.time()
	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)
	start = time.time()	
	while GPIO.input(ECHO)==0:		
		start = time.time()
		Dif = time.time() - realstart
		if Dif > 0.2:
			print("Ultrasonic Sensor Timed out, Restarting.")
			time.sleep(0.4)
			Main()
	while GPIO.input(ECHO)==1:		
		stop = time.time()
	elapsed = stop-start
	distance = (elapsed * 36000)/2

	return distance

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ECHO    = int(sys.argv[2])
TRIGGER = int(sys.argv[1])
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO, GPIO.OUT)
GPIO.output(ECHO, False)
GPIO.setup(ECHO,GPIO.IN)
#GPIO.output(TRIGGER, False)

def Main():	
	try:
		while True:
			Distance = Measure()
			print("Distance : %.1f" % Distance)
			time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

Main()
