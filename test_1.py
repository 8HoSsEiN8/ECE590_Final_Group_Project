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

dyno.LHP = 0
dyno.LKP = 0
dyno.LAP = 0

dyno.CHP = 0
dyno.CKP = 0
dyno.CAP = 0

dyno.RHP = 0
dyno.RKP = 0
dyno.RAP = 0

d.put(dyno)
time.sleep(2)

UL = 5.0
LL = 5.0



def dH(H):
	thetah = -m.acos((H/2.0)/UL)
	thetak = m.pi - 2.0*(m.pi/2.0 - thetah)
	thetaa = 0 + thetah - thetak
	
	A = [thetah , thetak , thetaa]
	
	return A

def rotHip(thetah, thetak, dT):
	thetah = thetah - dT
	thetaa = 0 + thetah - thetak
	
	A = [thetah , thetak , thetaa]
	
	return A
		
squat = dH(9)

dyno.CHP = squat[0]
dyno.CKP = squat[1]
dyno.CAP = squat[2]

dyno.RHP = squat[0]
dyno.RKP = squat[1]
dyno.RAP = squat[2]

dyno.LHP = squat[0]
dyno.LKP = squat[1]
dyno.LAP = squat[2]
d.put(dyno)
time.sleep(1)
#RAISE INNER LEG
B = dH(7)
dyno.CHP = B[0]
dyno.CKP = B[1]
dyno.CAP = B[2]
d.put(dyno)
time.sleep(1)

C = rotHip(dyno.CHP, dyno.CKP, .5)
dyno.CHP = C[0]
dyno.CAP = C[2]
d.put(dyno)
time.sleep(1)

A = dH(6)

dyno.RHP = A[0]
dyno.RKP = A[1]
dyno.RAP = A[2]

dyno.LHP = A[0]
dyno.LKP = A[1]
dyno.LAP = A[2]
d.put(dyno)

time.sleep(1)

for i in range(1,9):
	dyno.CKP = dyno.CKP + 1.0/10.0
	d.put(dyno)
	time.sleep(.075)



dyno.CHP = squat[0]
dyno.CKP = squat[1]
dyno.CAP = squat[2]
C = rotHip(dyno.RHP, dyno.RKP, .5)
dyno.RHP = C[0]
dyno.RAP = C[2]
dyno.LHP = C[0]
dyno.LAP = C[2]
d.put(dyno)

time.sleep(1)
'''
dyno.LHP = squat[0]
dyno.LKP = squat[1]
dyno.LAP = squat[2]
dyno.RHP = squat[0]
dyno.RKP = squat[1]
dyno.RAP = squat[2]
d.put(dyno)
time.sleep(1)

#START OUTER STEP
B = dH(7)
dyno.RHP = B[0]
dyno.RKP = B[1]
dyno.RAP = B[2]
dyno.LHP = B[0]
dyno.LKP = B[1]
dyno.LAP = B[2]
d.put(dyno)
time.sleep(1)

C = rotHip(dyno.RHP, dyno.RKP, .5)
dyno.RHP = C[0]
dyno.RAP = C[2]
dyno.LHP = C[0]
dyno.LAP = C[2]
d.put(dyno)
time.sleep(1)
'''
A = dH(5)

dyno.CHP = A[0]
dyno.CKP = A[1]
dyno.CAP = A[2]
d.put(dyno)

time.sleep(1)
dyno.CAP = dyno.CAP + .2
dyno.LAP = dyno.LAP + .2
dyno.RAP = dyno.RAP + .2
d.put(dyno)
time.sleep(1)

for i in range(1,8):
	dyno.LKP = dyno.LKP + 1.0/10.0
	dyno.RKP = dyno.RKP + 1.0/10.0
	dyno.LHP = dyno.LHP + 1.5/10.0
	dyno.RHP = dyno.RHP + 1.5/10.0
	d.put(dyno)
	time.sleep(.1)

dyno.LHP = squat[0]
dyno.LKP = squat[1]
dyno.LAP = squat[2]
dyno.RHP = squat[0]
dyno.RKP = squat[1]
dyno.RAP = squat[2]
dyno.CHP = squat[0]
dyno.CKP = squat[1]
dyno.CAP = squat[2]
d.put(dyno)
time.sleep(1)

