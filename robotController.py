import os
import dynamixel
import time
import random
import sys
import subprocess
import optparse
import yaml
import numpy as np
import ach
import math as m

import controller_include as ci
import dyno_include as di

c = ach.Channel(ci.CONTROLLER_REF_NAME)
controller 	= ci.KEY_REF()
c.flush()

d = ach.Channel(di.DYNO_REF_NAME)
dyno 		= di.DYNO_REF()
d.flush()

dyno.LHP = -.1
dyno.LKP = -.2
dyno.LAP = .1

dyno.CHP = -.1
dyno.CKP = -.2
dyno.CAP = .1

dyno.RHP = -.1
dyno.RKP = -.2
dyno.RAP = .1

d.put(dyno)
time.sleep(2)

while(1):
	
	[statuss, framesizes] = c.get(controller, wait=True, last=True)
	
	if (controller.direction == ci.FORWARD):
		print '\nMoving Fowrad ...'
		dyno.LHP = -1
		dyno.LKP = -2
		dyno.LAP = 1
		
		dyno.RHP = -1
		dyno.RKP = -2
		dyno.RAP = 1
		
		d.put(dyno)
		time.sleep(1)

		dyno.CHP = -.2
		dyno.CKP = -.4
		dyno.CAP = .2
		d.put(dyno)

		
			
	elif (controller.direction == ci.REVERSE):
		print '\nMoving Backward ...'
		dyno.LHP = -.2
		dyno.LKP = -.4
		dyno.LAP = .2

		dyno.CHP = -1
		dyno.CKP = -2
		dyno.CAP = 1

		dyno.RHP = -.2
		dyno.RKP = -.4
		dyno.RAP = .2
		
		d.put(dyno)

	elif (controller.direction == ci.RIGHT):
		print '\nTurning Right ...'
		dyno.CHR = .2
		d.put(dyno)

	elif (controller.direction == ci.LEFT):
		print '\nTurning Left ...'
		dyno.CHR = -.2
		d.put(dyno)

	elif (controller.direction == ci.STOP):
		print '\nStopped'
		dyno.LHR = 0
		dyno.LHP = 0
		dyno.LKP = 0
		dyno.LAP = 0

		dyno.CHR = 0
		dyno.CHP = 0
		dyno.CKP = 0
		dyno.CAP = 0

		dyno.RHR = 0
		dyno.RHP = 0
		dyno.RKP = 0
		dyno.RAP = 0
		
		d.put(dyno)
	
